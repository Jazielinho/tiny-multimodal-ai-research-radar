# Architecture

## High-level pipeline

```text
Paper source
  -> ingestion
  -> text extraction
  -> chunking
  -> embeddings
  -> vector index
  -> reranking
  -> grounded answer
  -> citations and evaluation
```

## Multimodal path

```text
PDF figures/images
  -> image extraction
  -> CLIP retrieval
  -> VLM visual Q&A
  -> answer with limitations
```

## Agent path

```text
User goal
  -> planner
  -> tool selection
  -> tool calls
  -> answer synthesis
  -> logs and failure analysis
```

## Design principles

1. Start with a simple baseline.
2. Add evaluation before adding complexity.
3. Keep citations and traceability visible.
4. Prefer explicit failure over confident hallucination.
5. Keep every week independently demonstrable.
