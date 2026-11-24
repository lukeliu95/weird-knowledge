#!/usr/bin/env python3
"""20个真实事件的离线配对试验；方法见docs/2026-11-24-event-judgment-plan.md。

prepare  冻结公开知识及无答案检索结果（4次现有订阅调用）。
freeze   独立核查后锁定题目、答案、材料、协议和脚本哈希。
run      两组各跑两遍，每5题一批，16次无工具独立调用；可断点续跑。
score    确定性算分、按20个事件重采样，生成隐藏组别的辅助审查材料。
self-test 用明确合成数据检验格式拒绝、算分与统计；不调用模型。
"""
import argparse, concurrent.futures as cf, datetime as dt, hashlib, json, math, os, random, re, subprocess, sys, tempfile, time
from pathlib import Path

REPO=Path(__file__).resolve().parents[2]
DATA=REPO/'docs/evals/2026-11-24-events'
WORK=REPO/'private/review-work/2026-11-24-event-eval'
sys.path.insert(0,str(Path(__file__).resolve().parent))
import opus_judge as OJ
from l1_eval import Index

LABELS=('S','C','U'); BATCH=5; REPEATS=2; TOP=40; TAKE=4; CHAR_CAP=90000
SYS='''你是基于证据分析事件的助手。只输出JSON，不调用工具。只依据本题提供的事实判断待判断主张。
S（支持）：材料对主张有正面证据，范围相符。C（反驳）：材料给出相反结果或与主张直接矛盾。
U（不足）：主张可能为真也可能为假，现有材料缺条件、识别或外推依据，不能确定。证据不足不自动等于反驳。
题目主张由测试编写者提出，不是原作者引语。知识材料只提供一般道理，不能替事件补造事实；与事实冲突时不能照套。
每题给出判断、三类概率、关键理由、适用边界、一个能检验判断的具体下一步。不要用理论名字代替事实。'''
FORMAT='''输出 {"answers":[{"id":"E01","label":"S或C或U","probs":{"S":0.8,"C":0.1,"U":0.1},"reason":"关键事实和判断理由，120字内","boundary":"最需要保留的边界，100字内","next_check":"一个具体可查或可测的下一步，100字内","used_knowledge":["实际使用的已提供知识编号，没有则空数组"]}]}。
概率各在0到1之间、合计为1；label须为最高概率类别之一。每个id恰好答一次。不得使用未提供的知识编号。'''


def read(p):return json.loads(p.read_text())
def write(p,obj):
 p.parent.mkdir(parents=True,exist_ok=True)
 with tempfile.NamedTemporaryFile(mode='w',encoding='utf-8',dir=p.parent,prefix=p.name+'.',suffix='.tmp',delete=False) as f:
  f.write(json.dumps(obj,ensure_ascii=False,indent=2)+'\n');f.flush();os.fsync(f.fileno());tmp=f.name
 os.replace(tmp,p)
def digest(data):return hashlib.sha256(data).hexdigest()
def stamp():return dt.datetime.now(dt.timezone(dt.timedelta(hours=9))).isoformat(timespec='seconds')
def chunks(rows,n=BATCH):return [rows[i:i+n] for i in range(0,len(rows),n)]
def section(t,name):
 m=re.search(r'^## '+re.escape(name)+r'\s*\n(.*?)(?=^## |\Z)',t,re.S|re.M)
 return m.group(1).strip() if m else ''
def front(t,k):
 m=re.search('^'+re.escape(k)+r':[ \t]*(.*)$',t.split('\n---',1)[0],re.M);v=m.group(1).strip() if m else ''
 return json.loads(v) if v.startswith('"') else v

def public_text(s):
 s=re.sub(r'https?://[^\s)）]+','（出处链接略）',s)
 for p in ['lukeliu95','LukeLiu95','刘仙升','simprr','lukeeMind','Luke']:
  s=re.sub(re.escape(p),'用户',s,flags=re.I)
 return s

def cases():
 rs=read(DATA/'cases.json');assert len(rs)==20 and len({r['id'] for r in rs})==20
 return rs

def packet(r):
 # 不读取标准答案、评分锚点、整理结论或私人档案。
 return {k:r[k] for k in ('id','title','date','domain','facts','claim')}

def validate_answers(obj,rs,allowed):
 if not isinstance(obj,dict) or not isinstance(obj.get('answers'),list):raise ValueError('answers不是列表')
 rows=obj['answers'];expected={r['id'] for r in rs}
 if len(rows)!=len(expected) or {r.get('id') for r in rows}!=expected:raise ValueError('id缺失、重复或越界')
 out=[]
 for r in rows:
  cid=r['id'];p=r.get('probs',{})
  if set(p)!=set(LABELS) or r.get('label') not in LABELS:raise ValueError('类别格式不合法')
  if any(isinstance(p[k],bool) or not isinstance(p[k],(int,float)) or not math.isfinite(p[k]) or not 0<=p[k]<=1 for k in LABELS):raise ValueError('概率非有限数或越界')
  z=sum(p.values())
  if abs(z-1)>0.001:raise ValueError('概率合计不为1')
  p={k:float(v)/z for k,v in p.items()}
  if p[r['label']]<max(p.values())-1e-9:raise ValueError('label不是最高概率')
  for k in ('reason','boundary','next_check'):
   if not isinstance(r.get(k),str) or not r[k].strip():raise ValueError('解释字段为空')
  used=r.get('used_knowledge',[])
  if not isinstance(used,list) or any(not isinstance(x,str) for x in used) or not set(used)<=set(allowed.get(cid,[])):raise ValueError('知识编号越界')
  out.append({**r,'probs':p,'used_knowledge':used})
 return {r['id']:r for r in out}

class CallFailure(RuntimeError):
 def __init__(self,message,meta=None):
  super().__init__(message);self.meta=meta or {}

def model_call(system,prompt):
 if len(prompt)>CHAR_CAP:raise ValueError('提示词超限，拒绝静默截断')
 # 仅本次子进程禁用全局/项目说明、记忆、命令和hooks；不改用户配置。
 env=dict(os.environ,CLAUDE_CODE_DISABLE_CLAUDE_MDS='1',CLAUDE_CODE_DISABLE_AUTO_MEMORY='1',CLAUDE_CODE_DISABLE_ORG_MEMORY='1')
 cmd=['claude','-p','--model',OJ.MODEL,'--system-prompt',system,'--tools','','--strict-mcp-config',
      '--no-session-persistence','--disable-slash-commands','--setting-sources','','--settings','{"disableAllHooks":true}',
      '--effort','low','--output-format','json']
 try:r=subprocess.run(cmd,input=prompt,capture_output=True,text=True,timeout=600,cwd='/tmp',env=env)
 except subprocess.TimeoutExpired:raise CallFailure('claude调用600秒超时，用量未知',dict(usage_status='unknown',usage_unknown_reason='timeout'))
 try:d=json.loads(r.stdout)
 except (ValueError,TypeError):
  raise CallFailure('claude外层输出不是JSON，退出码'+str(r.returncode),dict(usage_status='unknown',usage_unknown_reason='unparseable_cli_output'))
 meta=dict(cost_usd=d.get('total_cost_usd'),usage=d.get('usage'),duration_ms=d.get('duration_ms'),model_usage=d.get('modelUsage'),session_persisted=False)
 meta['usage_status']='known' if meta['usage'] is not None and meta['cost_usd'] is not None else 'unknown'
 if r.returncode:raise CallFailure('claude进程失败，退出码'+str(r.returncode),meta)
 if not meta['model_usage'] or set(meta['model_usage'])!={OJ.MODEL}:raise CallFailure('实际模型与协议不符',meta)
 text=d.get('result','')
 if d.get('is_error'):raise CallFailure('claude报告错误：'+public_text(text[:300]),meta)
 try:
  i=text.index('{');obj,_=json.JSONDecoder().raw_decode(text[i:])
 except (ValueError,TypeError):
  meta['unparsed_result']=text
  raise CallFailure('模型未提供可解析JSON：'+public_text(text[:200]),meta)
 return obj,meta

def dependency_paths():
 return {'SCRIPT':Path(__file__),'MODEL_HELPER':Path(OJ.__file__),'INDEX_HELPER':REPO/'tools/evolve/l1_eval.py'}

def prompt_for(group,arm,kb):
 body=[];allowed={}
 for r in group:
  its=kb[r['id']]['items'] if arm=='knowledge' else [];allowed[r['id']]=[x['id'] for x in its]
  body.append(dict(event=packet(r),knowledge=its))
 return json.dumps(body,ensure_ascii=False)+'\n'+FORMAT,allowed


def prepare(_):
 if (DATA/'frozen.json').exists():raise RuntimeError('已冻结，不能改准备材料')
 if (DATA/'knowledge-packets.json').exists():raise RuntimeError('准备材料已存在，不能静默重做或重复花用量')
 rs=cases();corpus=[];manifest={};novelty=[]
 for f in sorted((REPO/'roots').glob('*.md')):
  t=f.read_text();manifest[str(f.relative_to(REPO))]=digest(f.read_bytes())
  if front(t,'verified')=='false':continue
  name=front(t,'name_zh');en=front(t,'name_en');typ=front(t,'type')
  # 原始出处中的争议和限制保留；反向链接和clips内容不进入索引或提示词。
  content=public_text(f'类型：{typ}；出处已核实不等于命题普遍正确。\n定义：{section(t,"一句话")}\n出处及限制：{section(t,"原始出处")}\n更底层：{section(t,"更底层的源头")}')
  corpus.append(dict(id=f.stem,name=name,name_en=en,type=typ,content=content[:1800],text=public_text(name+' '+en+' '+section(t,'一句话'))))
 texts=[(str(p.relative_to(REPO)),p.read_text()) for folder in ('roots','clips') for p in (REPO/folder).glob('*.md')]
 from urllib.parse import urlsplit
 for r in rs:
  tail=urlsplit(r['source']['url']).path.rstrip('/')
  hits=[n for n,t in texts if tail.lower() in t.lower()]
  novelty.append(dict(id=r['id'],source_path=tail,direct_source_hits=hits))
 if any(r['direct_source_hits'] for r in novelty):raise RuntimeError('题集有同源事件已入库，先人工排查')
 write(DATA/'novelty-audit.json',novelty)
 idx=Index(corpus);candidates={}
 for r in rs:
  q=r['title']+' '+r['claim']+' '+' '.join(x['text'] for x in r['facts'])
  candidates[r['id']]=idx.top(q,TOP)
 write(WORK/'corpus.json',corpus);write(WORK/'candidates.json',candidates)
 write(DATA/'corpus-manifest.json',dict(created=stamp(),total_roots=len(manifest),eligible_verified_roots=len(corpus),hashes=manifest))
 outputs={};prep=WORK/'prepare-calls';prep.mkdir(parents=True,exist_ok=True)
 for i,group in enumerate(chunks(rs)):
  cp=prep/f'batch-{i}.json'
  payload=[dict(event=packet(r),candidates=[dict(id=x['id'],name=x['name'],type=x['type'],definition=x['text'][:180]) for x in candidates[r['id']]]) for r in group]
  prompt=json.dumps(payload,ensure_ascii=False)+'\n每题从自己的候选中选0到4个最有助于判断的基础知识，可不选。只输出 {"E01":{"ids":["编号"],"why":"选择依据，60字内"}}。不回答题目，不给S/C/U。不从候选外自造编号。'
  ph=digest(prompt.encode())
  if cp.exists():
   rec=read(cp)
   if rec.get('prompt_hash')!=ph:raise RuntimeError('已有检索调用与当前输入不符')
   # 第一批旧记录是同一提示的首个尝试；无损迁移，保留原输出和用量。
   if 'attempts' not in rec:rec=dict(prompt_hash=ph,attempts=[rec])
  else:rec=dict(prompt_hash=ph,attempts=[])
  def selection_errors(obj):
   errors=[]
   if not isinstance(obj,dict):return ['输出不是对象']
   if set(obj)!={r['id'] for r in group}:errors.append('题号缺失或越界')
   for r in group:
    sel=obj.get(r['id'],{});ids=sel.get('ids',[]) if isinstance(sel,dict) else None
    lookup={x['id'] for x in candidates[r['id']]}
    if not isinstance(ids,list) or any(not isinstance(x,str) for x in ids) or len(ids)>TAKE or len(ids)!=len(set(ids)) or not set(ids)<=lookup:errors.append(r['id']+'选材编号不合法')
   return errors
  for attempt in range(2):
   if attempt>=len(rec['attempts']):
    started=stamp()
    try:
     obj,meta=model_call('你负责从公开知识索引中选材料；不判断题目答案。只输出JSON。',prompt)
     rec['attempts'].append(dict(started=started,finished=stamp(),output=obj,meta=meta))
    except Exception as e:
     rec['attempts'].append(dict(started=started,finished=stamp(),output={},meta=getattr(e,'meta',{}),error=type(e).__name__+': '+str(e)[:300]))
   at=rec['attempts'][attempt];errors=selection_errors(at.get('output',{}))
   if errors:at['error']='；'.join(errors)
   write(cp,rec)
   if not errors:break
  obj=rec['attempts'][attempt].get('output',{});audit={}
  for r in group:
   sel=obj.get(r['id'],{}) if isinstance(obj,dict) else {};sel=sel if isinstance(sel,dict) else {}
   raw=sel.get('ids',[]);raw=raw if isinstance(raw,list) else []
   lookup={x['id']:x for x in candidates[r['id']]};ids=[];dropped=[]
   for x in raw:
    if not isinstance(x,str) or x not in lookup or x in ids or len(ids)>=TAKE:dropped.append(x)
    else:ids.append(x)
   audit[r['id']]=dict(retained=ids,dropped=dropped)
   outputs[r['id']]=dict(candidate_ids=list(lookup),selection_reason=sel.get('why',''),selection_attempts=attempt+1,dropped_ids=dropped,items=[{k:lookup[x][k] for k in ('id','name','type','content')} for x in ids])
  rec['final_selection_audit']=audit;write(cp,rec)
 write(DATA/'knowledge-packets.json',outputs)
 print('检索已完成：',len(outputs),'题，材料数',sum(len(v['items']) for v in outputs.values()),flush=True)

def frozen_files():return ['cases.json','gold.json','knowledge-packets.json','corpus-manifest.json','novelty-audit.json','protocol.md']
def freeze(_):
 p=DATA/'frozen.json'
 if p.exists():raise RuntimeError('已冻结，拒绝覆盖')
 fs={n:digest((DATA/n).read_bytes()) for n in frozen_files()};fs.update({n:digest(p.read_bytes()) for n,p in dependency_paths().items()})
 cli_version=subprocess.run(['claude','--version'],capture_output=True,text=True,check=True).stdout.strip()
 write(p,dict(created=stamp(),model=OJ.MODEL,cli_version=cli_version,effort='low',batch=BATCH,repeats=REPEATS,hashes=fs))
 print('已冻结题目、标准答案、知识材料、协议和脚本。')
def check_freeze():
 f=read(DATA/'frozen.json');assert f['model']==OJ.MODEL,'模型已改变'
 for n,h in f['hashes'].items():
  p=dependency_paths().get(n,DATA/n)
  if digest(p.read_bytes())!=h:raise RuntimeError('冻结文件发生改变：'+n)
 return f

def run(a):
 frozen=check_freeze();freeze_hash=digest((DATA/'frozen.json').read_bytes());rs=cases();kb=read(DATA/'knowledge-packets.json');jobs=[]
 for repeat in range(REPEATS):
  ordered=list(rs);random.Random(20261124+repeat).shuffle(ordered)
  for bi,group in enumerate(chunks(ordered)):
   for arm in ('base','knowledge'):
    jid=f'{arm}-r{repeat+1}-b{bi+1}'
    jobs.append((jid,arm,repeat+1,group))
 random.Random(24112026).shuffle(jobs)
 run_dir=DATA/'runs';run_dir.mkdir(exist_ok=True)
 def task(job):
  jid,arm,repeat,group=job;target=run_dir/(jid+'.json')
  prompt,allowed=prompt_for(group,arm,kb);ph=digest(prompt.encode())
  if target.exists():
   record=read(target)
   if record.get('prompt_hash')!=ph or record.get('frozen_hash')!=freeze_hash:raise RuntimeError('已有运行与冻结输入不符：'+jid)
   if record.get('state')=='finished':return jid,'已有结果，未重跑'
  else:
   record=dict(job=jid,arm=arm,repeat=repeat,ids=[r['id'] for r in group],model=OJ.MODEL,started=stamp(),prompt_hash=ph,frozen_hash=freeze_hash,prompt_chars=len(prompt),attempts=[],state='running')
  for at in record['attempts']:
   if at.get('status')=='in_flight':
    at.update(status='interrupted',error='调用中断，是否完成及用量未知；占用一次尝试预算，不能静默重跑',finished=stamp())
  write(target,record)
  for attempt in range(len(record['attempts']),2):
   began=time.monotonic();at=dict(status='in_flight',started=stamp());record['attempts'].append(at);write(target,record)
   try:
    obj,meta=model_call(SYS,prompt)
    at.update(output=obj,meta=meta,elapsed_seconds=round(time.monotonic()-began,3),finished=stamp())
    answers=validate_answers(obj,group,allowed)
    at['status']='complete';record.update(valid=True,answers=answers,finished=stamp(),state='finished');write(target,record);break
   except Exception as e:
    at.update(status='failed',error=type(e).__name__+': '+str(e)[:300],elapsed_seconds=round(time.monotonic()-began,3),finished=stamp())
    if isinstance(e,CallFailure):at['meta']=e.meta
    write(target,record)
  else:
   record.update(valid=False,answers={},finished=stamp(),state='finished');write(target,record)
  return jid,('完成' if record['valid'] else '失败，计入结果')
 with cf.ThreadPoolExecutor(max_workers=a.workers) as ex:
  for fu in cf.as_completed([ex.submit(task,j) for j in jobs]):print(*fu.result(),flush=True)
 check_freeze();print('16批执行结束；不改题、不挑运行。',flush=True)

def brier(p,y):return sum((p[k]-(k==y))**2 for k in LABELS)
def boot(values,n=10000):
 rnd=random.Random(20261124);arr=sorted(sum(rnd.choices(values,k=len(values)))/len(values) for _ in range(n))
 return dict(mean=sum(values)/len(values),ci90=[arr[int(n*.05)],arr[int(n*.95)]],positive_fraction=sum(v>1e-12 for v in arr)/n,zero_fraction=sum(abs(v)<=1e-12 for v in arr)/n)
def sign_test(ds):
 pos=sum(d>1e-12 for d in ds);neg=sum(d<-1e-12 for d in ds);n=pos+neg
 return dict(positive=pos,negative=neg,tied=len(ds)-n,two_sided_p=min(1,2*sum(math.comb(n,k) for k in range(min(pos,neg)+1))/(2**n)))

def score(_):
 check_freeze();freeze_hash=digest((DATA/'frozen.json').read_bytes());rs=cases();gold={r['id']:r for r in read(DATA/'gold.json')};kb=read(DATA/'knowledge-packets.json');records={};logs=[]
 for p in sorted((DATA/'runs').glob('*.json')):
  rec=read(p)
  if rec.get('state')!='finished':raise RuntimeError('有未结束运行：'+p.name)
  group=[next(r for r in rs if r['id']==cid) for cid in rec['ids']]
  prompt,allowed=prompt_for(group,rec['arm'],kb)
  if rec.get('frozen_hash')!=freeze_hash or rec.get('prompt_hash')!=digest(prompt.encode()):raise RuntimeError('运行输入不符：'+p.name)
  if rec['valid'] and validate_answers({'answers':list(rec['answers'].values())},group,allowed)!=rec['answers']:raise RuntimeError('结果不一致')
  logs.append(rec)
  for cid in rec['ids']:
   key=(rec['arm'],rec['repeat'],cid)
   if key in records:raise ValueError('运行出现重复结果')
   records[key]=rec['answers'].get(cid)
 if len(logs)!=16 or len(records)!=80:raise RuntimeError('未完成全部16批/80份判断，不能省略缺失结果')
 per=[];by_run=[];blind=[];mapping={};usage=[]
 for arm in ('base','knowledge'):
  for repeat in (1,2):
   correct=valid=0;bs=[]
   for r in rs:
    o=records[(arm,repeat,r['id'])];valid+=bool(o);correct+=bool(o and o['label']==gold[r['id']]['label']);bs.append(brier(o['probs'],gold[r['id']]['label']) if o else 2.0)
    alias=digest((arm+str(repeat)+r['id']+'event-eval-v1').encode())[:16]
    mapping[alias]=dict(arm=arm,repeat=repeat,event=r['id'])
    # 隐藏组别、概率、知识编号与材料命中率；只审解释质量。
    out={k:o[k] for k in ('label','reason','boundary','next_check')} if o else dict(label='INVALID',reason='',boundary='',next_check='')
    blind.append(dict(alias=alias,event_id=r['id'],event=packet(r),rubric=gold[r['id']],output=out))
   by_run.append(dict(arm=arm,repeat=repeat,n=20,valid=valid,correct=correct,accuracy=correct/20,brier=sum(bs)/20))
 for r in rs:
  row=dict(id=r['id'],title=r['title'],gold=gold[r['id']]['label'])
  for arm in ('base','knowledge'):
   os=[records[(arm,repeat,r['id'])] for repeat in (1,2)]
   row[arm]=dict(labels=[o['label'] if o else 'INVALID' for o in os],accuracy=sum(bool(o and o['label']==row['gold']) for o in os)/2,brier=sum(brier(o['probs'],row['gold']) if o else 2 for o in os)/2,knowledge_uses=[o.get('used_knowledge',[]) if o else [] for o in os])
  per.append(row)
 for r in logs:
  for at in r['attempts']:
   usage.append(dict(stage='answer',job=r['job'],elapsed_seconds=at.get('elapsed_seconds'),**at.get('meta',{}),error=at.get('error')))
 for p in sorted((WORK/'prepare-calls').glob('*.json')):
  r=read(p)
  for at in r.get('attempts',[r]):usage.append(dict(stage='retrieval',job=p.stem,**at.get('meta',{}),error=at.get('error')))
 ds=[r['knowledge']['accuracy']-r['base']['accuracy'] for r in per]
 db=[r['base']['brier']-r['knowledge']['brier'] for r in per]
 summ=dict(created=stamp(),model=OJ.MODEL,event_n=20,repeats=2,by_run=by_run,accuracy_delta=boot(ds),brier_improvement=boot(db),event_sign_test=sign_test(ds),per_event=per,call_count=len(usage),failed_attempts=sum(bool(x.get('error')) for x in usage),unknown_usage_calls=sum(x.get('usage') is None or x.get('cost_usd') is None for x in usage),api_equivalent_usd_known_subtotal=sum(x.get('cost_usd') or 0 for x in usage),usage=usage,limitations=['事件为定向选择的20个推论题，不是随机代表全体事件。','给定事实内可能含直接答案，存在天花板；历史事件也可能已在模型训练中出现。','知识组额外上下文更长，本轮没有等长度无关材料安慰剂组。','重采样只描述这20题的不确定性，不是知识有效的贝叶斯后验概率。'])
 write(DATA/'scores.json',summ)
 random.Random(777).shuffle(blind);write(DATA/'judgments-blind.json',blind);write(WORK/'blind-map.json',mapping)
 print(json.dumps({k:v for k,v in summ.items() if k not in ('per_event','usage')},ensure_ascii=False,indent=2))

def self_test(_):
 fake=[dict(id='E99')];allowed={'E99':[]}
 good=dict(answers=[dict(id='E99',label='S',probs={'S':.7,'C':.2,'U':.1},reason='合成校验用，不是真实事件',boundary='合成',next_check='合成',used_knowledge=[])])
 assert validate_answers(good,fake,allowed)['E99']['label']=='S'
 import copy
 for alter in ['nan','wrong_sum','wrong_label','unknown_knowledge','duplicate','bool']:
  x=copy.deepcopy(good);r=x['answers'][0]
  if alter=='nan':r['probs']['S']=float('nan')
  if alter=='wrong_sum':r['probs']['S']=.4
  if alter=='wrong_label':r['label']='C'
  if alter=='unknown_knowledge':r['used_knowledge']=['invented']
  if alter=='duplicate':x['answers'].append(r)
  if alter=='bool':r['probs']['S']=True
  try:validate_answers(x,fake,allowed)
  except ValueError:pass
  else:raise AssertionError(alter)
 assert brier({'S':1,'C':0,'U':0},'S')==0
 assert brier({'S':0,'C':1,'U':0},'S')==2
 assert abs(brier({'S':1/3,'C':1/3,'U':1/3},'S')-2/3)<1e-9
 assert boot([0]*20)['ci90']==[0,0] and sign_test([0]*20)['two_sided_p']==1
 assert sign_test([1]*5+[0]*15)['two_sided_p']==.0625
 assert 'key_fact' not in packet(dict(id='x',title='x',date='x',domain='x',facts=[],claim='x',key_fact='secret'))
 print('合成格式/拒绝/泄漏字段/Brier边界/配对统计校验通过；未调用模型。')

def main():
 p=argparse.ArgumentParser();s=p.add_subparsers(dest='cmd',required=True)
 for n in ('prepare','freeze','score','self-test'):s.add_parser(n)
 r=s.add_parser('run');r.add_argument('--workers',type=int,default=2)
 a=p.parse_args();{'prepare':prepare,'freeze':freeze,'run':run,'score':score,'self-test':self_test}[a.cmd](a)
if __name__=='__main__':main()
