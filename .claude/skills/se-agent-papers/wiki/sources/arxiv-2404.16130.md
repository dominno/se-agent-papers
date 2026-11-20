---
type: source
title: "From Local to Global: A Graph RAG Approach to Query-Focused Summarization"
created: 2026-11-19
arxiv_id: "2404.16130"
url: "https://arxiv.org/abs/2404.16130"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["retrieval-augmented-generation", "graph-rag", "knowledge-graph", "entity-extraction", "community-summarization", "recursive-summarization", "grounded-generation", "long-term-memory"]
source_path: "raw/papers/2404.16130.md"
sources: ["https://arxiv.org/abs/2404.16130"]
ingested: "2026-11-19"
---

# From Local to Global: A Graph RAG Approach to Query-Focused Summarization

**Paper:** [2404.16130](https://arxiv.org/abs/2404.16130) · [PDF](https://arxiv.org/pdf/2404.16130) · [HTML](https://arxiv.org/html/2404.16130)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** GraphRAG builds an entity graph from documents and summarizes its communities. It combines partial responses to a global question into a final answer. [PDF, p. 4](https://arxiv.org/pdf/2404.16130v2#page=4)

**Key result.** For cross-cutting news questions, the highest C0 summary level yielded a mean of 34.18 claims per answer versus 25.23 for vector RAG. For podcasts the figures were 32.21 versus 26.50. The study counted distinct claims and assessed judge preference separately. [PDF, p. 9](https://arxiv.org/pdf/2404.16130v2#page=9) [PDF, p. 10](https://arxiv.org/pdf/2404.16130v2#page=10) [PDF, p. 11](https://arxiv.org/pdf/2404.16130v2#page=11)

**Limitations and scope.** The evaluation covers two selected corpora. The finding concerns questions about a collection as a whole and does not establish an advantage for single-fact retrieval. [PDF, p. 8](https://arxiv.org/pdf/2404.16130v2#page=8)

[Audit report for 2404.16130v2](../reviews/audit-2026-11-19/2404.16130v2.md)

## Overview

The method builds an entity graph and summarizes graph communities to answer questions that span a large text collection. [PDF, p. 1](https://arxiv.org/pdf/2404.16130v2#page=1)

## Section notes

**Mechanism:** Indexing extracts entities and relations from text chunks to build a graph. Graph communities are summarized, and partial answers are combined into a global response. [PDF, p. 4](https://arxiv.org/pdf/2404.16130v2#page=4) · [PDF, p. 5](https://arxiv.org/pdf/2404.16130v2#page=5)

**Evaluation and study settings:** The authors evaluated global sensemaking questions on two large corpora, using pairwise LLM judgments and extracted claims. [PDF, p. 8](https://arxiv.org/pdf/2404.16130v2#page=8) · [PDF, p. 9](https://arxiv.org/pdf/2404.16130v2#page=9)

**Scope and interpretation:** The authors note that the study covers two corpora of roughly one million tokens each and call for evaluation in other domains and measures of fabricated content. [PDF, p. 11](https://arxiv.org/pdf/2404.16130v2#page=11)

**Sections checked:** 3 Methods, 5 Results, 6.1 Limitations of evaluation approach. [Read the paper](https://arxiv.org/html/2404.16130).


## Source files

arXiv version `2404.16130v2` · PDF pages: 26.

- [Original PDF](https://arxiv.org/pdf/2404.16130v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2404.16130.metadata.json)

PDF bookmarks — [Methods (p. 4)](https://arxiv.org/pdf/2404.16130v2#page=4) · [Results (p. 9)](https://arxiv.org/pdf/2404.16130v2#page=9).

## Related concepts

- [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md)
- [GraphRAG](../concepts/graph-rag.md)
- [Knowledge graph](../concepts/knowledge-graph.md)
- [Entity extraction](../concepts/entity-extraction.md)
- [Graph community summarization](../concepts/community-summarization.md)
- [Recursive summarization](../concepts/recursive-summarization.md)
- [Source-grounded generation](../concepts/grounded-generation.md)
- [Long-term memory](../concepts/long-term-memory.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.

## Findings and caveats

- [Finding 1 — method](../concepts/finding-2404-16130-1.md)
- [Finding 2 — evaluation](../concepts/finding-2404-16130-2.md)
- [Finding 3 — interpretive caveat](../concepts/finding-2404-16130-3.md)
