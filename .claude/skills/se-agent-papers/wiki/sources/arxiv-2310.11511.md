---
type: source
title: "Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection"
created: 2026-11-19
arxiv_id: "2310.11511"
url: "https://arxiv.org/abs/2310.11511"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["retrieval-augmented-generation", "selective-retrieval", "grounded-generation", "rag-evaluation", "long-term-memory"]
source_path: "raw/papers/2310.11511.md"
sources: ["https://arxiv.org/abs/2310.11511"]
ingested: "2026-11-19"
---

# Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

**Paper:** [2310.11511](https://arxiv.org/abs/2310.11511) · [PDF](https://arxiv.org/pdf/2310.11511) · [HTML](https://arxiv.org/html/2310.11511)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** A model trained on critic annotations generates special tokens for retrieval need, passage relevance, support and usefulness. Weights and a threshold control the selection of the next segment. [PDF, p. 4](https://arxiv.org/pdf/2310.11511v1#page=4) [PDF, p. 5](https://arxiv.org/pdf/2310.11511v1#page=5) [PDF, p. 17](https://arxiv.org/pdf/2310.11511v1#page=17) [PDF, p. 19](https://arxiv.org/pdf/2310.11511v1#page=19)

**Key result.** Self-RAG 13B scored 55.8 on PopQA and 74.5 on PubHealth, compared with 50.8 and 54.7 for retrieval-augmented ChatGPT. On ARC, ChatGPT led 75.3 to 73.1. [PDF, p. 8](https://arxiv.org/pdf/2310.11511v1#page=8)

**Limitations and scope.** Citation precision and citation completeness are separate metrics. On ASQA, Self-RAG 13B scored 70.3 and 71.3, compared with 65.1 and 76.6 for retrieval-augmented ChatGPT. [PDF, p. 7](https://arxiv.org/pdf/2310.11511v1#page=7) [PDF, p. 8](https://arxiv.org/pdf/2310.11511v1#page=8)

[Section and table audit for 2310.11511v1](../reviews/audit-2026-11-19/2310.11511v1.md)

## Overview

The method trains a model to retrieve evidence adaptively and evaluate its own responses using reflection tokens. [PDF, p. 1](https://arxiv.org/pdf/2310.11511v1#page=1)

## Source files

arXiv version `2310.11511v1` · PDF pages: 30.

- [Original PDF](https://arxiv.org/pdf/2310.11511v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2310.11511.metadata.json)

PDF bookmarks — [Experiments (p. 6)](https://arxiv.org/pdf/2310.11511v1#page=6).

## Related concepts

- [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md)
- [Selective retrieval](../concepts/selective-retrieval.md)
- [Source-grounded generation](../concepts/grounded-generation.md)
- [RAG evaluation](../concepts/rag-evaluation.md)
- [Long-term memory](../concepts/long-term-memory.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
