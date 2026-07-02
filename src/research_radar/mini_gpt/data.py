

from pathlib import Path
import numpy as np


def load_text(path: str | Path) -> str:
    """Load text from a file."""
    text_path = Path(path)
    if not text_path.exists():
        raise FileNotFoundError(f"Text file not found: {text_path}")
    return text_path.read_text(encoding="utf-8")


def train_val_split(
        ids: list[int],
        train_ratio: float = 0.9,
) -> tuple[list[int], list[int]]:
    """Split a list of IDs into train and validation sets."""
    if not 0 < train_ratio < 1:
        raise ValueError("train_ratio must be between 0 and 1")
    if len(ids) < 2:
        raise ValueError("At least two IDs are required for train-val split")
    split_idx = int(len(ids) * train_ratio)
    return ids[:split_idx], ids[split_idx:]


def make_batch(
        ids: list[int],
        block_size: int,
        batch_size: int,
        seed: int | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    """ create input and target batches for next-token prediction. """
    if block_size <= 0:
        raise ValueError("block_size must be positive")
    if batch_size <= 0:
        raise ValueError("batch_size must be positive")
    if len(ids) <= block_size:
        raise ValueError("ids must be at least as long as block_size")

    rng = np.random.default_rng(seed)
    max_start = len(ids) - block_size - 1
    starts = rng.integers(0, max_start + 1, size=batch_size)

    x = np.array([ids[start : start + block_size] for start in starts])
    y = np.array([ids[start + 1 : start + block_size + 1] for start in starts])

    return x, y