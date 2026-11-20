---
type: source
title: "ColPali: Efficient Document Retrieval with Vision Language Models"
created: 2026-11-19
arxiv_id: "2407.01449"
url: "https://arxiv.org/abs/2407.01449"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["retrieval-augmented-generation", "dense-retrieval", "late-interaction", "knowledge-graph", "entity-extraction", "grounded-generation", "rag-evaluation", "llm-as-judge"]
source_path: "raw/papers/2407.01449.md"
sources: ["https://arxiv.org/abs/2407.01449"]
ingested: "2026-11-19"
---

# ColPali: Efficient Document Retrieval with Vision Language Models

**Paper:** [2407.01449](https://arxiv.org/abs/2407.01449) · [PDF](https://arxiv.org/pdf/2407.01449) · [HTML](https://arxiv.org/html/2407.01449)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** ColPali maps page images and query tokens to sets of vectors. Ranking matches individual tokens to regions of a page image. ViDoRe evaluates retrieval of the source page. [PDF, p. 4](https://arxiv.org/pdf/2407.01449v6#page=4) [PDF, p. 6](https://arxiv.org/pdf/2407.01449v6#page=6)

**Key result.** Across ten ViDoRe datasets, mean nDCG@5 was 81.3 for ColPali, 58.8 for BiPali and 67.0 for BGE-M3 with captions. A separate comparison reports Recall@1 of 72.7 for ColPali. [PDF, p. 7](https://arxiv.org/pdf/2407.01449v6#page=7) [PDF, p. 21](https://arxiv.org/pdf/2407.01449v6#page=21)

**Limitations and scope.** The study evaluates page retrieval. On DocVQA, ColPali's float16 representations occupied 257.5 KB per page, compared with 8.60 KB for BGE-M3. The impact of compression depends on document type. [PDF, p. 4](https://arxiv.org/pdf/2407.01449v6#page=4) [PDF, p. 8](https://arxiv.org/pdf/2407.01449v6#page=8) [PDF, p. 9](https://arxiv.org/pdf/2407.01449v6#page=9) [PDF, p. 18](https://arxiv.org/pdf/2407.01449v6#page=18)

## Overview

The method retrieves visually complex documents using multi-vector embeddings of page images and evaluates retrieval on ViDoRe. [PDF, p. 1](https://arxiv.org/pdf/2407.01449v6#page=1)

[Section and evidence audit](../reviews/audit-2026-11-19/2407.01449v6.md)

## Source files

arXiv version `2407.01449v6` · PDF pages: 26.

- [Original PDF](https://arxiv.org/pdf/2407.01449v6)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2407.01449.metadata.json)

PDF bookmarks — [Results (p. 7)](https://arxiv.org/pdf/2407.01449v6#page=7).

## Related concepts

- [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md)
- [Dense retrieval](../concepts/dense-retrieval.md)
- [Late interaction](../concepts/late-interaction.md)
- [Knowledge graph](../concepts/knowledge-graph.md)
- [Entity extraction](../concepts/entity-extraction.md)
- [Source-grounded generation](../concepts/grounded-generation.md)
- [RAG evaluation](../concepts/rag-evaluation.md)
- [LLM-as-a-Judge](../concepts/llm-as-judge.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
