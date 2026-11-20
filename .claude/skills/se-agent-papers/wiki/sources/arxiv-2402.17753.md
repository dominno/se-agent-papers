---
type: source
title: "Evaluating Very Long-Term Conversational Memory of LLM Agents"
created: 2026-11-19
arxiv_id: "2402.17753"
url: "https://arxiv.org/abs/2402.17753"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "long-term-memory", "memory-evaluation", "retrieval-augmented-generation", "grounded-generation", "rag-evaluation", "evaluation-metrics", "llm-as-judge", "benchmarks", "comparison-and-reproducibility"]
source_path: "raw/papers/2402.17753.md"
sources: ["https://arxiv.org/abs/2402.17753"]
ingested: "2026-11-19"
---

# Evaluating Very Long-Term Conversational Memory of LLM Agents

**Paper:** [2402.17753](https://arxiv.org/abs/2402.17753) · [PDF](https://arxiv.org/pdf/2402.17753) · [HTML](https://arxiv.org/html/2402.17753)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** The authors generated 50 English conversations from personas and event graphs, then had people check their consistency. They evaluated question answering, event summarization and image-grounded dialogue generation. [PDF, p. 4](https://arxiv.org/pdf/2402.17753v1#page=4) [PDF, p. 5](https://arxiv.org/pdf/2402.17753v1#page=5) [PDF, p. 6](https://arxiv.org/pdf/2402.17753v1#page=6) [PDF, p. 16](https://arxiv.org/pdf/2402.17753v1#page=16)

**Key result.** Humans achieved an overall F1 of 87.9. For GPT-3.5-turbo-16K, overall F1 rose from 24.1 with a 4K window to 37.8 with a 16K window, while F1 on trick questions fell from 13.1 to 2.1. With five retrieved observations, the model reached 41.4 overall F1. [PDF, p. 7](https://arxiv.org/pdf/2402.17753v1#page=7)

**Limitations and scope.** The conversations are simulated, the images come from the web, and the scoring of short answers depends on wording. One recall@10 cell in Table 3 contains 247.4%, making that value unusable for comparison. [PDF, p. 7](https://arxiv.org/pdf/2402.17753v1#page=7) [PDF, p. 9](https://arxiv.org/pdf/2402.17753v1#page=9)

[Audit of sections, tables and appendices](../reviews/audit-2026-11-19/2402.17753v1.md)

## Overview

LoCoMo is a benchmark of multi-session conversations for evaluating memory and reasoning about events far apart in time. [PDF, p. 1](https://arxiv.org/pdf/2402.17753v1#page=1)

## Source files

arXiv version `2402.17753v1` · PDF pages: 19.

- [Original PDF](https://arxiv.org/pdf/2402.17753v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2402.17753.metadata.json)

PDF bookmarks — [LoCoMo Evaluation Benchmark (p. 5)](https://arxiv.org/pdf/2402.17753v1#page=5) · [Limitations (p. 9)](https://arxiv.org/pdf/2402.17753v1#page=9).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Long-term memory](../concepts/long-term-memory.md)
- [Memory evaluation](../concepts/memory-evaluation.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md)
- [Source-grounded generation](../concepts/grounded-generation.md)
- [RAG evaluation](../concepts/rag-evaluation.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [LLM-as-a-Judge](../concepts/llm-as-judge.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
