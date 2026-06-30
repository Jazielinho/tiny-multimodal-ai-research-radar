from pathlib import Path

import fitz  # PyMuPDF


def extract_text_from_pdf(path: str | Path) -> str:
    """Extract text from a PDF using PyMuPDF.

    Week 1 goal: simple extraction only.
    Later: keep page numbers, section titles, figures and metadata.
    """
    pdf_path = Path(path)
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    parts: list[str] = []
    with fitz.open(pdf_path) as doc:
        for page in doc:
            parts.append(page.get_text())

    return "\n".join(parts)
