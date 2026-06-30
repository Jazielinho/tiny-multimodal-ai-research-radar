.PHONY: install test lint api

install:
	pip install -e ".[dev]"

test:
	pytest

lint:
	ruff check .

api:
	uvicorn app.api:app --reload
