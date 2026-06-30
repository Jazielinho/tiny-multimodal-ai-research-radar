from pathlib import Path

import typer
from rich import print

from research_radar.chunking import chunk_text
from research_radar.ingestion import extract_text_from_pdf

app = typer.Typer()


@app.command()
def ingest(pdf_path: Path, paper_id: str = "paper-001") -> None:
    text = extract_text_from_pdf(pdf_path)
    chunks = chunk_text(text=text, paper_id=paper_id)
    print(f"[green]Extracted {len(text)} characters[/green]")
    print(f"[green]Created {len(chunks)} chunks[/green]")


if __name__ == "__main__":
    app()
