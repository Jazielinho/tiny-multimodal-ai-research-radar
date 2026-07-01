# Mini GPT Implementation Contract

This contract keeps the Mini GPT implementation small, testable and reviewable.

## Current milestone

Task 01 only:

- tokenizer;
- data-loader;
- tests.

## Review rules

A change is reviewable when:

- it has a small scope;
- it can be tested locally;
- it does not mix unrelated features;
- it includes evidence in the commit or worklog.

## Do not mix these in one commit

Do not combine Task 01 with:

- model architecture;
- attention;
- training loop;
- generation;
- visualization;
- RAG;
- agent tools;
- public post polishing.

## Expected implementation order

1. `CharTokenizer`.
2. tokenizer tests.
3. `load_text`.
4. `train_val_split`.
5. `make_batch`.
6. data-loader tests.
7. run `pytest`.
8. run `ruff check .`.
9. update worklog.
10. commit and push.

## Suggested API

```python
class CharTokenizer:
    def __init__(self, text: str) -> None: ...
    @property
    def vocab_size(self) -> int: ...
    def encode(self, text: str) -> list[int]: ...
    def decode(self, ids: list[int]) -> str: ...
```

```python
def load_text(path: str) -> str: ...
def train_val_split(ids: list[int], train_ratio: float = 0.9) -> tuple[list[int], list[int]]: ...
def make_batch(ids: list[int], block_size: int, batch_size: int, seed: int | None = None): ...
```

## Expected evidence after Task 01

```text
pytest: OK
ruff check .: OK
Tokenizer: encode/decode reversible
Data-loader: x/y shifted correctly
```
