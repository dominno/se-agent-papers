---
type: source
title: "Prometheus 2: An Open Source Language Model Specialized in Evaluating Other Language Models"
created: 2026-11-19
arxiv_id: "2405.01535"
url: "https://arxiv.org/abs/2405.01535"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-roles", "citation-grounding", "rag-evaluation", "evaluation-metrics", "llm-as-judge", "benchmarks"]
source_path: "raw/papers/2405.01535.md"
sources: ["https://arxiv.org/abs/2405.01535"]
ingested: "2026-11-19"
---

# Prometheus 2: An Open Source Language Model Specialized in Evaluating Other Language Models

**Paper:** [2405.01535](https://arxiv.org/abs/2405.01535) · [PDF](https://arxiv.org/pdf/2405.01535) · [HTML](https://arxiv.org/html/2405.01535)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** The authors fine-tuned separate models for 1–5 ratings and for selecting the better response under a criterion, then merged the weights. Four benchmarks evaluate absolute scores and four evaluate comparisons. [PDF, p. 3](https://arxiv.org/pdf/2405.01535v2#page=3) [PDF, p. 4](https://arxiv.org/pdf/2405.01535v2#page=4) [PDF, p. 5](https://arxiv.org/pdf/2405.01535v2#page=5)

**Key result.** Across the three pairwise-comparison benchmarks in Table 5, Mixtral averaged 79.15% accuracy after model merging and 75.29% after joint training. On FLASK, Pearson correlation with human judgments was 0.555 for Prometheus 2 8×7B and 0.679 for GPT-4. [PDF, p. 6](https://arxiv.org/pdf/2405.01535v2#page=6) [PDF, p. 8](https://arxiv.org/pdf/2405.01535v2#page=8)

**Limitations and scope.** Agreement with the judge depends on the source of the ratings and whether a reference answer is supplied. Removing it reduced the 8×7B model's correlation with humans on FLASK to 0.411. Tables 3 and 5 give different correlations with GPT-4 on FLASK for the 7B model. [PDF, p. 6](https://arxiv.org/pdf/2405.01535v2#page=6) [PDF, p. 8](https://arxiv.org/pdf/2405.01535v2#page=8) [PDF, p. 9](https://arxiv.org/pdf/2405.01535v2#page=9) [PDF, p. 17](https://arxiv.org/pdf/2405.01535v2#page=17)

[Audit of sections, tables and appendices](../reviews/audit-2026-11-19/2405.01535v2.md)

## Overview

The authors present an open judge model for absolute scoring and pairwise comparisons using user-defined criteria. [PDF, p. 1](https://arxiv.org/pdf/2405.01535v2#page=1)

## Source files

arXiv version `2405.01535v2` · PDF pages: 20.

- [Original PDF](https://arxiv.org/pdf/2405.01535v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2405.01535.metadata.json)

## Related concepts

- [Agent roles](../concepts/agent-roles.md)
- [Citations and supporting evidence](../concepts/citation-grounding.md)
- [RAG evaluation](../concepts/rag-evaluation.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [LLM-as-a-Judge](../concepts/llm-as-judge.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
