---
type: source
title: "Dense Passage Retrieval for Open-Domain Question Answering"
created: 2026-11-19
arxiv_id: "2004.04906"
url: "https://arxiv.org/abs/2004.04906"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["coding-agents", "retrieval-augmented-generation", "dense-retrieval", "knowledge-graph", "entity-extraction", "grounded-generation", "rag-evaluation", "llm-as-judge"]
source_path: "raw/papers/2004.04906.md"
sources: ["https://arxiv.org/abs/2004.04906"]
ingested: "2026-11-19"
---

# Dense Passage Retrieval for Open-Domain Question Answering

**Paper:** [2004.04906](https://arxiv.org/abs/2004.04906) · [PDF](https://arxiv.org/pdf/2004.04906) · [HTML](https://arxiv.org/html/2004.04906)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** Two separate BERT-base encoders represent questions and passages from English Wikipedia. DPR ranks candidates by dot product. A top-20 hit means at least one of the first 20 passages contains the answer. [PDF, p. 2](https://arxiv.org/pdf/2004.04906v3#page=2) [PDF, p. 3](https://arxiv.org/pdf/2004.04906v3#page=3) [PDF, p. 4](https://arxiv.org/pdf/2004.04906v3#page=4)

**Key result.** In Table 2, DPR trained separately on each dataset exceeds Lucene-BM25 in top-20 retrieval accuracy by 19.3 percentage points on NQ, 12.5 on TriviaQA, 18.2 on WebQuestions and 8.9 on TREC. On SQuAD, DPR reaches 63.2% versus 68.8% for BM25 (−5.6 points). [PDF, p. 5](https://arxiv.org/pdf/2004.04906v3#page=5)

**Limitations and scope.** The collection uses English Wikipedia and excludes tables and lists. SQuAD questions were written with the paragraph visible, which the authors argue favors lexical overlap between question and passage. [PDF, p. 4](https://arxiv.org/pdf/2004.04906v3#page=4) [PDF, p. 5](https://arxiv.org/pdf/2004.04906v3#page=5)

[Audit of sections, tables and appendices](../reviews/audit-2026-11-19/2004.04906v3.md)

## Overview

A dual encoder produces dense representations of questions and passages for retrieval over open-domain document collections. [PDF, p. 1](https://arxiv.org/pdf/2004.04906v3#page=1)

## Source files

arXiv version `2004.04906v3` · PDF pages: 13.

- [Original PDF](https://arxiv.org/pdf/2004.04906v3)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2004.04906.metadata.json)

## Related concepts

- [Coding agents](../concepts/coding-agents.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md)
- [Dense retrieval](../concepts/dense-retrieval.md)
- [Knowledge graph](../concepts/knowledge-graph.md)
- [Entity extraction](../concepts/entity-extraction.md)
- [Source-grounded generation](../concepts/grounded-generation.md)
- [RAG evaluation](../concepts/rag-evaluation.md)
- [LLM-as-a-Judge](../concepts/llm-as-judge.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
