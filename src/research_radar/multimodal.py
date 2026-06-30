from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class FigureAnalysis:
    image_path: Path
    question: str
    answer: str
    confidence: str
    limitations: list[str]


def analyze_figure_placeholder(image_path: str | Path, question: str) -> FigureAnalysis:
    """Placeholder for Week 5-6 multimodal experiments.

    Later implementations may use CLIP for retrieval and a VLM for visual Q&A.
    """
    path = Path(image_path)
    return FigureAnalysis(
        image_path=path,
        question=question,
        answer="Multimodal model not connected yet.",
        confidence="not_available",
        limitations=["Placeholder implementation."],
    )
