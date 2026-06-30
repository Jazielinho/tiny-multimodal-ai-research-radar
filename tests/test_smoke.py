from research_radar.chunking import chunk_text
from research_radar.evaluation import precision_at_k
from research_radar.rag import SimpleKeywordRetriever


def test_chunk_text_creates_chunks() -> None:
    chunks = chunk_text("hello world " * 100, paper_id="demo", chunk_size=100, overlap=10)
    assert chunks
    assert chunks[0].paper_id == "demo"


def test_keyword_retriever_returns_results() -> None:
    chunks = chunk_text("RAG uses retrieval and generation.", paper_id="demo")
    retriever = SimpleKeywordRetriever(chunks)
    results = retriever.search("retrieval")
    assert results


def test_precision_at_k() -> None:
    assert precision_at_k(["a", "b"], ["b"], k=2) == 0.5
