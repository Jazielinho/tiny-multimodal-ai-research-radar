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

Actualizar esta review con la evidencia real y preparar Week 1.5 como pista de despegue para Mini GPT, sin adelantar toda la Semana 2.

## 2026-07-01 — Borrador interno y Week 1.5

### Contexto

La parte técnica principal de Week 1 quedó adelantada: repo creado, documentación base preparada, setup local verificado, pruebas ejecutadas y borrador interno del primer post añadido al repo.

La semana no se cierra formalmente hasta la review del domingo, pero se abre una fase controlada llamada **Week 1.5 — Mini GPT runway** para reducir riesgo antes de empezar la Semana 2.

### Acciones

- Borrador interno del primer post creado en `docs/posts/week-01-starting-the-sprint.md`: OK
- Evidencia de setup local subida en el commit `a346fe4`: OK
- Borrador interno y progreso de Week 1 subidos en el commit `90e1ca1`: OK
- Issue #2 creado para Week 1.5 — Mini GPT runway: OK

### Decisión

La publicación pública queda bloqueada hasta tener un hito técnico más fuerte: Mini GPT funcional, RAG con citas, evaluación real, experimento multimodal o demo.

### Siguiente paso

Crear `docs/experiments/mini-gpt-plan.md` con objetivo, alcance, dataset candidato, tokenizer/data-loader, métrica mínima y límites.

## Promised deliverables

- [x] Repository created
- [x] README created
- [x] Architecture documented
- [x] Paper list created
- [x] Basic ingestion script
- [x] First post draft created as internal material
- [ ] Weekly review completed on Sunday

## Evidence

- Repo: https://github.com/Jazielinho/tiny-multimodal-ai-research-radar
- Setup commit: `a346fe4` — Add local setup verification for Week 1 review
- Post/progress commit: `90e1ca1` — Add Week 1 sprint kickoff and progress documentation
- Post draft: `docs/posts/week-01-starting-the-sprint.md`
- Week 1.5 issue: https://github.com/Jazielinho/tiny-multimodal-ai-research-radar/issues/2
- Video/explanation: pending
- Demo/capture: pending

## What I learned

- La base del proyecto cuenta: entorno, tests, lint, documentación y commits son evidencia real.
- No hace falta publicar por publicar. La visibilidad pública debe esperar a un hito técnico con más valor.
- Week 1 puede ir adelantada técnicamente sin mover todo el roadmap: Week 1.5 prepara Mini GPT sin cambiar el alcance.

## What failed or blocked me

- No hubo bloqueo técnico en setup local: `pytest` y `ruff` pasaron.
- El riesgo principal es confundir avance rápido con permiso para abrir más scope.
- La publicación pública queda pospuesta de forma intencional.

## Energy and recovery

- Average energy, 1-5: 3
- Sleep, 1-5: 3
- CrossFit/lesions: Continue protecting shoulder and recovery. Do not add more load just to force sprint progress.
- Heat impact: High on several days. It required minimum mode and avoiding heavy study at night.

## Score

| Area | Score |
|---|---:|
| Deep AI work | 3 |
| Code/repo | 4 |
| Documentation | 4 |
| English | 2 |
| Speaking/oratory | 1 |
| Public content | 2 |
| Health/family/sleep | 3 |

## Next week adjustment

Keep:
- Morning or focused AI blocks.
- Evidence-based work: commit, tests and worklog.
- Small tasks before complex model work.

Cut:
- Guilt-driven recovery.
- Reading without applying.
- Starting new architecture before defining scope.

Add:
- One short review block after each technical task.
- One clear next issue before implementing.

Main risk:
- Jumping from bigram baseline to transformer too fast.

Recommended mode:
- Normal if energy is good; minimum if sleep, heat or stomach symptoms are bad.
