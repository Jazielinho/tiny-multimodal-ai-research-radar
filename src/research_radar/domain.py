from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Paper:
    paper_id: str
    title: str
    source_path: Path | None = None
    url: str | None = None


@dataclass(frozen=True)
class Chunk:
    chunk_id: str
    paper_id: str
    text: str
    page: int | None = None


@dataclass(frozen=True)
class SearchResult:
    chunk: Chunk
    score: float


@dataclass(frozen=True)
class Answer:
    question: str
    answer: str
    citations: list[str]
    confidence: str
