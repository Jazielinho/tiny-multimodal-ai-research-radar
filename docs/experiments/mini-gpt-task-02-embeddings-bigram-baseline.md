# Mini GPT Task 02 — Embeddings y baseline bigram

## Objetivo

Definir el siguiente paso mínimo después de Task 01 y dejarlo listo para implementar de forma controlada:

1. explicar cómo los token IDs pasan a representaciones numéricas aprendibles;
2. crear un primer baseline entrenable tipo bigram;
3. comprobar con tests que las formas de entrada, logits y loss son correctas.

Esta tarea no busca crear un GPT completo. Busca construir el primer modelo mínimo antes de avanzar a embeddings posicionales completos, attention causal y transformer blocks.

## Estado de esta especificación

Este documento cierra la definición de alcance de Task 02.

La implementación de Task 02 se hará después, en otro bloque de trabajo, siguiendo este contrato. No se debe empezar a programar modelo, attention ni training loop hasta que esta especificación esté revisada.

## Por qué importa esta tarea

Task 01 demostró que el pipeline de datos funciona:

- texto bruto -> tokens;
- tokens -> token IDs;
- token IDs -> batches `x/y`;
- `y` es `x` desplazado un token hacia delante.

Task 02 debe demostrar el siguiente paso técnico:

- los IDs no se usan como números con significado matemático directo;
- un modelo necesita parámetros aprendibles;
- el modelo debe producir logits con forma predecible;
- la loss debe poder compararse contra los targets `y`;
- antes de añadir attention, necesitamos un baseline simple que podamos testear.

## Qué es y qué no es el baseline bigram

`BigramLanguageModel` no es un modelo de attention.

Es un baseline mínimo que aprende algo mucho más simple:

```text
token actual -> logits del siguiente token
```

En una implementación típica, puede usar una tabla aprendible con forma:

```text
(vocab_size, vocab_size)
```

Cada fila representa las puntuaciones que el modelo asigna al siguiente token dado el token actual.

Esto se parece a una tabla de embeddings porque se consulta por ID, pero no es todavía el bloque de embeddings completo de un GPT moderno:

- no tiene attention;
- no mezcla información entre varias posiciones;
- no usa contexto largo de verdad;
- no tiene transformer blocks;
- no es el destino final de Semana 2.

Sirve como primer modelo entrenable porque permite validar:

- forward pass;
- logits;
- loss;
- shapes;
- integración con `x/y`.

## Relación con el modelo del libro

El libro avanza hacia un GPT pequeño con:

```text
token IDs
-> token embeddings
-> positional embeddings
-> attention causal
-> transformer blocks
-> logits
-> loss
-> generación
```

Task 02 no implementa toda esa cadena. Implementa el primer escalón entrenable para no saltar directamente a un transformer sin haber validado logits y loss.

La ruta prevista es:

```text
Task 01: tokenizer + data-loader
Task 02: baseline bigram + logits/loss
Task 03: token embeddings + positional embeddings explícitos
Task 04: causal self-attention
Task 05: transformer block
Task 06: mini GPT entrenable + generación básica
```

Por tanto, sí: el objetivo de Semana 2 sigue siendo entrenar un modelo real, pequeño y cercano mecánicamente a un GPT. El baseline bigram es un escalón de control, no el modelo final.

## Idea técnica

Un batch de entrada llega como IDs:

```text
x.shape = (batch_size, block_size)
```

Por ejemplo:

```text
x = [
  [5, 6, 7],
  [2, 3, 4],
]
```

El modelo debe devolver puntuaciones para cada token posible del vocabulario:

```text
logits.shape = (batch_size, block_size, vocab_size)
```

Si:

```text
batch_size = 2
block_size = 3
vocab_size = 10
```

entonces:

```text
logits.shape = (2, 3, 10)
```

Esto significa:

- 2 ejemplos en el batch;
- 3 posiciones por ejemplo;
- 10 posibles tokens para cada posición.

## Alcance

Entra en esta tarea:

- explicar la diferencia entre token ID, tabla aprendible y logits;
- crear un módulo mínimo en `src/research_radar/mini_gpt/model.py`;
- implementar `BigramLanguageModel`;
- aceptar `x` con forma `(batch_size, block_size)`;
- devolver logits con forma `(batch_size, block_size, vocab_size)`;
- calcular loss si se pasan `targets`;
- añadir tests mínimos de forward pass y shapes;
- mantener todo CPU-friendly y pequeño.

## Fuera de alcance

No entra en esta tarea:

- multi-head attention;
- causal self-attention;
- transformer block;
- GPT completo;
- training loop largo;
- generación de texto;
- token embeddings + positional embeddings como bloque GPT completo;
- GPU;
- BPE;
- padding;
- tokens especiales;
- RAG;
- agentes;
- multimodal.

Si aparece la tentación de añadir cualquiera de esos puntos, se documenta como tarea futura y no se mezcla en este commit.

## Diseño recomendado para Task 02

La implementación puede empezar con un baseline muy pequeño:

```python
class BigramLanguageModel:
    ...
```

Responsabilidad mínima:

- recibir `x`;
- consultar una tabla aprendible para obtener logits;
- devolver logits con la forma esperada;
- si recibe `targets`, devolver también una loss.

El baseline bigram no necesita attention. Predice el siguiente token usando información muy limitada. Precisamente por eso sirve como baseline: es simple, fácil de probar y deja claro qué mejora aportarán embeddings posicionales, attention y contexto más adelante.

## Decisión crítica

No mezclar dos objetivos en la misma tarea:

- Task 02 valida que existe un modelo entrenable mínimo con logits y loss.
- Task 03 introducirá embeddings más cercanos al GPT del libro.

Esto evita una tarea demasiado grande y mantiene la evidencia clara.

## Archivos a crear o modificar

Crear:

```text
src/research_radar/mini_gpt/model.py
tests/test_mini_gpt_model.py
```

Este documento define el alcance:

```text
docs/experiments/mini-gpt-task-02-embeddings-bigram-baseline.md
```

Actualizar al cerrar la tarea:

```text
docs/experiments/mini-gpt-worklog.md
```

## Dependencias

Para implementar el modelo probablemente usaremos PyTorch, que ya está declarado como extra opcional `ml` en `pyproject.toml`.

Antes de implementar, verificar o instalar:

```bash
uv pip install --python .\.venv\Scripts\python.exe -e ".[dev,ml]"
```

En Linux/macOS, el equivalente sería:

```bash
uv pip install --python .venv/bin/python -e ".[dev,ml]"
```

## Tests mínimos

Los tests deben comprobar al menos:

1. el modelo acepta un batch de IDs con forma `(batch_size, block_size)`;
2. el modelo devuelve logits con forma `(batch_size, block_size, vocab_size)`;
3. si se pasan targets, la loss existe y es un escalar;
4. el forward pass funciona en CPU;
5. no se necesita attention para que el baseline corra.

Ejemplo conceptual:

```text
x.shape = (2, 3)
logits.shape = (2, 3, vocab_size)
```

## Criterio de terminado de la especificación

La definición de Task 02 queda lista cuando:

- este documento existe;
- el alcance está escrito en castellano y es entendible;
- queda claro que bigram no es attention;
- queda claro que el mini GPT real vendrá en tareas posteriores;
- queda claro qué archivos, tests y comandos se usarán.

## Criterio de terminado de la implementación

Task 02 estará terminada cuando:

- `model.py` exista;
- `tests/test_mini_gpt_model.py` exista;
- el baseline tenga un forward pass mínimo;
- los logits tengan la forma esperada;
- la loss funcione si se pasan targets;
- `pytest` pase;
- `ruff check .` pase;
- el worklog quede actualizado con comandos y resultado;
- el commit quede subido a GitHub.

## Comandos de validación

En Windows:

```bash
.\.venv\Scripts\python.exe -m pytest
.\.venv\Scripts\python.exe -m ruff check .
```

Si el entorno está activado:

```bash
pytest
ruff check .
```

## Preguntas que esta tarea debe poder responder

Al cerrar Task 02, debería poder explicarse:

1. por qué un token ID no es suficiente como representación semántica;
2. qué hace una tabla aprendible en el baseline bigram;
3. qué forma tiene la entrada `x`;
4. qué forma tienen los logits;
5. por qué un baseline bigram es útil aunque sea limitado;
6. por qué bigram no es attention;
7. qué queda pendiente para acercarse al GPT del libro.

## Limitaciones esperadas

Este baseline será débil a propósito:

- no entiende contexto largo;
- no usa attention;
- no modela relaciones complejas entre posiciones;
- no generará texto de calidad;
- solo sirve para validar el primer paso de modelo.

Esa limitación es aceptable. El objetivo de Task 02 es crear una base pequeña, testeable y explicable antes de avanzar.

## Siguiente tarea después de Task 02

Solo después de cerrar Task 02 se podrá definir una tarea nueva para uno de estos bloques:

- token embeddings explícitos;
- positional embeddings;
- causal self-attention;
- causal mask;
- transformer block;
- training loop corto;
- generación básica.

No se debe empezar ninguna de esas partes dentro de Task 02.
