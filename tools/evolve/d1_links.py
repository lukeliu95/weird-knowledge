#!/usr/bin/env python3
"""D1 出处核查：检查 roots/ 里「原始出处」的链接还能不能打开。

用法：
  python3 tools/evolve/d1_links.py [--workers 6]

结果写进 private/d1/links-时间.jsonl，成绩追加进 private/d1/metrics.jsonl。
请求头只用通用的 weird-knowledge-research-bot，不带任何个人信息。
"""
import argparse, concurrent.futures as cf, datetime as dt, json, re, urllib.error, urllib.parse, urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
PRIVATE = REPO / "private"
UA = {"User-Agent": "Mozilla/5.0 (compatible; weird-knowledge-research-bot)"}
URL = re.compile(r"https?://[^\s（）\]>，。；、\"`]+")


def clean(u):
    """Trim trailing punctuation and an unbalanced closing paren (markdown link), keep Wikipedia-style (x)."""
    u = u.rstrip(",;:'")
    if u.endswith(".") and not re.search(r"/wiki/[^/]*\.$", u):   # keep Wikipedia titles like Chandler_Jr.
        u = u.rstrip(".")
    while u.endswith(")") and u.count(")") > u.count("("):
        u = u[:-1]
    return urllib.parse.quote(u, safe=":/?#[]@!$&'()*+,;=%~")


def section(t, title):
    m = re.search(rf"^## {title}\n(.*?)(?=^## |\Z)", t, re.S | re.M)
    return m.group(1) if m else ""


def check(url):
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, headers=UA, method=method)
            with urllib.request.urlopen(req, timeout=20) as r:
                return r.status, r.geturl()
        except urllib.error.HTTPError as e:
            if method == "GET" or e.code not in (403, 405, 400, 429, 501):
                return e.code, url
        except Exception as e:  # timeouts, TLS, DNS
            if method == "GET":
                return type(e).__name__, url
    return "unknown", url


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=6)
    a = ap.parse_args()
    items, repaired = [], set()
    for f in sorted((REPO / "roots").glob("*.md")):
        for line in section(f.read_text(), "原始出处").split("\n"):
            urls = [clean(u) for u in URL.findall(line)]
            if ("web.archive.org" in line or "doi.org" in line) and "打不开" in line:
                repaired.update((f.stem, u) for u in urls if "web.archive.org" not in u and "doi.org" not in u)
            items += [(f.stem, u) for u in urls]
        items = list(dict.fromkeys(items))
    out = []
    with cf.ThreadPoolExecutor(a.workers) as ex:
        for (slug, url), (status, final) in zip(items, ex.map(lambda x: check(x[1]), items)):
            out.append(dict(root=slug, url=url, status=status, final=final))
    ok = [r for r in out if isinstance(r["status"], int) and r["status"] < 400]
    blocked = [r for r in out if r["status"] in (401, 403, 429)]
    fixed = [r for r in out if (r["root"], r["url"]) in repaired and r not in ok]
    dead = [r for r in out if r not in ok and r not in blocked and r not in fixed]
    stamp = f"{dt.datetime.now():%Y%m%d-%H%M}"
    d = PRIVATE / "d1"
    d.mkdir(parents=True, exist_ok=True)
    (d / f"links-{stamp}.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in out))
    rec = dict(time=stamp, links=len(out), roots=len({r['root'] for r in out}), ok=len(ok), blocked=len(blocked), repaired=len(fixed),
               dead=len(dead), dead_rate=round(len(dead) / max(1, len(out)), 3))
    with open(d / "metrics.jsonl", "a") as f:
        f.write(json.dumps(rec) + "\n")
    print(json.dumps(rec))
    for r in dead[:40]:
        print(r["status"], r["root"], r["url"])


if __name__ == "__main__":
    main()
