---
title: "从零搭建大模型的五阶段流程"
author: "Rahul (@sairahul1)"
url: https://x.com/sairahul1/status/2066076937806856661
source: X Article
published: 2026-06-14 08:35 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
roots: []
---

## 原文

# How To Build Your Own LLM from Scratch (The 5-Stage Pipeline Behind GPT and Claude)

![Image](https://pbs.twimg.com/media/HKweGDsa0AAk3KQ.jpg)

Everyone talks about LLMs.

Nobody explains how they actually work under the hood.

GPT. Claude. Gemini. Llama.

They all come from the same 5-stage pipeline.

And once you understand it, you can build one yourself.

Not a GPT-4 clone.

But a real working language model.

One that learns from text, generates new text, and actually makes sense.

I built one. Here's exactly how it works.

No PhD required. Code included.

The lie everyone believes about LLMs

Most people think building an LLM is about the architecture.

Transformers. Attention heads. Layers.

It is not.

The transformer architecture is publicly published. Every major lab uses roughly the same building blocks.

If architecture were the secret, everyone would have GPT-4.

The real secret: data, training, and alignment.

Architecture is one paragraph. Everything else is where real models are won and lost.

Here are the 5 stages.

## Stage 1 — Data (Where models are actually won)

![Image](https://pbs.twimg.com/media/HKweaA6bwAEf_kK.jpg)

Raw internet text is filthy.

You cannot train on it directly.

Common Crawl — the public web scrape used to train most LLMs — contains 250 billion pages and over a million gigabytes.

But most of it is garbage.

Duplicate headers. Spam. Toxic content. Personal data. Low-quality pages with 3 words.

Before any training happens, you run a brutal multi-step filter:

→ Extract clean text from raw HTML 

→ Filter harmful, NSFW, and personal data 

→ Deduplicate by URL, document, and line 

→ Remove low-quality docs by word count and token density 

→ Run model-based quality scoring — would a Wikipedia editor cite this page? 

→ Balance the data mix across code, books, science, and web

The result: a clean dataset that's a fraction of the original size but dramatically better.

The rule to burn in:

Data quality beats data quantity. Every time.

The most guarded secret in the field is not the architecture.

It's how the data was cleaned.

## Stage 2 — Tokenization (Break text into pieces the model can actually learn from)

![Image](https://pbs.twimg.com/media/HKwfo7aacAAyFSd.jpg)

The model never reads raw text.

It reads tokens.

A token is not always a full word. It is a piece of a word — a fragment the model learned to treat as a unit.

"playing" → ["play", "ing"] "unbelievable" → ["un", "believ", "able"] "dog" → ["dog"]

The standard method is called Byte-Pair Encoding (BPE).

It starts with individual characters and merges the most common pairs repeatedly until it has a fixed vocabulary — usually 32,000 to 100,000 tokens.

Here is a minimal tokenizer in Python:

Rule of thumb: 1 token ≈ 0.75 words.

1,000 tokens ≈ 750 words.

A 100k context window = roughly a full novel.

## Stage 3 — Training (One deceptively simple objective)

![Image](https://pbs.twimg.com/media/HKwgBktbkAAmzoE.jpg)

The entire training task sounds too simple to be powerful:

Predict the next token.

That is it.

Given "The cat sat on the", predict "mat".

Do this across trillions of examples and something remarkable happens.

The model learns grammar. Then facts. Then reasoning. Then how to write code, translate languages, solve math.

Nobody taught it any of that.

It emerged from next-token prediction at massive scale.

Here is a minimal decoder-only transformer in PyTorch — the same architecture behind every major LLM:

Now the training loop:

What the model is actually learning:

→ Every input token attends to every previous token 

→ The causal mask prevents looking into the future 

→ Loss = how surprised the model was by the real next token 

→ Lower loss = better predictions = model is learning language

## Stage 4 — Alignment (Turn a text predictor into an assistant)

![Image](https://pbs.twimg.com/media/HKwgz62bEAA7RsK.jpg)

After pretraining you have something impressive but useless for chat.

Ask it a question and it might reply with three more questions.

Because predicting the next token doesn't mean understanding what you want.

Two steps fix this.

Step 1: Supervised Fine-Tuning (SFT)

Show the model thousands of examples:

prompt → ideal response

The model learns to imitate the format of a good answer.

The surprising part: you need very little data.

A few thousand examples is enough because the knowledge is already inside the pretrained model.

SFT just teaches it to express that knowledge in the right format.

Step 2: RLHF (Reinforcement Learning from Human Feedback)

SFT teaches format. RLHF teaches preference.

The model generates two answers. A human picks the better one. Those preferences train a reward model. The LLM is optimized to maximize that reward.

This is why ChatGPT and Claude feel like assistants — not random text generators.

Without RLHF:

→ Fluent. Capable. But unreliable. 

→ Confidently wrong. 

→ Doesn't know when to say "I don't know."

With RLHF:

→ Helpful. Clear. Safe. 

→ Learns what "a good answer" actually means.

## Stage 5 — Evaluation (Prove it actually works)

![Image](https://pbs.twimg.com/media/HKwhflrbwAAPa80.jpg)

Building a model without measuring it is guessing.

During pretraining — measure perplexity.

Perplexity measures how "surprised" the model is by real text.

Lower perplexity = model predicts text better = it's learning.

Between 2017 and 2023, the best models dropped from perplexing among ~70 possible tokens to fewer than 10.

After alignment — perplexity stops working.

Fine-tuned models score worse on perplexity while being far more useful.

You need human benchmarks:

→ MMLU: 57 academic subjects, multiple choice — measures knowledge 

→ Chatbot Arena: humans blind-compare two models and vote — measures preference 

→ AlpacaEval: LLM judges LLM — 98% correlation with human judges, costs $10

The honest truth: no single score captures a good model.

The same model scores 0.637 or 0.488 on the same benchmark depending only on how the prompt is formatted.

Evaluation is genuinely hard.

And no one has fully solved it.

## How to generate text from your model

![Image](https://pbs.twimg.com/media/HKwiLJEbAAAqsLO.jpg)

The model is trained.

Now make it generate something.

Temperature controls creativity:

→ temperature = 0.1 → safe, predictable, repetitive 

→ temperature = 0.8 → natural, varied, good default 

→ temperature = 1.5 → creative, surprising, sometimes incoherent

## What the full pipeline looks like

![Image](https://pbs.twimg.com/media/HKwi9ABagAAQANk.jpg)

Before: raw internet text, 1 million GB, completely unusable. 

After Stage 1: clean filtered dataset, ready to train on.

Before: raw text, meaningless to a model. 

After Stage 2: tokens with IDs, the model's native language.

Before: random weights, outputs garbage. 

After Stage 3: a model that understands language patterns.

Before: a text predictor that answers questions with more questions. 

After Stage 4: an assistant that follows instructions and is safe.

Before: no idea if the model is actually good. 

After Stage 5: benchmarks, perplexity scores, human evaluations.

Each stage builds on the last.

Skip any one and the whole thing breaks.

## The 5 mistakes that sink LLM projects

1. Obsessing over architecture.

Transformers are standardized. Published. Copied.

The architecture is the least important part.

2. Treating data as a commodity.

Dirty data caps your ceiling regardless of compute.

The top labs spend more on data cleaning than model design.

3. Skipping the scaling math.

A model too big for its data is undertrained and wastes compute.

Optimal ratio: ~20 tokens of training data per parameter.

4. Stopping at SFT.

A fine-tuned model imitates. Without RLHF it never learns what people actually prefer.

5. Trusting perplexity after alignment.

Post-training changes the distribution.

Perplexity stops being meaningful the moment you run SFT.

Switch to human benchmarks immediately.

## The uncomfortable truth

A great LLM is not trained.

It is engineered.

5 stages. Not 1.

Architecture is one paragraph inside Stage 3.

Everything that matters is in the other four.

Data quality. Scaling math. Alignment. Honest evaluation.

That's what separates GPT-4 from a hobby model.

Two labs with identical architecture produce wildly different models.

The architecture is shared.

Everything that actually matters is not.

Start here

Want to run this yourself? Here is the minimal setup:

Start small. 15M parameters. WikiText dataset. Free GPU on Google Colab.

Watch the perplexity drop from 800 to 50 over a few hours.

That drop is the model learning language.

In real time.

That's the moment everything clicks.

## Now make it useful: build a real niche LLM

![Image](https://pbs.twimg.com/media/HKwlBG7bUAAILY-.jpg)

WikiText is a learning dataset.

The real money — and the real fun — is training on a specific domain and watching your model become an expert in exactly one thing.

Here are 5 niches you can build right now. Same pipeline. Different data.

## Niche 1 — Coding Assistant LLM (The main example: highest impact, most dramatic results)

This is the one to build first.

The pain is universal. Every developer has hit this:

→ You stare at a function that isn't working. 

→ Stack Overflow has 12 answers, all from 2014. 

→ You paste into ChatGPT and get something almost right.

A coding LLM trained on the right data does this natively, offline, and tuned to your exact stack.

The data:

What the training pairs look like:

The before/after that sells this:

Before training:

> Prompt: "Write a Python decorator that retries a function on failure"
Output: "A decorator is a design pattern in Python that allows..."
# Generic. Useless. Textbook answer.

After 10 hours of training on GitHub + Stack Overflow:

Prompt: "Write a Python decorator that retries a function on failure"
Output:


The model learned what a senior developer would write.

Not from being told. From reading 6 million Python files and every accepted Stack Overflow answer.

![Image](https://pbs.twimg.com/media/HKwjhhBbkAAsjhh.jpg)

## Niche 2 — SQL Query Generator

The pain: every non-technical founder has data they cannot access.

The data is there. In their database. They just cannot write the query.

They describe what they want in plain English. Your model writes the SQL.

The data:

The before/after:

Who pays for this: every SaaS founder, every e-commerce operator, every analyst who sits between a business owner and a database.

They will pay $20/month without thinking.

## Niche 3 — US Legal Document Summarizer

The pain: a 40-page contract. A lease agreement. An NDA.

Most people sign without understanding it.

A lawyer charges $300/hour to read it.

Your model reads it in 3 seconds.

The data:

The output format that makes this worth paying for:

Who pays for this: freelancers reviewing client contracts, small business owners, renters reviewing leases, startup founders signing their first SaaS agreements.

The market is everyone who cannot afford a lawyer but still has to sign things.

## Niche 4 — Medical Symptom Explainer

The pain: you Google a symptom and WebMD tells you that you have 3 days to live.

A medical LLM trained on clinical notes and patient education materials does something different.

It explains what the symptom actually means. In plain English. Without catastrophizing.

The key: every response ends with a clear disclaimer and escalation signal.

That is what separates useful health information from dangerous advice.

## Niche 5 — E-commerce Product Description Writer

The pain: a Shopify store with 500 products. Every description is a wall of spec sheet text nobody reads.

Good product descriptions do one thing: make someone feel something.

An LLM trained on high-converting product copy learns exactly what words drive clicks.

The data source: scrape the top 1,000 Shopify stores by traffic. Extract product titles, specs, and descriptions. Filter for products with high review counts — those descriptions are proven to convert. Train on those.

Your model learns the difference between spec sheets and copy that sells.

The pattern across all 5 niches

Look at what they share:

→ A clear, specific pain the user feels every day 

→ A data source that already exists and is publicly available 

→ A before/after that is immediately obvious to anyone in that profession 

→ A willingness to pay because the alternative costs more time or money

The 5-stage pipeline is identical for every single one.

You change only one thing: the training data.

Same tokenizer setup. Same transformer architecture. Same training loop. Same evaluation method.

Different data → different expert → different product.

That is the leverage.

One pipeline. Five products. Five revenue streams.

If this was useful:

→ Repost to share it with every developer learning AI 

→ Follow @sairahul1 for more breakdowns like this 

→ Bookmark this — the code works, run it tonight

I write about AI, building products, and systems that work while you sleep.

## 溯源

