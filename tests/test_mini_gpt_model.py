import pytest
import torch

from research_radar.mini_gpt.model import BigramLanguageModel


def test_bigram_model_returns_expected_logits_shape() -> None:
    vocab_size = 10
    batch_size = 2
    block_size = 3

    model = BigramLanguageModel(vocab_size=vocab_size)
    x = torch.randint(0, vocab_size, (batch_size, block_size))

    logits, loss = model(x)

    assert logits.shape == (batch_size, block_size, vocab_size)
    assert loss is None


def test_bigram_model_returns_scalar_loss_when_targets_are_given() -> None:
    vocab_size = 10
    batch_size = 2
    block_size = 3

    model = BigramLanguageModel(vocab_size=vocab_size)
    x = torch.randint(0, vocab_size, (batch_size, block_size))
    targets = torch.randint(0, vocab_size, (batch_size, block_size))

    logits, loss = model(x, targets)

    assert logits.shape == (batch_size, block_size, vocab_size)
    assert loss is not None
    assert loss.ndim == 0


def test_bigram_model_rejects_invalid_vocab_size() -> None:
    with pytest.raises(ValueError, match="vocab_size"):
        BigramLanguageModel(vocab_size=0)