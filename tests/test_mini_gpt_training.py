import math

import torch

from research_radar.mini_gpt.model import BigramLanguageModel
from research_radar.mini_gpt.training import train_step


def test_train_step_returns_finite_loss() -> None:
    torch.manual_seed(0)

    model = BigramLanguageModel(vocab_size=10)
    optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
    x = torch.tensor([[1, 2, 3], [4, 5, 6]])
    targets = torch.tensor([[2, 3, 4], [5, 6, 7]])

    loss = train_step(model, x, targets, optimizer)

    assert isinstance(loss, float)
    assert math.isfinite(loss)


def test_train_step_updates_model_parameters() -> None:
    torch.manual_seed(0)

    model = BigramLanguageModel(vocab_size=10)
    optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
    x = torch.tensor([[1, 2, 3], [4, 5, 6]])
    targets = torch.tensor([[2, 3, 4], [5, 6, 7]])
    parameters_before = [
        parameter.detach().clone() for parameter in model.parameters()
    ]

    train_step(model, x, targets, optimizer)

    parameters_changed = any(
        not torch.equal(before, after.detach())
        for before, after in zip(parameters_before, model.parameters())
    )

    assert parameters_changed
