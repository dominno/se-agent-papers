---
type: source
title: "HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models"
created: 2026-11-19
arxiv_id: "2405.14831"
url: "https://arxiv.org/abs/2405.14831"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["long-term-memory", "memory-evaluation", "retrieval-augmented-generation", "graph-rag", "grounded-generation"]
source_path: "raw/papers/2405.14831.md"
sources: ["https://arxiv.org/abs/2405.14831"]
ingested: "2026-11-19"
---

# HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models

**Paper:** [2405.14831](https://arxiv.org/abs/2405.14831) · [PDF](https://arxiv.org/pdf/2405.14831) · [HTML](https://arxiv.org/html/2405.14831)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** HippoRAG indexes passages as a graph of entities and relations. For a new question it identifies entities and ranks passages in one retrieval step using Personalized PageRank. [PDF, p. 3](https://arxiv.org/pdf/2405.14831v3#page=3) [PDF, p. 4](https://arxiv.org/pdf/2405.14831v3#page=4) [PDF, p. 5](https://arxiv.org/pdf/2405.14831v3#page=5)

**Key result.** Across three datasets, mean R@5 rose from 65.6 for ColBERTv2 to 72.9 with HippoRAG. For 1,000 queries, the authors report $0.10 in API costs and three minutes, compared with $1–3 and 20–40 minutes for IRCoT. [PDF, p. 6](https://arxiv.org/pdf/2405.14831v3#page=6) [PDF, p. 28](https://arxiv.org/pdf/2405.14831v3#page=28)

**Limitations and scope.** The savings apply to queries after index construction. Results depend on preserving context during entity and relation extraction. On HotpotQA, single-step HippoRAG with ColBERTv2 had R@5 1.6 points below ColBERTv2 alone. [PDF, p. 6](https://arxiv.org/pdf/2405.14831v3#page=6) [PDF, p. 25](https://arxiv.org/pdf/2405.14831v3#page=25) [PDF, p. 26](https://arxiv.org/pdf/2405.14831v3#page=26) [PDF, p. 28](https://arxiv.org/pdf/2405.14831v3#page=28)

## Overview

Knowledge graphs and Personalized PageRank support associations between facts and multi-hop retrieval. [PDF, p. 1](https://arxiv.org/pdf/2405.14831v3#page=1)

[Section and evidence audit](../reviews/audit-2026-11-19/2405.14831v3.md)

## Source files

arXiv version `2405.14831v3` · PDF pages: 31.

- [Original PDF](https://arxiv.org/pdf/2405.14831v3)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2405.14831.metadata.json)

PDF bookmarks — [Results (p. 6)](https://arxiv.org/pdf/2405.14831v3#page=6) · [Conclusions & Limitations (p. 10)](https://arxiv.org/pdf/2405.14831v3#page=10).

## Related concepts

- [Long-term memory](../concepts/long-term-memory.md)
- [Memory evaluation](../concepts/memory-evaluation.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md)
- [GraphRAG](../concepts/graph-rag.md)
- [Source-grounded generation](../concepts/grounded-generation.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
