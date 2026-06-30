# Tiny Multimodal AI Research Radar

> A focused 8-week sprint to build a small but serious AI research assistant with LLMs, RAG, multimodal understanding, agents, evaluation, and deployment.

## Mission

This project is a professional learning lab and portfolio project. The goal is not to build a huge product. The goal is to build a clear, testable and explainable system that proves practical competence in:

- LLM fundamentals
- RAG architecture
- embeddings, chunking and reranking
- multimodal AI with images and figures from papers
- agentic tools and failure modes
- FastAPI, Docker and deployment discipline
- evaluation and traceability

## Final demo

The final system should help a user:

1. discover AI papers;
2. ingest selected papers;
3. split and index paper content;
4. answer questions with citations;
5. analyze figures/images with a multimodal model;
6. compare papers;
7. generate a learning path;
8. generate quizzes to test understanding;
9. expose a small API and UI.

## Sprint window

**1 July 2026 — 31 August 2026**

This repository is connected to the sprint operating system in Google Drive:

- Master Plan: https://docs.google.com/document/d/1RX_KBJVQVv8YqRWywn7ABTN7cUMqzC3v47qbJqWeezQ/edit
- Weekly Reviews: https://docs.google.com/document/d/1LquySE40hljddDGU_BAiTvYb707mia3DjLecGhYgBXQ/edit
- Sprint Tracker: https://docs.google.com/spreadsheets/d/1os_1po7sSk5Wj7gj5dxqsRcof0tYch-I_PwVhbDfwvo/edit

## Repository structure

```text
.
├── app/                    # API and UI entrypoints
├── docs/                   # Architecture, roadmap, weekly reviews and decisions
├── notebooks/              # Weekly experiments
├── scripts/                # CLI scripts for ingestion, RAG and evaluation
├── src/research_radar/     # Main Python package
├── tests/                  # Smoke tests and evaluation tests
├── data/                   # Local data, ignored by git except .gitkeep
├── models/                 # Local models/checkpoints, ignored by git except .gitkeep
└── .github/                # CI, issue templates and PR template
```

## Weekly plan

| Week | Focus | Main output |
|---:|---|---|
| 1 | Foundation and direction | repo, README, architecture, paper list, ingestion stub |
| 2 | Mini GPT from scratch | tiny transformer, toy dataset, loss curve |
| 3 | RAG v1 | extraction, chunking, embeddings, vector store, cited answers |
| 4 | RAG v2 + evaluation | reranking, 20 eval questions, failure cases |
| 5 | CLIP and figures | image-text retrieval experiment |
| 6 | VLM for paper figures | figure Q&A and limitations |
| 7 | Agent with tools | search, summarize, compare, learning path, quiz |
| 8 | Professional demo | FastAPI, Docker, UI, final README, demo video |
| 9 | Jobs and authority | CV, LinkedIn, portfolio, pitch, outreach |

## Working rules

1. One main project only.
2. New ideas go to `docs/after-august.md`.
3. Morning is for deep work.
4. Nights are for light work, English, reading or recovery.
5. Every week must produce evidence: code, docs, post, video or metric.
6. Failure modes must be documented, not hidden.
7. Keep it small, useful and finished.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
pytest
uvicorn app.api:app --reload
```

## Current status

Sprint setup in progress.

Next milestone: **Week 1 — Foundation and direction**.
