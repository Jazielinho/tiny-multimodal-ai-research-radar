# Mini GPT Worklog

Use this file to record small implementation checkpoints.

## 2026-07-01 — Setup

Created planning artifacts for Week 1.5:

- `docs/experiments/mini-gpt-plan.md`
- `docs/experiments/mini-gpt-task-01-tokenizer-dataloader.md`
- `docs/experiments/mini-gpt-reading-notes.md`
- `docs/experiments/mini-gpt-implementation-contract.md`
- `tests/fixtures/mini_gpt_corpus.txt`
- `src/research_radar/mini_gpt/__init__.py`

Setup commits:

- `4cfbf29` — Add Mini GPT experiment plan
- `eab0090` — Add Mini GPT tokenizer and dataloader task
- `bdbae47` — Add Mini GPT sample corpus fixture
- `86e26d7` — Add Mini GPT package skeleton
- `8dedda7` — Add Mini GPT reading notes template
- `2186821` — Add Mini GPT implementation contract
- `6d286aa` — Update Mini GPT worklog with setup commits

Next human task:

Implement Task 01: tokenizer and data-loader baseline.

## 2026-07-02 — Task 01 tokenizer and data-loader

### What changed

- Added `CharTokenizer` for character-level tokenization.
- Added tokenizer tests for roundtrip encoding, vocabulary size and integer IDs.
- Added `load_text` for UTF-8 text loading.
- Added `train_val_split` for deterministic train/validation splits.
- Added `make_batch` for next-token prediction batches.
- Added data-loader tests for fixture loading, split behavior, batch shapes, shifted targets, deterministic seeds and short datasets.

### Commands run

```bash
.\.venv\Scripts\python.exe -m pytest
.\.venv\Scripts\python.exe -m ruff check .
```

### Result

- `pytest`: 13 passed.
- `ruff check .`: All checks passed.

### Next step

Start the next Mini GPT task only after defining its scope. Do not add embeddings, attention or a training loop to Task 01.

## 2026-07-09 — Task 02 bigram baseline

### What changed

- Added `BigramLanguageModel` as the first minimal trainable Mini GPT baseline.
- Added a learnable lookup table that maps token IDs to next-token logits.
- Added optional cross-entropy loss when targets are provided.
- Added model tests for logits shape, scalar loss and invalid vocabulary size.

### Commands run

```bash
.\.venv\Scripts\python.exe -m pytest
.\.venv\Scripts\python.exe -m ruff check .
```

### Result

- `pytest`: 16 passed.
- `ruff check .`: All checks passed.

### Evidence

- `src/research_radar/mini_gpt/model.py`
- `tests/test_mini_gpt_model.py`

### Decision

- Keep Task 02 limited to the bigram baseline, logits and loss.
- Do not add attention, positional embeddings, generation or a training loop in this task.

### Next step

Define the next Mini GPT task before implementing causal attention or GPT-style embeddings.

## 2026-07-23 — Task 03 bigram training smoke test

### What changed

- Added `train_step` for one CPU optimization step.
- Added a check that the model returns a loss before backpropagation.
- Added tests for finite loss and model parameter updates.

### Commands run

```bash
.\.venv\Scripts\python.exe -m pytest
.\.venv\Scripts\python.exe -m ruff check .
```

### Result

- `pytest`: 18 passed.
- `ruff check .`: All checks passed.

### Evidence

- `src/research_radar/mini_gpt/training.py`
- `tests/test_mini_gpt_training.py`
- `docs/experiments/mini-gpt-task-03-bigram-training-smoke-test.md`

### Decision

- Keep Task 03 limited to one optimization step.
- Do not add a longer training loop, generation, positional embeddings, attention or transformer blocks.

### Next step

Prepare a clean Task 03 commit, then define the next Mini GPT task before implementing it.

## Template

### Date

YYYY-MM-DD

### What changed

-

### Commands run

```bash
pytest
ruff check .
```

### Result

-

### Next step

-
