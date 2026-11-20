---
type: source
title: "LightRAG: Simple and Fast Retrieval-Augmented Generation"
created: 2026-11-19
arxiv_id: "2410.05779"
url: "https://arxiv.org/abs/2410.05779"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["retrieval-augmented-generation", "graph-rag", "grounded-generation", "rag-evaluation", "llm-as-judge", "long-term-memory"]
source_path: "raw/papers/2410.05779.md"
sources: ["https://arxiv.org/abs/2410.05779"]
ingested: "2026-11-19"
---

# LightRAG: Simple and Fast Retrieval-Augmented Generation

**Paper:** [2410.05779](https://arxiv.org/abs/2410.05779) · [PDF](https://arxiv.org/pdf/2410.05779) · [HTML](https://arxiv.org/html/2410.05779)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** LightRAG indexes entities and relations extracted by an LLM. It combines vector retrieval of entities and topics with graph-neighbor context and source passages. [PDF, p. 3](https://arxiv.org/pdf/2410.05779v3#page=3) [PDF, p. 4](https://arxiv.org/pdf/2410.05779v3#page=4) [PDF, p. 5](https://arxiv.org/pdf/2410.05779v3#page=5)

**Key result.** Against GraphRAG, the GPT-4o-mini judge preferred LightRAG overall in 54.8% of comparisons in Agriculture, 52.0% in CS, 52.8% in Legal and 49.6% in Mix. Each domain had 125 questions generated using the same procedure. [PDF, p. 6](https://arxiv.org/pdf/2410.05779v3#page=6) [PDF, p. 7](https://arxiv.org/pdf/2410.05779v3#page=7)

**Limitations and scope.** The judge evaluated pairs of answers without a reference answer or a separate source-retrieval metric. In Table 3, both answers discuss movie-recommendation metrics, although the question asks about feature normalization. The answers match the question in appendix Figure 3. [PDF, p. 6](https://arxiv.org/pdf/2410.05779v3#page=6) [PDF, p. 9](https://arxiv.org/pdf/2410.05779v3#page=9) [PDF, p. 13](https://arxiv.org/pdf/2410.05779v3#page=13)

[Audit of sections, tables and appendices](../reviews/audit-2026-11-19/2410.05779v3.md)

## Overview

The method combines a relationship graph and vector representations with two-level retrieval and incremental index updates. [PDF, p. 1](https://arxiv.org/pdf/2410.05779v3#page=1)

## Source files

arXiv version `2410.05779v3` · PDF pages: 16.

- [Original PDF](https://arxiv.org/pdf/2410.05779v3)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2410.05779.metadata.json)

PDF bookmarks — [Evaluation (p. 5)](https://arxiv.org/pdf/2410.05779v3#page=5).

## Related concepts

- [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md)
- [GraphRAG](../concepts/graph-rag.md)
- [Source-grounded generation](../concepts/grounded-generation.md)
- [RAG evaluation](../concepts/rag-evaluation.md)
- [LLM-as-a-Judge](../concepts/llm-as-judge.md)
- [Long-term memory](../concepts/long-term-memory.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
