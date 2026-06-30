from research_radar.domain import Answer, Chunk, SearchResult


class SimpleKeywordRetriever:
    """A deliberately simple retriever for the first working baseline.

    This is not the final RAG system. It gives us a baseline before adding
    embeddings, vector search and reranking.
    """

    def __init__(self, chunks: list[Chunk]) -> None:
        self.chunks = chunks

    def search(self, query: str, top_k: int = 5) -> list[SearchResult]:
        query_terms = set(query.lower().split())
        scored: list[SearchResult] = []

        for chunk in self.chunks:
            chunk_terms = set(chunk.text.lower().split())
            score = len(query_terms & chunk_terms) / max(len(query_terms), 1)
            if score > 0:
                scored.append(SearchResult(chunk=chunk, score=score))

        return sorted(scored, key=lambda item: item.score, reverse=True)[:top_k]


def answer_with_context(question: str, results: list[SearchResult]) -> Answer:
    """Create a placeholder answer with citations.

    Later this should call an LLM and enforce grounded answering.
    """
    if not results:
        return Answer(
            question=question,
            answer="I do not have enough retrieved evidence to answer this question.",
            citations=[],
            confidence="low",
        )

    citations = [result.chunk.chunk_id for result in results]
    answer = (
        "Baseline answer placeholder. Retrieved evidence is available, "
        "but LLM generation has not been connected yet."
    )

    return Answer(
        question=question,
        answer=answer,
        citations=citations,
        confidence="baseline",
    )
