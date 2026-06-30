from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Tiny Multimodal AI Research Radar",
    version="0.1.0",
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/ask")
def ask(request: QuestionRequest) -> dict[str, object]:
    return {
        "question": request.question,
        "answer": "RAG pipeline not connected yet. This endpoint is a Week 1 API stub.",
        "citations": [],
        "confidence": "not_available",
    }
