---
type: source
title: "ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction"
created: 2026-11-19
arxiv_id: "2112.01488"
url: "https://arxiv.org/abs/2112.01488"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["retrieval-augmented-generation", "late-interaction", "knowledge-graph", "entity-extraction", "grounded-generation", "rag-evaluation", "llm-as-judge", "stateful-tool-use"]
source_path: "raw/papers/2112.01488.md"
sources: ["https://arxiv.org/abs/2112.01488"]
ingested: "2026-11-19"
---

# ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction

**Paper:** [2112.01488](https://arxiv.org/abs/2112.01488) · [PDF](https://arxiv.org/pdf/2112.01488) · [HTML](https://arxiv.org/html/2112.01488)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** ColBERTv2 scores documents at token level, distills a teacher model's score distribution and stores a centroid and quantized residual for each representation. [PDF, p. 3](https://arxiv.org/pdf/2112.01488v3#page=3) [PDF, p. 4](https://arxiv.org/pdf/2112.01488v3#page=4) [PDF, p. 5](https://arxiv.org/pdf/2112.01488v3#page=5)

**Key result.** On MS MARCO, the ColBERT index occupied 154 GiB. ColBERTv2 used 16 GiB with one residual bit per dimension or 25 GiB with two, reducing space by factors of about 9.6 and 6.2, respectively. On the official development set, ColBERTv2 scored 39.7 MRR@10 versus 36.0 for the original ColBERT. [PDF, p. 7](https://arxiv.org/pdf/2112.01488v3#page=7) [PDF, p. 9](https://arxiv.org/pdf/2112.01488v3#page=9)

**Limitations and scope.** The tests use English, and the transfer comparisons cover models trained on MS MARCO. The separate ablation isolates the effect of compression on quality. The main model also uses a modified training procedure. [PDF, p. 7](https://arxiv.org/pdf/2112.01488v3#page=7) [PDF, p. 10](https://arxiv.org/pdf/2112.01488v3#page=10) [PDF, p. 15](https://arxiv.org/pdf/2112.01488v3#page=15)

## Overview

The method combines multi-vector retrieval, late token interaction, representation compression and training with denoised supervision. [PDF, p. 1](https://arxiv.org/pdf/2112.01488v3#page=1)

[Section and evidence audit](../reviews/audit-2026-11-19/2112.01488v3.md)

## Source files

arXiv version `2112.01488v3` · PDF pages: 20.

- [Original PDF](https://arxiv.org/pdf/2112.01488v3)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2112.01488.metadata.json)

## Related concepts

- [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md)
- [Late interaction](../concepts/late-interaction.md)
- [Knowledge graph](../concepts/knowledge-graph.md)
- [Entity extraction](../concepts/entity-extraction.md)
- [Source-grounded generation](../concepts/grounded-generation.md)
- [RAG evaluation](../concepts/rag-evaluation.md)
- [LLM-as-a-Judge](../concepts/llm-as-judge.md)
- [Stateful tool use](../concepts/stateful-tool-use.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
