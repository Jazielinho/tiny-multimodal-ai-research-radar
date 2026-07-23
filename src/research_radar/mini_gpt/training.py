
import torch
from torch.optim import Optimizer

from .model import BigramLanguageModel


def train_step(
        model: BigramLanguageModel,
        x: torch.Tensor,
        targets: torch.Tensor,
        optimizer: Optimizer
) -> float:
    model.train()
    optimizer.zero_grad()
    _, loss = model(x, targets)

    if loss is None:
        raise RuntimeError("Model did not return a loss")

    loss.backward()
    optimizer.step()

    return loss.detach().item()
