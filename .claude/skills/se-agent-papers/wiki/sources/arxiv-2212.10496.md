---
type: source
title: "Precise Zero-Shot Dense Retrieval without Relevance Labels"
created: 2026-11-19
arxiv_id: "2212.10496"
url: "https://arxiv.org/abs/2212.10496"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["retrieval-augmented-generation", "dense-retrieval", "knowledge-graph", "entity-extraction", "grounded-generation", "rag-evaluation", "llm-as-judge"]
source_path: "raw/papers/2212.10496.md"
sources: ["https://arxiv.org/abs/2212.10496"]
ingested: "2026-11-19"
---

# Precise Zero-Shot Dense Retrieval without Relevance Labels

**Paper:** [2212.10496](https://arxiv.org/abs/2212.10496) · [PDF](https://arxiv.org/pdf/2212.10496) · [HTML](https://arxiv.org/html/2212.10496)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** HyDE generates hypothetical documents from the question and a domain-specific instruction, averages their Contriever or mContriever representations, and retrieves similar real documents. It uses pretrained weights. [PDF, p. 2](https://arxiv.org/pdf/2212.10496v1#page=2) [PDF, p. 3](https://arxiv.org/pdf/2212.10496v1#page=3) [PDF, p. 4](https://arxiv.org/pdf/2212.10496v1#page=4) [PDF, p. 11](https://arxiv.org/pdf/2212.10496v1#page=11)

**Key result.** In the tables, HyDE outperformed the corresponding base encoder on both TREC DL years, six BEIR tasks and four Mr.TyDi languages. For nDCG@10, DL19 rose from 44.5 to 61.3 and DL20 from 42.1 to 57.9. Page 2 lists 11 datasets, although the tables show 12 task comparisons. [PDF, p. 2](https://arxiv.org/pdf/2212.10496v1#page=2) [PDF, p. 5](https://arxiv.org/pdf/2212.10496v1#page=5) [PDF, p. 6](https://arxiv.org/pdf/2212.10496v1#page=6)

**Limitations and scope.** The hypothetical document may contain errors, and averaging representations assumes an unambiguous query. On TREC-COVID, BM25 outperformed HyDE on both nDCG@10 and Recall@100. [PDF, p. 2](https://arxiv.org/pdf/2212.10496v1#page=2) [PDF, p. 4](https://arxiv.org/pdf/2212.10496v1#page=4) [PDF, p. 5](https://arxiv.org/pdf/2212.10496v1#page=5)

## Overview

HyDE generates a hypothetical document, embeds it and retrieves real documents without using relevance labels. [PDF, p. 1](https://arxiv.org/pdf/2212.10496v1#page=1)

[Section and evidence audit](../reviews/audit-2026-11-19/2212.10496v1.md)

## Source files

arXiv version `2212.10496v1` · PDF pages: 11.

- [Original PDF](https://arxiv.org/pdf/2212.10496v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2212.10496.metadata.json)

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
