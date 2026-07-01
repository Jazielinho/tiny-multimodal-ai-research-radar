# Mini GPT Task 01 — Tokenizer and Data Loader

## Goal

Implement the first technical building block for the Mini GPT experiment:

1. a simple character-level tokenizer;
2. a deterministic data-loader for next-token prediction;
3. tests that prove both pieces work.

This task deliberately avoids model architecture, attention and training.

## Why this task matters

A language model is only as good as the data pipeline that feeds it.

Before implementing embeddings, attention or a training loop, we need to prove that:

- text is converted into token IDs correctly;
- token IDs can be decoded back into text;
- inputs and targets are created correctly;
- the target sequence is shifted by one token;
- the batch shapes are predictable;
- tests catch mistakes early.

## Files to create

Create these files:

```text
src/research_radar/mini_gpt/tokenizer.py
src/research_radar/mini_gpt/data.py
tests/test_mini_gpt_tokenizer.py
tests/test_mini_gpt_data.py
```

The package folder already exists:

```text
src/research_radar/mini_gpt/
```

The fixture corpus already exists:

```text
tests/fixtures/mini_gpt_corpus.txt
```

## Implementation contract

### tokenizer.py

Implement a small class or functions that support:

```python
encode(text: str) -> list[int]
decode(ids: list[int]) -> str
```

Recommended simple class:

```python
class CharTokenizer:
    def __init__(self, text: str) -> None:
        ...

    @property
    def vocab_size(self) -> int:
        ...

    def encode(self, text: str) -> list[int]:
        ...

    def decode(self, ids: list[int]) -> str:
        ...
```

### data.py

Implement functions that support:

```python
load_text(path: str) -> str
train_val_split(ids: list[int], train_ratio: float = 0.9) -> tuple[list[int], list[int]]
make_batch(ids: list[int], block_size: int, batch_size: int, seed: int | None = None)
```

The first version may return Python lists or NumPy arrays. PyTorch tensors are also acceptable if you keep the implementation simple.

Minimum behavior:

- `x` and `y` must have the same shape;
- `y` must be `x` shifted by one token;
- `block_size` controls sequence length;
- `batch_size` controls number of sequences;
- the function should fail clearly if the dataset is too short.

## Tests to write

### tests/test_mini_gpt_tokenizer.py

Required tests:

1. `decode(encode(text)) == text` for known text.
2. `vocab_size` equals the number of unique characters.
3. Encoding returns integers.

### tests/test_mini_gpt_data.py

Required tests:

1. fixture corpus loads successfully;
2. train/validation split is deterministic;
3. batch creation returns matching shapes;
4. `y` is shifted one token ahead of `x`.

## Commands

Run:

```bash
.\.venv\Scripts\python.exe -m pytest
.\.venv\Scripts\python.exe -m ruff check .
```

If you use PowerShell and the environment is activated, this is also fine:

```bash
pytest
ruff check .
```

## Completion checklist

This task is complete when:

- [ ] `tokenizer.py` exists;
- [ ] `data.py` exists;
- [ ] tokenizer tests pass;
- [ ] data-loader tests pass;
- [ ] full `pytest` passes;
- [ ] `ruff check .` passes;
- [ ] commit is pushed to GitHub;
- [ ] Issue #2 is updated with the commit.

## What not to do in this task

Do not implement:

- embeddings;
- attention;
- transformer block;
- training loop;
- generation;
- GPU support;
- RAG;
- agents;
- multimodal logic.

Those come later.

## Suggested commit message

```bash
git add src/research_radar/mini_gpt tests/test_mini_gpt_*.py
git commit -m "Add Mini GPT tokenizer and dataloader baseline"
git push
```

## How to ask for review

After pushing, send:

```text
Task 01 done.
Commit: <sha>
pytest: OK/fail
ruff: OK/fail
Main doubt:
```
