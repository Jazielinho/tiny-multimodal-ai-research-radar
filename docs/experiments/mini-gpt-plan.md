# Mini GPT Experiment Plan

## Purpose

Build a tiny GPT-like language model to understand the mechanics behind modern LLMs.

This experiment is not meant to produce a useful production model. It is meant to make the core ideas concrete:

- text as tokens;
- token IDs as model inputs;
- embeddings and positional embeddings;
- causal self-attention;
- next-token prediction;
- training loss;
- basic generation;
- limitations of small models.

## Why this experiment exists

The project goal is to become stronger as an applied AI engineer, not only as a user of APIs.

Before building RAG, agents and multimodal workflows, this experiment creates a small controlled lab where the basic language-modeling pipeline can be inspected end to end.

The expected professional value is the ability to explain, in an interview or technical post:

1. what a language model predicts;
2. why tokenization matters;
3. how inputs and targets are created;
4. why causal masking is needed;
5. what training loss measures;
6. why a tiny model is useful for learning but not for production.

## Design principles

This plan follows a few practical AI/ML engineering principles:

- start with a simple, trustworthy pipeline;
- test data preparation before modeling;
- make the objective observable;
- create a baseline before adding complexity;
- keep the experiment reproducible;
- document what works, what fails and what is intentionally out of scope.

## Scope

### In scope

- small local text corpus;
- character-level tokenizer as the first baseline;
- deterministic train/validation split;
- input-target sequence creation;
- small GPT-like model later;
- local training later;
- loss logging;
- simple generation;
- tests for tokenizer/data-loader;
- clear technical explanation.

### Out of scope

- large-scale training;
- fine-tuning a pretrained LLM;
- RLHF;
- reasoning model;
- RAG;
- agents;
- multimodal models;
- GPU optimization;
- distributed training;
- production serving.

## Dataset strategy

### Phase A — self-contained corpus

Use a tiny in-repository fixture first:

```text
tests/fixtures/mini_gpt_corpus.txt
```

Why:

- no download required;
- deterministic tests;
- easy debugging;
- enough to validate tokenizer and data-loader behavior.

This is not for meaningful generation quality. It is only for pipeline validation.

### Phase B — classic tiny corpus

After the pipeline works, optionally test with a classic tiny corpus such as Tiny Shakespeare or another small public-domain text.

Why:

- larger than the fixture;
- common baseline for character-level language modeling;
- useful for showing loss decrease and crude generation.

### Phase C — project-aligned corpus

Later, optionally use AI paper titles, abstracts or project documentation.

Why:

- closer to the Research Radar theme;
- useful for a more project-specific demo;
- only worth doing after the base pipeline is stable.

## Tokenizer baseline

Start with a character-level tokenizer.

### Requirements

The tokenizer should:

- build a vocabulary from input text;
- map each character to an integer ID;
- map each integer ID back to a character;
- support `encode(text) -> list[int]`;
- support `decode(ids) -> str`;
- be deterministic;
- preserve enough information so that `decode(encode(text)) == text` for known characters.

### Why character-level first

A character-level tokenizer is simple and transparent. It avoids adding BPE, SentencePiece, Hugging Face tokenizers or other complexity before the learning objective is clear.

A better tokenizer can be added later, but only after the full pipeline works.

## Data-loader baseline

The first data-loader should create batches for next-token prediction.

Given a sequence of token IDs:

```text
[t0, t1, t2, t3, t4, ...]
```

For a block size of `4`, one training example should look like:

```text
x = [t0, t1, t2, t3]
y = [t1, t2, t3, t4]
```

The model will learn to predict the next token at every position.

### Requirements

The data-loader should:

- accept raw text or token IDs;
- split data into train/validation sets;
- create `(x, y)` batches;
- ensure `x.shape == y.shape`;
- ensure `y` is `x` shifted by one token;
- be deterministic when a seed is provided;
- support small batch sizes for local debugging.

## Initial implementation files

Expected package:

```text
src/research_radar/mini_gpt/
  __init__.py
  tokenizer.py
  data.py
```

Expected tests:

```text
tests/test_mini_gpt_tokenizer.py
tests/test_mini_gpt_data.py
```

Expected fixture:

```text
tests/fixtures/mini_gpt_corpus.txt
```

## Minimum success criteria

The Mini GPT preparation phase is valid if:

- the corpus can be loaded;
- tokenizer can encode/decode text;
- train/validation split is deterministic;
- a batch can be created;
- `x` and `y` have the expected shape;
- `y` is shifted by one token;
- tests pass;
- the limitations are documented.

## Evidence to generate

- `docs/experiments/mini-gpt-plan.md`;
- `docs/experiments/mini-gpt-task-01-tokenizer-dataloader.md`;
- tokenizer/data-loader implementation;
- tests passing;
- short notes in `docs/weekly-reviews/week-01.md` or the next weekly review.

## First coding task

Implement Task 01:

```text
docs/experiments/mini-gpt-task-01-tokenizer-dataloader.md
```

Do not implement attention, transformer blocks or training loop before Task 01 passes.

## Reading focus

Read only to unblock implementation.

Recommended reading now:

- Build a Large Language Model From Scratch — chapter 2, tokenization and data preparation;
- AI Engineering — chapter 1, foundation models and language modeling concepts;
- Designing Machine Learning Systems — chapter 2, objectives and requirements.

Reading output must be applied to the repo. A useful reading note should produce one of:

- a design decision;
- a test;
- a clearer implementation plan;
- an explicit limitation.

## References that influenced this plan

- Google Rules of Machine Learning: https://developers.google.com/machine-learning/guides/rules-of-ml
- Full Stack Deep Learning course: https://fullstackdeeplearning.com/course/2022/
- DeepLearning.AI Machine Learning in Production: https://www.deeplearning.ai/courses/machine-learning-in-production
- Hugging Face LLM/NLP course: https://huggingface.co/learn/llm-course/chapter1/1
