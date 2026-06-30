from rich import print

from research_radar.chunking import chunk_text
from research_radar.rag import SimpleKeywordRetriever, answer_with_context


def main() -> None:
    sample_text = (
        "RAG combines retrieval with generation. "
        "A retriever finds relevant chunks and a generator answers with context."
    )
    chunks = chunk_text(sample_text, paper_id="demo")
    retriever = SimpleKeywordRetriever(chunks)
    results = retriever.search("What is RAG?")
    answer = answer_with_context("What is RAG?", results)
    print(answer)


if __name__ == "__main__":
    main()
