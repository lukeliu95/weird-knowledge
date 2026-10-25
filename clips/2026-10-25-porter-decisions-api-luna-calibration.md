---
title: Jev 的厂商实测 GPT-6 Luna（OpenAI Decisions API 背后的模型）：说 99% 确定时只对 68%，推理五步后像抛硬币；决策模型要紧的是置信度可信
author: Ryan Alyn Porter (@RyanAlynPorter)，anth.us（Jev 的开发方）
url: https://anth.us/blog/openai-decisions-api-preview/
source: 网页
published: 2026-10-01
saved: 2026-10-25
why: 探索日报：Luke 想看
related_principles: [原则 1, 原则 12]
status: 未整理
kind: 观点
topic: 模型与本地部署
roots: []
---

## 原文

October 1, 2026[#articles](https://anth.us/tags/articles/)[#AI](https://anth.us/tags/ai/)[#explainer](https://anth.us/tags/explainer/)

# The OpenAI Decisions API Needs a Confidence You Can Trust

We've routed decisions on LLM confidence since 2023, and calibration is what we most hope OpenAI's new Decisions API gets right. The model underneath, GPT-6 Luna, isn't there yet: on 3,600 reasoning problems its 99% meant 68%, and by five inference steps it was at a coin flip.

Say you send an agent's next step to a decision model, and you only let it act on its own when it's at least 99% sure. Everything else goes to a person. That rule is only as good as the 99%. We gave GPT-6 Luna, the model behind OpenAI's new Decisions API, 3,600 reasoning problems and asked for exactly that kind of answer. When Luna said it was 99% sure or more, it was right 68% of the time.

OpenAI announced the Decisions API at DevDay on September 29, in limited preview. It picks one answer from a list you define, so software can branch on it: classify a message, route a request, choose what an agent does next. [The Decoder](https://the-decoder.com/openai-expands-codex-and-its-api-at-devday-with-security-scans-a-decisions-api-and-ultrafast/) and [Axios](https://www.axios.com/2026/09/29/openai-dev-day-2026-dots-space-sol) report it runs on "a version of GPT-6 Luna," OpenAI's low-cost model, and OpenAI's own chart puts it at 150 milliseconds a decision. It's OpenAI's answer to [Jev](https://anth.us/articles/making-decisions-instead-of-generating-text/).

We'd already run Luna that way. In [Hard-Decisions](https://hard-decisions.anth.us/), our benchmark of decision models on multi-step logic, Luna answered the same problems as Jev, Kev and Laya, one request each, from a fixed list of options. That makes it a preview of a Luna-based decision model. It isn't the Decisions API itself: OpenAI uses a specialized version of Luna, and there's no documentation yet to test against.

## Why we care

We've been routing on a model's confidence since 2023. For [Call Criteria](https://anth.us/articles/call-criteria/), LLMs score calls against hundreds of client scorecards, and people review the calls the system is unsure about. Everything depends on knowing which calls those are. When we read that confidence from the token log-probabilities of OpenAI's models, [the numbers were so concentrated](https://anth.us/articles/making-decisions-instead-of-generating-text/) that they looked certain about nearly every answer. OpenAI's models have had confidence problems for as long as we've used them, and not the shy kind. Newer reasoning models often don't expose log-probabilities at all. So we built the confidence ourselves: extract the probability behind each label, check it against labeled answers, calibrate it, and only then route on it. [Classification with Confidence](https://anth.us/articles/classification-with-confidence/) shows that pipeline on GPT-4o-mini.

That's the pain the Decisions API could end. What we're hoping for most is that OpenAI now treats calibration as a product: a confidence you can set a threshold on, documented and tested, instead of something withheld from the API, which we suspect, without proof, is partly about making the models harder to distill. A decision endpoint is where that would have to happen. So we wanted to know what the model underneath does today.

![Line chart of accuracy by proof depth from 0 to 5 on 3,600 problems. Jev starts near 99% and is still at 85% at depth 5. GPT-6 Luna starts near 96%, drops to 77% at depth 1 and 63% at depth 2, and ends at 45% at depth 5.](https://anth.us/assets/responsive/images/openai-decisions-api-preview-accuracy-by-depth-1600.jpg)

Accuracy by the number of inference steps the answer needs, both ProofWriter tasks pooled.

## The test

The problems come from ProofWriter, a dataset from the Allen Institute for AI. Each one is a short list of facts and if-then rules in plain English, and a statement to judge. Some answers can be read straight off the page. Others need five rules chained together. The dataset labels every problem with that number, its proof depth, which makes difficulty something you can measure instead of argue about.

There are two versions of the task. In the open-world one the answer is true, false or unknown: unknown when the rules settle neither the statement nor its opposite. In the closed-world one, anything you can't prove is false. We sampled 1,800 problems for each, about 300 at every depth, and recomputed every gold answer with an independent solver.

Luna got the same treatment as everyone else. One request per problem. The problem, the question and the meaning of each option, word for word what Jev receives. A strict JSON schema that only allows the three options. Reasoning off, which is the setting a fast decision API implies.

## Accuracy: fine on the page, coin flips five steps in

On problems you can answer by reading, Luna is nearly as good as Jev: 93% against 98% on the open-world task, and 98% against 99% on the closed one. Then it loses ground with every step. By five chained inferences Luna gets 46% and 45% right. On the closed-world task, that's a coin flip. Jev gets 81% and 89% at the same depth, on the same problems.

Across all depths, Jev scored 83.8% and 89.3%; Luna, 64.1% and 65.0%. The gap at depth 5 is 35 and 45 points, with 95% intervals from 27 to 43 and from 38 to 51. That isn't a close call.

You might be thinking that reasoning off is what sank Luna. Turning it on might help, but it would also make every decision slower and costlier than the one-shot job a decision API exists to do, and every model here got the same single shot. The open models we tested are stuck at depth 5 too: [every model except Jev](https://hard-decisions.anth.us/breakdowns/proof-depth/) was at coin-flip accuracy by depth 5.

## Wrong when the answer is on the page

Most of Luna's misses come from long chains, but not all of them. At depth 0, where the statement or its opposite is written in the text, Luna got 20 of 300 open-world problems wrong and 6 of 300 closed-world ones. At depth 1, one rule away, it missed 67 of 302 and 70 of 300. Here are the shortest of those misses at each depth, in each version of the task, with the confidence Luna gave when we asked again for log-probabilities and it gave the same answer:

-   **Depth 0, open world.** The text says "The lion is not big." Is "The lion is big" true, false or unknown? It's false; the text says so. Luna said **unknown, 100% sure**.
-   **Depth 0, closed world.** The text says "Charlie is nice." Is "Charlie is not nice" true or false? False. Luna said **true, 100% sure**.
-   **Depth 1, open world.** "The tiger is big. All big people are cold." Is "The tiger is cold" true? Yes, one rule away. Luna said **unknown, 100% sure**.
-   **Depth 1, closed world.** "The rabbit is big. If someone is big then they chase the rabbit." Is "The rabbit does not chase the rabbit" true or false? False: the rabbit is big, so it chases the rabbit. Luna said **true, 100% sure**.

They're the clearest of Luna's misses; at depth 0 it's right 93% and 98% of the time. But a decision model that can be 100% sure Charlie is not nice, when the text says Charlie is nice, needs more than a threshold on its confidence.

## Can Luna tell you how sure it is?

A decision model earns its keep when you can trust its confidence. Jev returns a probability for every option. Luna, through the regular API, returns text. But with reasoning off, OpenAI's API will also return log-probabilities: for each token Luna writes, the log of the probability it gave that token, plus the most likely alternatives. With reasoning on, it refuses: "'logprobs' is not supported with this model," which matches [OpenAI's guide](https://developers.openai.com/api/docs/guides/latest-model).

The strict schema makes the reading clean. It only lets Luna reply `{"answer":"<option>"}`, so the token that spells the option carries the whole decision, with no "No" versus "no" to reconcile. Turn its log-probability into a probability and you have Luna's confidence in the answer it gave.

Here's one real exchange. The request, minus the long prompt:

```json
{
  "model": "gpt-6-luna",
  "reasoning_effort": "none",
  "max_completion_tokens": 1024,
  "response_format": {
    "type": "json_schema",
    "json_schema": {
      "name": "decision",
      "strict": true,
      "schema": {
        "type": "object",
        "properties": { "answer": { "type": "string", "enum": ["true", "false", "unknown"] } },
        "required": ["answer"],
        "additionalProperties": false
      }
    }
  },
  "logprobs": true,
  "top_logprobs": 5
}
```

The problem, in its paraphrased form:

> Alan is young, round, and kind, but that doesn't mean he isn't also rough and cold at times, as well. … Young round people who are green are usually blue. … Kind people with rough skin are usually red because it's wind burn. If someone shows that they are red, then they are also showing that they are green. …
>
> Statement: Alan is not blue.

And Luna's answer, with its log-probabilities:

```json
"content": "{\"answer\":\"unknown\"}",
"logprobs": { "content": [
  { "token": "{\"",     "logprob": 0.0,      "top_logprobs": [ { "token": "{\"",     "logprob": 0.0 } ] },
  { "token": "answer",  "logprob": 0.0,      "top_logprobs": [ { "token": "answer",  "logprob": 0.0 } ] },
  { "token": "\":\"",   "logprob": 0.0,      "top_logprobs": [ { "token": "\":\"",   "logprob": 0.0 } ] },
  { "token": "unknown", "logprob": -0.00182, "top_logprobs": [ { "token": "unknown", "logprob": -0.0018 } ] },
  { "token": "\"}",     "logprob": 0.0,      "top_logprobs": [ { "token": "\"}",     "logprob": 0.0 } ] }
]}
```

A log-probability of −0.00182 is a probability of 99.82%. We asked for five alternatives and got none: Luna put essentially nothing on "true" or "false". And it's wrong. Alan is kind with rough skin, so he's red; red means green; young, round and green means blue. "Alan is not blue" is false, three steps in.

## When Luna says 99%

One example proves nothing, so we asked for log-probabilities on all 3,600 problems with exactly the benchmark's request. It cost about 14 cents, and every request and response is [kept verbatim](https://hard-decisions.anth.us/openai-decisions-api-preview/).

![Reliability chart of stated probability against actual accuracy. Jev's line climbs close to the diagonal and reaches 98.9% accuracy among 1,667 answers stated at 99% or more. GPT-6 Luna's line stays near 50% for every band up to 97% and reaches only 68% among 2,672 answers stated at 99% or more.](https://anth.us/assets/responsive/images/openai-decisions-api-preview-reliability-1600.jpg)

Each point is a band of stated probability; the dashed diagonal is where a perfectly calibrated model would sit. Both tasks pooled.

Luna stated 99% or more on 2,672 of the 3,600 answers, and 68% of those were right. Below that it's flat: whether Luna says 70%, 90% or 97%, it's right about half the time. Jev stated 99% or more on 1,667 answers and got 98.9% of them right. Its line runs close to the diagonal the whole way.

The other numbers say the same thing:

-   **Wrong answers stated at 95% or more:** 78% of Luna's, against 7% and 17% of Jev's on the two tasks.
-   **Expected calibration error**, the average gap between stated and actual: 0.32 for Luna on both tasks; 0.04 and 0.03 for Jev.
-   **Separating right from wrong** (AUROC, where 0.5 means the probability tells you nothing): 0.66 and 0.68 for Luna; 0.85 and 0.86 for Jev.

## Past a few steps, the confidence carries no information

Overconfidence on its own is fixable. If a model's 99% always means 68%, you can relabel it, the same way [Jev's confidence calibrates](https://anth.us/articles/can-you-trust-jev-confidence/). What calibration can't fix is a probability that doesn't move with being right.

![Line chart of AUROC by proof depth. Jev stays between 0.76 and 0.97 at every depth and ends at 0.84. GPT-6 Luna falls from 0.88 at depth 0 to 0.72, 0.63, 0.56 and 0.54, and ends at 0.51 at depth 5, on the coin-flip line.](https://anth.us/assets/responsive/images/openai-decisions-api-preview-auroc-by-depth-1600.jpg)

How well each model's stated probability separates its right answers from its wrong ones, by proof depth. 0.5 is no information at all.

On problems you can read off the page, Luna's probability is informative: right answers get higher numbers than wrong ones. Each inference step erodes that, and by five steps the AUROC is 0.51: a high stated probability is no more likely to be right than a low one. Remapping the numbers can't add information they don't carry, so on hard problems a threshold on Luna's confidence routes at random. Jev's still sorts right from wrong at 0.84.

## Hidden, or just overconfident?

We'd assumed OpenAI hides Luna's log-probabilities. With reasoning off, it mostly doesn't. The alternatives it returns cover 99.8% of the probability on average; the ones it leaves out carry almost nothing. The problem in these results is overconfidence, not secrecy.

That fits what OpenAI itself reported for GPT-4: the pre-trained model's probabilities were well calibrated, and post-training made them markedly worse ([GPT-4 Technical Report](https://arxiv.org/abs/2303.08774), figure 8). It also fits our experience with OpenAI models generally. Where they expose log-probabilities, they've been too sure of themselves to calibrate into a confidence you'd route on.

Why does the API refuse log-probabilities once reasoning is on? We don't know. Researchers have recovered part of a production OpenAI model from its API's log-probabilities and logit bias, and OpenAI changed its API in response ([Carlini et al., 2024](https://arxiv.org/abs/2403.06634); see also [Finlayson et al., 2024](https://arxiv.org/abs/2403.09539)). OpenAI has also kept o1's raw reasoning private, partly for competitive advantage ([OpenAI](https://openai.com/index/learning-to-reason-with-llms/)). Protecting the model from distillation is a plausible reason. We have no evidence that it's the reason.

## What this means for the Decisions API

We'll admit these results worry us. We want the Decisions API to be good: we've waited years for a hosted model whose confidence we could route on. But the model it's built on lost to Jev by 35 to 45 points at five inference steps, and its 99% meant 68%. A specialized version has a lot of ground to make up, on accuracy as much as on confidence.

Some coverage says the Decisions API returns a confidence score. OpenAI hasn't published documentation, so we can't say. If it does, these results tell you what to check before you route on it:

-   **Test it at the difficulty you'll run it at.** Easy problems flatter everyone. Luna and Jev are within a few points at depth 0.
-   **Check calibration against labeled answers before you set a threshold.** A 99% that means 68% will push the wrong decisions past your reviewers.
-   **Check that the confidence separates right from wrong on your hardest cases.** If it doesn't, no calibration will rescue it.
-   **Ask twice.** Asked every question a second time, Luna gave a different answer on 10% of them; Jev changed on 2 to 3%, and Kev-0.8B, Kev-4B and Laya on none. Part of that is sampling: 137 of Luna's replies weren't even its own most probable answer, because OpenAI samples at its default temperature.

A specialized Luna may do better than the general one. When the Decisions API opens up, we'll put it through the same 3,600 problems and the same probe.

## How we measured

Every model answered the same 3,600 problems once, with the same wording and no examples. The Luna probe sits outside the scored benchmark. Luna ran with reasoning off at OpenAI's default sampling. ProofWriter is synthetic, templated logic, so these numbers describe multi-step reasoning of that kind; other tasks deserve their own test. The full results and every record are on [hard-decisions.anth.us](https://hard-decisions.anth.us/).

If you're choosing between the Decisions API, Jev and an open model, run the same kind of test on your own decisions before you trust any of them: labeled cases from your own work, hard ones included, every model asked the same way, accuracy by difficulty, and a check that each model's confidence separates its right answers from its wrong ones. ProofWriter shows how these models handle chained logic; your own cases show how they'll handle your decisions. [That's work we do with teams](https://anth.us/ai-solutions/).

## 溯源

（整理时填写，存的时候留空）
