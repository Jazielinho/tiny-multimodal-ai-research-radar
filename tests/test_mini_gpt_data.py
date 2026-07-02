

import pytest
from pathlib import Path

from research_radar.mini_gpt.data import load_text, make_batch, train_val_split


def test_load_text_reads_fixture() -> None:
    text = load_text(Path("tests/fixtures/mini_gpt_corpus.txt"))
    assert "Tiny models are useful" in text


def test_train_val_split_is_deterministic() -> None:
    ids = list(range(10))
    train_a, val_a = train_val_split(ids, train_ratio=0.8)
    train_b, val_b = train_val_split(ids, train_ratio=0.8)
    assert train_a == train_b
    assert val_a == val_b


def test_train_val_split_uses_ratio() -> None:
    train, val = train_val_split(list(range(10)), train_ratio=0.8)
    assert train == list(range(8))
    assert val == [8, 9]


def test_make_batch_returns_expected_shape() -> None:
    x, y = make_batch(list(range(20)), block_size=4, batch_size=3, seed=1)

    assert x.shape == (3, 4)
    assert y.shape == (3, 4)


def test_make_batch_targets_are_shifted_inputs() -> None:
    x, y = make_batch(list(range(20)), block_size=4, batch_size=3, seed=1)

    assert (x[:, 1:] == y[:, :-1]).all()


def test_make_batch_is_deterministic_with_seed() -> None:
    x1, y1 = make_batch(list(range(20)), block_size=4, batch_size=3, seed=42)
    x2, y2 = make_batch(list(range(20)), block_size=4, batch_size=3, seed=42)

    assert (x1 == x2).all()
    assert (y1 == y2).all()


def test_make_batch_fails_when_ids_are_too_short() -> None:
    with pytest.raises(ValueError):
        make_batch([1, 2, 3], block_size=3, batch_size=1)
