---
type: source
title: "CRAG -- Comprehensive RAG Benchmark"
created: 2026-11-19
arxiv_id: "2406.04744"
url: "https://arxiv.org/abs/2406.04744"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["retrieval-augmented-generation", "grounded-generation", "evaluation-metrics", "benchmarks", "stateful-tool-use", "tool-evaluation", "comparison-and-reproducibility", "long-term-memory"]
source_path: "raw/papers/2406.04744.md"
sources: ["https://arxiv.org/abs/2406.04744"]
ingested: "2026-11-19"
---

# CRAG -- Comprehensive RAG Benchmark

**Paper:** [2406.04744](https://arxiv.org/abs/2406.04744) · [PDF](https://arxiv.org/pdf/2406.04744) · [HTML](https://arxiv.org/html/2406.04744)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** The authors prepared 4,409 English-language questions in five domains. Using the 1,335 public test questions, they compared a retrieval-free baseline with three configurations using archived web pages and simulated knowledge graphs. [PDF, p. 4](https://arxiv.org/pdf/2406.04744v2#page=4) [PDF, p. 5](https://arxiv.org/pdf/2406.04744v2#page=5) [PDF, p. 7](https://arxiv.org/pdf/2406.04744v2#page=7)

**Key result.** For GPT-4 Turbo, the accepted-answer rate rose from 33.5% without RAG to 43.6% on Task 3. Incorrect answers rose from 13.5% to 30.1%, so the error-penalized score fell from 20.0 to 13.4. [PDF, p. 7](https://arxiv.org/pdf/2406.04744v2#page=7) [PDF, p. 8](https://arxiv.org/pdf/2406.04744v2#page=8)

**Limitations and scope.** The benchmark supplies the initial pool of pages. Humans rated the industrial systems. Two models rated the simpler configurations, using different scoring rules for partially correct answers. [PDF, p. 7](https://arxiv.org/pdf/2406.04744v2#page=7) [PDF, p. 8](https://arxiv.org/pdf/2406.04744v2#page=8) [PDF, p. 9](https://arxiv.org/pdf/2406.04744v2#page=9) [PDF, p. 20](https://arxiv.org/pdf/2406.04744v2#page=20)

[Audit of sections, tables and appendices](../reviews/audit-2026-11-19/2406.04744v2.md)

## Overview

The benchmark provides diverse questions, answers and simulated APIs for evaluating factual accuracy in RAG systems. [PDF, p. 1](https://arxiv.org/pdf/2406.04744v2#page=1)

## Source files

arXiv version `2406.04744v2` · PDF pages: 20.

- [Original PDF](https://arxiv.org/pdf/2406.04744v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2406.04744.metadata.json)

PDF bookmarks — [Metrics and Evaluation (p. 6)](https://arxiv.org/pdf/2406.04744v2#page=6).

## Related concepts

- [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md)
- [Source-grounded generation](../concepts/grounded-generation.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Stateful tool use](../concepts/stateful-tool-use.md)
- [Tool evaluation](../concepts/tool-evaluation.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)
- [Long-term memory](../concepts/long-term-memory.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
