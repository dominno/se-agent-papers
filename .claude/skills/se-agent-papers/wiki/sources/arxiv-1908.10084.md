---
type: source
title: "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks"
created: 2026-11-19
arxiv_id: "1908.10084"
url: "https://arxiv.org/abs/1908.10084"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["retrieval-augmented-generation", "dense-retrieval", "knowledge-graph", "entity-extraction", "grounded-generation", "rag-evaluation", "llm-as-judge"]
source_path: "raw/papers/1908.10084.md"
sources: ["https://arxiv.org/abs/1908.10084"]
ingested: "2026-11-19"
---

# Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks

**Paper:** [1908.10084](https://arxiv.org/abs/1908.10084) · [PDF](https://arxiv.org/pdf/1908.10084) · [HTML](https://arxiv.org/html/1908.10084)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** Sentence-BERT learns sentence representations with a Siamese or triplet architecture. Once computed, the embeddings can be compared by cosine similarity. [PDF, p. 1](https://arxiv.org/pdf/1908.10084v1#page=1)

**Key result.** For 10,000 sentences, the authors report about 65 hours for BERT pairwise comparisons, versus about 5 seconds to compute SBERT vectors and 0.01 seconds for similarities. Table 7 independently implies about 4.9 s for encoding alone, at 2,042 sentences/s on a Tesla V100. [PDF, p. 2](https://arxiv.org/pdf/1908.10084v1#page=2) [PDF, p. 8](https://arxiv.org/pdf/1908.10084v1#page=8)

**Limitations and scope.** The speedup applies to repeated comparisons within a collection. It does not provide a general speedup factor for scoring a single pair. [PDF, p. 2](https://arxiv.org/pdf/1908.10084v1#page=2)

[Audit report for 1908.10084v1](../reviews/audit-2026-11-19/1908.10084v1.md)

## Overview

BERT trained with a Siamese or triplet architecture produces sentence embeddings that can be compared by cosine similarity for semantic search. [PDF, p. 1](https://arxiv.org/pdf/1908.10084v1#page=1)

## Source files

arXiv version `1908.10084v1` · PDF pages: 11.

- [Original PDF](https://arxiv.org/pdf/1908.10084v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/1908.10084.metadata.json)

## Related concepts

- [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md)
- [Dense retrieval](../concepts/dense-retrieval.md)
- [Knowledge graph](../concepts/knowledge-graph.md)
- [Entity extraction](../concepts/entity-extraction.md)
- [Source-grounded generation](../concepts/grounded-generation.md)
- [RAG evaluation](../concepts/rag-evaluation.md)
- [LLM-as-a-Judge](../concepts/llm-as-judge.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
