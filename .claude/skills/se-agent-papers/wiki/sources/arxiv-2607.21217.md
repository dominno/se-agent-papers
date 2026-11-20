---
type: source
title: "ICAE-Bench: Evaluating Coding Agents as Interactive Project Builders"
created: 2026-11-19
arxiv_id: "2607.21217"
url: "https://arxiv.org/abs/2607.21217"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "coding-agents", "rag-evaluation", "evaluation-metrics", "llm-as-judge", "benchmarks", "comparison-and-reproducibility"]
source_path: "raw/papers/2607.21217.md"
sources: ["https://arxiv.org/abs/2607.21217"]
ingested: "2026-11-19"
---

# ICAE-Bench: Evaluating Coding Agents as Interactive Project Builders

**Paper:** [2607.21217](https://arxiv.org/abs/2607.21217) · [PDF](https://arxiv.org/pdf/2607.21217) · [HTML](https://arxiv.org/html/2607.21217)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** The authors derived incomplete product descriptions from 480 repositories in 12 languages. The agent can ask a simulated customer up to 16 questions. The main metric is the percentage of test cases passed in a fresh container. [PDF, p. 6](https://arxiv.org/pdf/2607.21217v1#page=6) [PDF, p. 7](https://arxiv.org/pdf/2607.21217v1#page=7) [PDF, p. 8](https://arxiv.org/pdf/2607.21217v1#page=8)

**Key result.** On the full dataset, Opus 4.8 achieved 38.2% and GPT-5.5 achieved 37.2%. Their ranking reversed on Lite. In the GLM-5.1 think-8k experiment, providing ready-made public test files raised the score from 37.4% to 61.8% while the information available through the client stayed the same. [PDF, p. 9](https://arxiv.org/pdf/2607.21217v1#page=9) [PDF, p. 10](https://arxiv.org/pdf/2607.21217v1#page=10)

**Limitations and scope.** Lite contains 50 projects. The ranking of six models correlates with the ranking on the full dataset at ρ ≈ 0.71. The client uses prepared records. Correlations between the judge’s three subjective criteria and mean human ratings range from 0.372 to 0.471. [PDF, p. 6](https://arxiv.org/pdf/2607.21217v1#page=6) [PDF, p. 7](https://arxiv.org/pdf/2607.21217v1#page=7) [PDF, p. 12](https://arxiv.org/pdf/2607.21217v1#page=12)

[Audit of sections, tables and appendices](../reviews/audit-2026-11-19/2607.21217v1.md)

## Overview

The study examines project development through interactions with a user who initially supplies incomplete requirements. [PDF, p. 1](https://arxiv.org/pdf/2607.21217v1#page=1)

## Source files

arXiv version `2607.21217v1` · PDF pages: 23.

- [Original PDF](https://arxiv.org/pdf/2607.21217v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2607.21217.metadata.json)

PDF bookmarks — [Experiments (p. 7)](https://arxiv.org/pdf/2607.21217v1#page=7).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Coding agents](../concepts/coding-agents.md)
- [RAG evaluation](../concepts/rag-evaluation.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [LLM-as-a-Judge](../concepts/llm-as-judge.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
