"""交给 Opus 或外部服务前去掉客户名、人名的小工具，和调本地 Qwen 出 JSON。

原来写在 salesroom.py 里。Luke 2026-10-28 让 lukeeMind 不再读 Salesroom（选了 A），salesroom.py 和会议数据已挪进废纸篓；
客户名单留了一份在 private/mind/scrub-names.json，只用来去名，不做别的用。
"""
import json, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "evolve"))
import l1_eval as E  # noqa: E402

NAMES = E.PRIVATE / "mind" / "scrub-names.json"
HONORIFIC = re.compile(r"[一-鿿぀-ヿA-Za-z]{1,8}(?:氏|さん|様|さま|部長|課長|社長|会長|専務|常務)")


def all_customer_names():
    return json.loads(NAMES.read_text()) if NAMES.exists() else []


def scrub(s, names):
    """所有客户公司名、带敬称的人名都换掉。"""
    for n in names:
        s = s.replace(n, "某客户")
    return HONORIFIC.sub("某人", s)


def qwen_json(prompt, max_tokens=1800):
    d = E.post(E.os.environ["QWEN_BASE_URL"] + "/chat/completions", {
        "model": "qwen3.8-27b-coder390-mlx-mixed4-mtp",
        "messages": [{"role": "system", "content": "只输出一个 JSON 对象，不要多余的字。"},
                     {"role": "user", "content": prompt}],
        "max_tokens": max_tokens, "temperature": 0, "chat_template_kwargs": {"enable_thinking": False}},
        E.os.environ["QWEN_API_KEY"])
    text = d["choices"][0]["message"]["content"]
    i = text.find("{")
    obj, _ = json.JSONDecoder().raw_decode(text[i:])
    return obj
