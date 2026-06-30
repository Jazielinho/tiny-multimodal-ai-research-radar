# Evaluation Plan

## Why evaluation matters

This project should not only look good in a demo. It should show engineering judgment.

## RAG evaluation

Initial metrics:

- precision@k
- recall@k
- answer groundedness, manual
- abstention quality
- citation correctness

## Evaluation set

Start with 20 questions:

- 10 factual questions
- 5 comparison questions
- 3 method questions
- 2 trick/unknown questions where the system should abstain

## Weekly rule

Every new RAG feature must include at least one example where it works and one where it fails.
