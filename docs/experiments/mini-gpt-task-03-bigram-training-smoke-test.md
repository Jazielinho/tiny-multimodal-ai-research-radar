# Mini GPT Task 03 - Smoke test de entrenamiento bigram

## Objetivo

Comprobar que el baseline bigram puede ejecutar un paso mínimo de entrenamiento.

## Por qué importa

Task 02 probó que el modelo produce logits y loss.

Task 03 debe probar que la loss puede hacer backpropagation y que los parámetros cambian tras `optimizer.step()`.

## En alcance

- Un helper pequeño de entrenamiento.
- Un único paso de optimización.
- CPU solamente.
- Loss finita.
- Al menos un parámetro actualizado.
- Tests mínimos.
- Worklog actualizado al cerrar.

## Fuera de alcance

- Training loop largo.
- Curva de loss.
- Generación de texto.
- Embeddings posicionales.
- Attention o causal mask.
- Transformer blocks.
- GPU.
- RAG, agents o multimodal.

## Archivos

Crear:

```text
src/research_radar/mini_gpt/training.py
tests/test_mini_gpt_training.py
```

Actualizar al cerrar:

```text
docs/experiments/mini-gpt-worklog.md
```

## API propuesta

```python
def train_step(model, x, targets, optimizer) -> float:
    ...
```

Debe:

1. poner el modelo en modo entrenamiento;
2. limpiar gradientes;
3. calcular logits y loss;
4. hacer `loss.backward()`;
5. ejecutar `optimizer.step()`;
6. devolver la loss como `float`.

## Tests

Comprobar:

- `train_step` devuelve una loss finita.
- `train_step` cambia al menos un parámetro del modelo.

No comprobar todavía que la loss baja mucho.

## Criterio de terminado

- `training.py` existe.
- Los tests de entrenamiento existen.
- `pytest` pasa.
- `ruff check .` pasa.
- El worklog queda actualizado.

## Decisión

Mantener esta tarea limitada a un smoke test de entrenamiento.

No añadir generation, attention, embeddings posicionales ni transformer blocks.
