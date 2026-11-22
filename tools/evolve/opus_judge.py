#!/usr/bin/env python3
"""判断引擎的兜底：本地模型连不上时，改用 Claude Code 订阅里的 Opus 5.5 打分。另外放本地模型的配置（local_*）。

Luke 2026-10-20 定的：本地模型（当时是 Qwen，2026-11-23 起是 Inkling 2 Mini）无法服务时，用当前 Claude Code 订阅的 Opus 5.5 打分、评估。
走命令行 `claude -p`（不带工具、不读 MCP、不留会话），一次调用固定开销约 6 千 token，所以按批打分。
Opus 给的是它自己说的概率，不是本地模型那种从 token 概率算出来的，两者不可混着比：每条结果都记下是谁打的分。
"""
import json, os, re, subprocess, urllib.request

MODEL = "claude-opus-5-5"


# 本地打分模型。地址和密钥仍是 .env 里的 QWEN_BASE_URL / QWEN_API_KEY（名字是历史留下的），
# 模型名写在 LOCAL_MODEL，没写就是 2026-11-22 以前用的 Qwen。Luke 2026-11-23 选了 A：换成 Inkling 2 Mini。
# 端口上挂的模型和 LOCAL_MODEL 对不上时不能打分（11-22 晚换模型后旧代码把每道题都记成了 0.5）
QWEN_MODEL = "qwen3.8-27b-coder390-mlx-mixed4-mtp"


def local_model():
    return os.environ.get("LOCAL_MODEL") or QWEN_MODEL


def local_name(model=None):
    """记进 scorer 的短名。不同模型的概率口径不同，成绩按它分开算。"""
    m = (model or local_model()).lower()
    return "inkling" if "inkling" in m else "qwen" if "qwen" in m else m


def local_ok(timeout=4):
    """本地模型能不能用：/models 能带 key 打开，而且挂的就是 LOCAL_MODEL。"""
    try:
        req = urllib.request.Request(os.environ["QWEN_BASE_URL"].rstrip("/") + "/models",
                                     headers={"Authorization": f"Bearer {os.environ.get('QWEN_API_KEY', '')}"})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            ids = [m.get("id") for m in json.load(r).get("data", [])]
            return r.status == 200 and local_model() in ids
    except Exception:
        return False


def ask_json(system, prompt, timeout=600):
    """调一次 Opus，返回它输出里的 JSON 对象。"""
    return ask_json_meta(system, prompt, timeout)[0]


def ask_json_meta(system, prompt, timeout=600):
    """同 ask_json，另外返回这次调用的花费和用时（claude -p 报的 total_cost_usd 是按 API 价折算的，订阅不另收钱）。"""
    r = subprocess.run(["claude", "-p", "--model", MODEL, "--system-prompt", system, "--tools", "",
                        "--strict-mcp-config", "--no-session-persistence", "--effort", "low", "--output-format", "json"],
                       input=prompt, capture_output=True, text=True, timeout=timeout, cwd="/tmp")
    if r.returncode != 0:
        raise RuntimeError(f"claude -p 失败：{(r.stderr or r.stdout)[-300:]}")
    d = json.loads(r.stdout)
    text = d.get("result", "")
    i = text.find("{")
    if i < 0:
        raise RuntimeError(f"Opus 没给 JSON：{text[:200]}")
    obj, _ = json.JSONDecoder().raw_decode(text[i:])   # 只取第一个 JSON 对象，后面多出来的字不管
    return obj, {"cost_usd": d.get("total_cost_usd"), "usage": d.get("usage"), "duration_ms": d.get("duration_ms")}
