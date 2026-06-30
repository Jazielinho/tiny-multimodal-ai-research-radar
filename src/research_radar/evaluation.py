from dataclasses import dataclass


@dataclass(frozen=True)
class EvalQuestion:
    question: str
    expected_evidence: list[str]


def precision_at_k(retrieved_ids: list[str], expected_ids: list[str], k: int) -> float:
    if k <= 0:
        raise ValueError("k must be positive")
    top_k = retrieved_ids[:k]
    if not top_k:
        return 0.0
    expected = set(expected_ids)
    hits = sum(1 for item in top_k if item in expected)
    return hits / len(top_k)
