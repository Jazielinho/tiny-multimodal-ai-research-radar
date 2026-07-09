from __future__ import annotations

import torch
from torch import nn
import torch.nn.functional as F


class BigramLanguageModel(nn.Module):
    """A simple bigram language model."""

    def __init__(self, vocab_size: int):
        super().__init__()
        if vocab_size <= 0:
            raise ValueError("vocab_size must be positive")

        self.vocab_size = vocab_size
        self.token_embedding_table = nn.Embedding(vocab_size, vocab_size)

    def forward(
            self,
            x: torch.Tensor,
            targets: torch.Tensor | None = None
    ) -> tuple[torch.Tensor, torch.Tensor | None]:
        """ Forward pass."""

        logits = self.token_embedding_table(x)
        loss = None
        if targets is not None:
            batch_size, block_size, vocab_size = logits.shape
            logits_flat = logits.view(batch_size * block_size, vocab_size)
            targets_flat = targets.view(batch_size * block_size)
            loss = F.cross_entropy(logits_flat, targets_flat)

        return logits, loss