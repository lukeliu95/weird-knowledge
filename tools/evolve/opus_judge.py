#!/usr/bin/env python3
"""判断引擎的兜底：本地 Qwen 连不上时，改用 Claude Code 订阅里的 Opus 5.5 打分。

Luke 2026-10-20 定的：本地 Qwen 无法服务时，用当前 Claude Code 订阅的 Opus 5.5 打分、评估。
走命令行 `claude -p`（不带工具、不读 MCP、不留会话），一次调用固定开销约 6 千 token，所以按批打分。
Opus 给的是它自己说的概率，不是 Qwen 那种从 token 概率算出来的，两者不可混着比：每条结果都记下是谁打的分。
"""
import json, os, re, subprocess, urllib.request

MODEL = "claude-opus-5-5"


def qwen_ok(timeout=4):
    """本地 Qwen 服务能不能用：看 /models 能不能带 key 打开。"""
    try:
        req = urllib.request.Request(os.environ["QWEN_BASE_URL"].rstrip("/") + "/models",
                                     headers={"Authorization": f"Bearer {os.environ.get('QWEN_API_KEY', '')}"})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status == 200
    except Exception:
        return False


def ask_json(system, prompt, timeout=600):
    """调一次 Opus，返回它输出里的 JSON 对象。"""
    r = subprocess.run(["claude", "-p", "--model", MODEL, "--system-prompt", system, "--tools", "",
                        "--strict-mcp-config", "--no-session-persistence", "--effort", "low", "--output-format", "json"],
                       input=prompt, capture_output=True, text=True, timeout=timeout, cwd="/tmp")
    if r.returncode != 0:
        raise RuntimeError(f"claude -p 失败：{(r.stderr or r.stdout)[-300:]}")
    text = json.loads(r.stdout).get("result", "")
    m = re.search(r"\{.*\}", text, re.S)
    if not m:
        raise RuntimeError(f"Opus 没给 JSON：{text[:200]}")
    return json.loads(m.group(0))
