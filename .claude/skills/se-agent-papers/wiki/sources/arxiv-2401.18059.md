---
type: source
title: "RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval"
created: 2026-11-19
arxiv_id: "2401.18059"
url: "https://arxiv.org/abs/2401.18059"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["memory-hierarchy", "retrieval-augmented-generation", "hierarchical-retrieval", "clustering", "recursive-summarization", "grounded-generation", "rag-evaluation", "llm-as-judge", "observability", "long-term-memory"]
source_path: "raw/papers/2401.18059.md"
sources: ["https://arxiv.org/abs/2401.18059"]
ingested: "2026-11-19"
---

# RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval

**Paper:** [2401.18059](https://arxiv.org/abs/2401.18059) · [PDF](https://arxiv.org/pdf/2401.18059) · [HTML](https://arxiv.org/html/2401.18059)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** RAPTOR clusters passages by semantic similarity and recursively summarizes the clusters. In the main tests it retrieves nodes from all levels within the same context budget as the competing methods. [PDF, p. 3](https://arxiv.org/pdf/2401.18059v1#page=3) [PDF, p. 4](https://arxiv.org/pdf/2401.18059v1#page=4) [PDF, p. 5](https://arxiv.org/pdf/2401.18059v1#page=5) [PDF, p. 6](https://arxiv.org/pdf/2401.18059v1#page=6)

**Key result.** In the controlled comparison on QuALITY-dev with GPT-3, accuracy was 62.4% for RAPTOR, 60.4% for DPR and 57.3% for BM25. GPT-4 with RAPTOR scored 76.2% in a separate QuALITY-HARD test. [PDF, p. 8](https://arxiv.org/pdf/2401.18059v1#page=8) [PDF, p. 9](https://arxiv.org/pdf/2401.18059v1#page=9)

**Limitations and scope.** The authors selected the retrieval strategy using 20 QASPER documents. On five QuALITY stories, the full tree performed best on three. Manual inspection found unsupported information in six of the 150 summaries examined. [PDF, p. 6](https://arxiv.org/pdf/2401.18059v1#page=6) [PDF, p. 9](https://arxiv.org/pdf/2401.18059v1#page=9) [PDF, p. 17](https://arxiv.org/pdf/2401.18059v1#page=17) [PDF, p. 21](https://arxiv.org/pdf/2401.18059v1#page=21) [PDF, p. 22](https://arxiv.org/pdf/2401.18059v1#page=22)

## Overview

The method builds a hierarchy of summaries and passages to support retrieval at multiple levels of detail. [PDF, p. 1](https://arxiv.org/pdf/2401.18059v1#page=1)

## Section notes

**Mechanism:** RAPTOR clusters text chunks by semantic similarity and recursively summarizes them into a tree that supports retrieval at multiple levels of detail. [PDF, p. 3](https://arxiv.org/pdf/2401.18059v1#page=3) · [PDF, p. 4](https://arxiv.org/pdf/2401.18059v1#page=4)

**Evaluation and study settings:** The comparisons include question answering over long texts and alternative retrieval strategies. [PDF, p. 6](https://arxiv.org/pdf/2401.18059v1#page=6) · [PDF, p. 8](https://arxiv.org/pdf/2401.18059v1#page=8)

**Scope and interpretation:** Generated summaries can omit details. Indexing complexity and the risk of hallucination require separate evaluation. [PDF, p. 15](https://arxiv.org/pdf/2401.18059v1#page=15) · [PDF, p. 17](https://arxiv.org/pdf/2401.18059v1#page=17)

**Sections checked:** 3 Methods, 4 Experiments, A Scalability, E Hallucination Analysis. [Read the paper](https://arxiv.org/html/2401.18059).


[Section and evidence audit](../reviews/audit-2026-11-19/2401.18059v1.md)

## Source files

arXiv version `2401.18059v1` · PDF pages: 23.

- [Original PDF](https://arxiv.org/pdf/2401.18059v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2401.18059.metadata.json)

PDF bookmarks — [Methods (p. 3)](https://arxiv.org/pdf/2401.18059v1#page=3) · [Experiments (p. 6)](https://arxiv.org/pdf/2401.18059v1#page=6).

## Related concepts

- [Memory hierarchy](../concepts/memory-hierarchy.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md)
- [Hierarchical retrieval](../concepts/hierarchical-retrieval.md)
- [Clustering](../concepts/clustering.md)
- [Recursive summarization](../concepts/recursive-summarization.md)
- [Source-grounded generation](../concepts/grounded-generation.md)
- [RAG evaluation](../concepts/rag-evaluation.md)
- [LLM-as-a-Judge](../concepts/llm-as-judge.md)
- [Agent observability](../concepts/observability.md)
- [Long-term memory](../concepts/long-term-memory.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.

## Findings and caveats

- [Finding 1 — method](../concepts/finding-2401-18059-1.md)
- [Finding 2 — evaluation](../concepts/finding-2401-18059-2.md)
- [Finding 3 — interpretive caveat](../concepts/finding-2401-18059-3.md)
