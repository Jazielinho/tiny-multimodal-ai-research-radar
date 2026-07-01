# Week 1 Review — Foundation and Direction

## Dates

1 July 2026 — 5 July 2026

## 2026-07-01 — Setup local

### Contexto

Setup local verificado en Windows usando `uv` y CPython 3.11.14.

Se recreó `.venv` con `uv` y se ejecutaron las herramientas usando el intérprete explícito del entorno.

### Acciones

- Entorno virtual recreado con `uv venv --python 3.11 --seed --clear .venv`: OK
- Dependencias instaladas con `uv pip install --python .\.venv\Scripts\python.exe -e ".[dev]"`: OK
- Pruebas básicas ejecutadas con `.\.venv\Scripts\python.exe -m pytest`: OK
- Lint ejecutado con `.\.venv\Scripts\python.exe -m ruff check .`: OK

### Resultado

El setup local queda verificado.

### Evidencia

```text
Python: 3.11.14
pip: 26.1.2
pytest: 3 passed
ruff check .: All checks passed
```

### Decisión

Usar `uv` con Python 3.11 como entorno local del proyecto. Esta versión coincide con la versión usada en CI y reduce problemas con comandos globales como `python`, `pip`, `pytest` o `ruff`.

### Siguiente paso

Hacer commit de esta evidencia de setup y continuar con el siguiente pendiente de Week 1: preparar el primer borrador de post público.

## Promised deliverables

- [ ] Repository created
- [ ] README created
- [ ] Architecture documented
- [ ] Paper list created
- [ ] Basic ingestion script
- [ ] First public post

## Evidence

- Repo:
- Commit: pending for local setup evidence
- Post:
- Video/explanation:
- Demo/capture:

## What I learned

-

## What failed or blocked me

-

## Energy and recovery

- Average energy, 1-5:
- Sleep, 1-5:
- CrossFit/lesions:
- Heat impact:

## Score

| Area | Score |
|---|---:|
| Deep AI work |  |
| Code/repo |  |
| Documentation |  |
| English |  |
| Speaking/oratory |  |
| Public content |  |
| Health/family/sleep |  |

## Next week adjustment

Keep:

Cut:

Add:

Main risk:

Recommended mode:
