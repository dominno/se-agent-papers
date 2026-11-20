---
type: source
title: "RAGBench: Explainable Benchmark for Retrieval-Augmented Generation Systems"
created: 2026-11-19
arxiv_id: "2407.11005"
url: "https://arxiv.org/abs/2407.11005"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["retrieval-augmented-generation", "grounded-generation", "rag-evaluation", "evaluation-metrics", "llm-as-judge", "benchmarks", "comparison-and-reproducibility"]
source_path: "raw/papers/2407.11005.md"
sources: ["https://arxiv.org/abs/2407.11005"]
ingested: "2026-11-19"
---

# RAGBench: Explainable Benchmark for Retrieval-Augmented Generation Systems

**Paper:** [2407.11005](https://arxiv.org/abs/2407.11005) · [PDF](https://arxiv.org/pdf/2407.11005) · [HTML](https://arxiv.org/html/2407.11005)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** RAGBench provides approximately 100,000 examples from five domains. TRACe evaluates distinct properties of the response and the retrieved context. [PDF, p. 1](https://arxiv.org/pdf/2407.11005v2#page=1)

**Key result.** Fine-tuned DeBERTa achieved the highest AUROC for hallucination detection on 11 of 12 datasets, with scores of 0.64–0.87. On DelucionQA, RAGAS reached 0.70 versus 0.64 for DeBERTa. The abstract names RoBERTa, while the experimental configuration and Table 3 identify DeBERTa. [PDF, p. 1](https://arxiv.org/pdf/2407.11005v2#page=1) [PDF, p. 8](https://arxiv.org/pdf/2407.11005v2#page=8) [PDF, p. 9](https://arxiv.org/pdf/2407.11005v2#page=9)

**Limitations and scope.** In the experiments, instruction wording alone changed context use and answer completeness. Comparisons must account for the generator configuration. [PDF, p. 8](https://arxiv.org/pdf/2407.11005v2#page=8)

[Audit report for 2407.11005v2](../reviews/audit-2026-11-19/2407.11005v2.md)

## Overview

The dataset provides cases and interpretable labels for assessing whether retrieved evidence supports an answer. [PDF, p. 1](https://arxiv.org/pdf/2407.11005v2#page=1)

## Source files

arXiv version `2407.11005v2` · PDF pages: 21.

- [Original PDF](https://arxiv.org/pdf/2407.11005v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2407.11005.metadata.json)

PDF bookmarks — [Experiments (p. 8)](https://arxiv.org/pdf/2407.11005v2#page=8).

## Related concepts

- [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md)
- [Source-grounded generation](../concepts/grounded-generation.md)
- [RAG evaluation](../concepts/rag-evaluation.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [LLM-as-a-Judge](../concepts/llm-as-judge.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
