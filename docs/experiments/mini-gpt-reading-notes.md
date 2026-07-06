# Mini GPT Reading Notes

Use this file only for notes that change the project.

Do not summarize chapters for the sake of summarizing.

## Reading rule

Each useful reading block must produce:

- 3 ideas understood;
- 1 decision for the repo;
- 1 thing not to do;
- 1 evidence artifact.

## Reading block template

### Date

YYYY-MM-DD

### Source

Book / chapter / section:

### 3 ideas understood

1.
2.
3.

### Decision for the repo

-

### Thing not to do

-

### Evidence artifact

- Commit / test / doc / issue / code path:

## Applied notes

### Date

2026-07-06

### Source

Build a Large Language Model From Scratch — Chapter 2: Working with text data.

### 3 ideas understood

1. Un modelo de lenguaje no trabaja directamente con texto bruto. Primero el texto se divide en tokens y después cada token se convierte en un ID numérico. En el Mini GPT actual, el tokenizer es por caracteres, así que `"casa."` se convierte en tokens como `["c", "a", "s", "a", "."]` y después en una lista de IDs.
2. Para next-token prediction, `x` es la secuencia de entrada e `y` es la misma secuencia desplazada un token hacia delante. Por ejemplo, si `x = [5, 6, 7]`, entonces `y = [6, 7, 8]`. Esto permite que el modelo aprenda varias predicciones dentro de una misma fila: `5 -> 6`, `5, 6 -> 7` y `5, 6, 7 -> 8`.
3. `block_size`, `batch_size`, embeddings y posiciones tienen responsabilidades distintas. `block_size` define cuánto contexto ve cada ejemplo, `batch_size` define cuántos ejemplos se procesan juntos, el token embedding representa el contenido del token y el positional embedding añade información sobre el orden dentro de la secuencia.

### Decision for the repo

- Mantener el primer pipeline de Mini GPT simple y trazable: tokenizer por caracteres, `ids` como lista 1D, batches `x/y` con la misma forma y sin padding ni tokens especiales hasta que se defina una tarea específica para ello.

### Thing not to do

- No implementar embeddings, attention, training loop, BPE, padding ni tokens especiales antes de definir Task 02 con alcance cerrado.

### Evidence artifact

- Task 01 commit: `4382f9c5d9bea58cf8fef4d397fb58c713b66ec8`.
- Code paths reviewed: `src/research_radar/mini_gpt/tokenizer.py` and `src/research_radar/mini_gpt/data.py`.

## Initial recommended notes

### Build a Large Language Model From Scratch — Chapter 2

Focus:

- tokenization;
- encode/decode;
- text-to-token IDs;
- input-target creation.

Expected repo impact:

- tokenizer baseline;
- data-loader baseline;
- tests for reversible encoding and shifted targets.

### AI Engineering — Chapter 1

Focus:

- what AI engineering is;
- language models and foundation models;
- why evaluation matters more with open-ended outputs.

Expected repo impact:

- clearer Mini GPT purpose;
- limitation notes;
- explanation suitable for interviews.

### Designing Machine Learning Systems — Chapter 2

Focus:

- objectives;
- requirements;
- reliability;
- maintainability;
- why systems need clear success criteria.

Expected repo impact:

- Mini GPT success criteria;
- scope boundaries;
- evidence gates.
