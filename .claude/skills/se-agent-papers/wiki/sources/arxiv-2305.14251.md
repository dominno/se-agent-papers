---
type: source
title: "FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation"
created: 2026-11-19
arxiv_id: "2305.14251"
url: "https://arxiv.org/abs/2305.14251"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["citation-grounding", "citation-precision", "claim-verification", "rag-evaluation", "evaluation-metrics", "llm-as-judge", "benchmarks", "comparison-and-reproducibility"]
source_path: "raw/papers/2305.14251.md"
sources: ["https://arxiv.org/abs/2305.14251"]
ingested: "2026-11-19"
---

# FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation

**Paper:** [2305.14251](https://arxiv.org/abs/2305.14251) · [PDF](https://arxiv.org/pdf/2305.14251) · [HTML](https://arxiv.org/html/2305.14251)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** For each answer, the authors measure the fraction of atomic claims supported by the source, then average those fractions across answers. They compare human evaluation of biographies with automated retrieval and classification. [PDF, p. 3](https://arxiv.org/pdf/2305.14251v2#page=3) [PDF, p. 4](https://arxiv.org/pdf/2305.14251v2#page=4) [PDF, p. 6](https://arxiv.org/pdf/2305.14251v2#page=6) [PDF, p. 7](https://arxiv.org/pdf/2305.14251v2#page=7)

**Key result.** Human raters scored InstructGPT at 42.5%, ChatGPT at 58.3% and PerplexityAI at 71.5%. One estimator preserved this ranking, with respective errors of 1.4, 0.4 and 9.9 points. [PDF, p. 4](https://arxiv.org/pdf/2305.14251v2#page=4) [PDF, p. 7](https://arxiv.org/pdf/2305.14251v2#page=7)

**Limitations and scope.** The metric omits missing information and depends on the reference source. In three of 30 cases that lacked support in Wikipedia, reviewers found support elsewhere. [PDF, p. 10](https://arxiv.org/pdf/2305.14251v2#page=10) [PDF, p. 16](https://arxiv.org/pdf/2305.14251v2#page=16) [PDF, p. 17](https://arxiv.org/pdf/2305.14251v2#page=17)

[Audit of sections, tables and appendices](../reviews/audit-2026-11-19/2305.14251v2.md)

## Overview

The method decomposes long answers into atomic facts and measures the proportion supported by a trusted source. [PDF, p. 1](https://arxiv.org/pdf/2305.14251v2#page=1)

## Source files

arXiv version `2305.14251v2` · PDF pages: 25.

- [Original PDF](https://arxiv.org/pdf/2305.14251v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2305.14251.metadata.json)

## Related concepts

- [Citations and supporting evidence](../concepts/citation-grounding.md)
- [Citation precision](../concepts/citation-precision.md)
- [Claim verification](../concepts/claim-verification.md)
- [RAG evaluation](../concepts/rag-evaluation.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [LLM-as-a-Judge](../concepts/llm-as-judge.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
