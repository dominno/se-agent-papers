---
type: source
title: "Corrective Retrieval Augmented Generation"
created: 2026-11-19
arxiv_id: "2401.15884"
url: "https://arxiv.org/abs/2401.15884"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["retrieval-augmented-generation", "knowledge-graph", "entity-extraction", "grounded-generation", "rag-evaluation", "llm-as-judge"]
source_path: "raw/papers/2401.15884.md"
sources: ["https://arxiv.org/abs/2401.15884"]
ingested: "2026-11-19"
---

# Corrective Retrieval Augmented Generation

**Paper:** [2401.15884](https://arxiv.org/abs/2401.15884) · [PDF](https://arxiv.org/pdf/2401.15884) · [HTML](https://arxiv.org/html/2401.15884)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** A fine-tuned T5-large scores each question–document pair for relevance. The maximum score and two thresholds determine whether to filter corpus evidence, search the web, or combine both sources. [PDF, p. 4](https://arxiv.org/pdf/2401.15884v3#page=4) [PDF, p. 5](https://arxiv.org/pdf/2401.15884v3#page=5) [PDF, p. 6](https://arxiv.org/pdf/2401.15884v3#page=6)

**Key result.** In Table 1, CRAG outperforms standard RAG on four datasets with both generators. With SelfRAG-LLaMA2-7b, gains range from 7.0 accuracy points on PopQA to 36.6 on PubHealth. Comparing Self-CRAG with Self-RAG, however, yields −0.1 points on ARC for that generator and −0.1 on PubHealth for LLaMA2-hf-7b. [PDF, p. 7](https://arxiv.org/pdf/2401.15884v3#page=7)

**Limitations and scope.** Thresholds were fitted empirically for particular datasets, and the evaluator was trained on PopQA. The compute-cost table excludes retrieval and source processing, so it does not establish end-to-end query latency. [PDF, p. 10](https://arxiv.org/pdf/2401.15884v3#page=10) [PDF, p. 15](https://arxiv.org/pdf/2401.15884v3#page=15)

[Audit of sections, tables and appendices](../reviews/audit-2026-11-19/2401.15884v3.md)

## Overview

CRAG assesses retrieved documents and takes corrective action when the retrieved evidence is of poor quality. [PDF, p. 1](https://arxiv.org/pdf/2401.15884v3#page=1)

## Source files

arXiv version `2401.15884v3` · PDF pages: 16.

- [Original PDF](https://arxiv.org/pdf/2401.15884v3)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2401.15884.metadata.json)

PDF bookmarks — [Experiments (p. 6)](https://arxiv.org/pdf/2401.15884v3#page=6).

## Related concepts

- [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md)
- [Knowledge graph](../concepts/knowledge-graph.md)
- [Entity extraction](../concepts/entity-extraction.md)
- [Source-grounded generation](../concepts/grounded-generation.md)
- [RAG evaluation](../concepts/rag-evaluation.md)
- [LLM-as-a-Judge](../concepts/llm-as-judge.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
