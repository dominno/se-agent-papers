---
type: source
title: "Ragas: Automated Evaluation of Retrieval Augmented Generation"
created: 2026-11-19
arxiv_id: "2309.15217"
url: "https://arxiv.org/abs/2309.15217"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["retrieval-augmented-generation", "grounded-generation", "rag-evaluation", "evaluation-metrics", "llm-as-judge", "benchmarks", "comparison-and-reproducibility"]
source_path: "raw/papers/2309.15217.md"
sources: ["https://arxiv.org/abs/2309.15217"]
ingested: "2026-11-19"
---

# Ragas: Automated Evaluation of Retrieval Augmented Generation

**Paper:** [2309.15217](https://arxiv.org/abs/2309.15217) · [PDF](https://arxiv.org/pdf/2309.15217) · [HTML](https://arxiv.org/html/2309.15217)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** Ragas decomposes an answer into claims checked against the context, compares questions using embeddings, and measures the share of context sentences needed to answer. The authors assess agreement with human judgments on WikiEval. [PDF, p. 3](https://arxiv.org/pdf/2309.15217v2#page=3) [PDF, p. 4](https://arxiv.org/pdf/2309.15217v2#page=4)

**Key result.** On WikiEval, Ragas agreed with humans on the preferred item in 0.95 of pairs for answer faithfulness, 0.78 for answer relevance and 0.70 for context relevance. Direct GPT ranking achieved 0.54, 0.40 and 0.52, respectively. [PDF, p. 5](https://arxiv.org/pdf/2309.15217v2#page=5)

**Limitations and scope.** This validation measures which of two items a judge prefers. Preference agreement does not establish that absolute quality scores are calibrated. [PDF, p. 5](https://arxiv.org/pdf/2309.15217v2#page=5)

[Audit report for 2309.15217v2](../reviews/audit-2026-11-19/2309.15217v2.md)

## Overview

The authors define metrics for retrieval, faithfulness to context and generation quality that do not require exhaustive human annotation. [PDF, p. 1](https://arxiv.org/pdf/2309.15217v2#page=1)

## Source files

arXiv version `2309.15217v2` · PDF pages: 8.

- [Original PDF](https://arxiv.org/pdf/2309.15217v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2309.15217.metadata.json)

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
