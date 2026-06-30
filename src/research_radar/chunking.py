from research_radar.domain import Chunk


def chunk_text(
    text: str,
    paper_id: str,
    chunk_size: int = 900,
    overlap: int = 150,
) -> list[Chunk]:
    """Split text into overlapping character chunks.

    This is intentionally simple for Week 1-3. Later, compare this with
    section-aware and token-aware chunking.
    """
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")
    if overlap < 0:
        raise ValueError("overlap cannot be negative")
    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    clean = " ".join(text.split())
    chunks: list[Chunk] = []
    start = 0
    idx = 0

    while start < len(clean):
        end = min(start + chunk_size, len(clean))
        chunk_text_value = clean[start:end]
        chunks.append(
            Chunk(
                chunk_id=f"{paper_id}::chunk-{idx:04d}",
                paper_id=paper_id,
                text=chunk_text_value,
                page=None,
            )
        )
        idx += 1
        if end == len(clean):
            break
        start = end - overlap

    return chunks
