---
type: source
title: "Lost in the Middle: How Language Models Use Long Contexts"
created: 2026-11-19
arxiv_id: "2307.03172"
url: "https://arxiv.org/abs/2307.03172"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["context-window", "retrieval-augmented-generation", "grounded-generation", "long-term-memory"]
source_path: "raw/papers/2307.03172.md"
sources: ["https://arxiv.org/abs/2307.03172"]
ingested: "2026-11-19"
---

# Lost in the Middle: How Language Models Use Long Contexts

**Paper:** [2307.03172](https://arxiv.org/abs/2307.03172) · [PDF](https://arxiv.org/pdf/2307.03172) · [HTML](https://arxiv.org/html/2307.03172)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** For questions from NaturalQuestions-Open, the authors moved the answer-bearing document among distractors. A separate task isolated key–value lookup. Comparisons also included the model without documents and with one gold document. [PDF, p. 3](https://arxiv.org/pdf/2307.03172v3#page=3) [PDF, p. 5](https://arxiv.org/pdf/2307.03172v3#page=5) [PDF, p. 6](https://arxiv.org/pdf/2307.03172v3#page=6)

**Key result.** With 20 documents, GPT-3.5-Turbo achieved 75.8% accuracy when the answer-bearing document appeared first, 53.8% when it appeared tenth and 63.2% when it appeared last. The tenth-position result was below the 56.1% score without documents. [PDF, p. 5](https://arxiv.org/pdf/2307.03172v3#page=5) [PDF, p. 18](https://arxiv.org/pdf/2307.03172v3#page=18)

**Limitations and scope.** The effect depends on the task and model. Repeating the query before and after the data helped key retrieval but did not eliminate the mid-context decline in QA. Llama-2 7B primarily favored the end of the context. [PDF, p. 8](https://arxiv.org/pdf/2307.03172v3#page=8) [PDF, p. 15](https://arxiv.org/pdf/2307.03172v3#page=15) [PDF, p. 16](https://arxiv.org/pdf/2307.03172v3#page=16)

## Overview

The authors find that models can make less effective use of information placed in the middle of a long context. [PDF, p. 1](https://arxiv.org/pdf/2307.03172v3#page=1)

[Section and evidence audit](../reviews/audit-2026-11-19/2307.03172v3.md)

## Source files

arXiv version `2307.03172v3` · PDF pages: 18.

- [Original PDF](https://arxiv.org/pdf/2307.03172v3)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2307.03172.metadata.json)

## Related concepts

- [Context window](../concepts/context-window.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md)
- [Source-grounded generation](../concepts/grounded-generation.md)
- [Long-term memory](../concepts/long-term-memory.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
