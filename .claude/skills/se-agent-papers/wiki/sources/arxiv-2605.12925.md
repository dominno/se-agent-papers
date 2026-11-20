---
type: source
title: "AgentLens: Revealing The Lucky Pass Problem in SWE-Agent Evaluation"
created: 2026-11-19
arxiv_id: "2605.12925"
url: "https://arxiv.org/abs/2605.12925"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "coding-agents", "rag-evaluation", "evaluation-metrics", "llm-as-judge", "benchmarks", "comparison-and-reproducibility"]
source_path: "raw/papers/2605.12925.md"
sources: ["https://arxiv.org/abs/2605.12925"]
ingested: "2026-11-19"
---

# AgentLens: Revealing The Lucky Pass Problem in SWE-Agent Evaluation

**Paper:** [2605.12925](https://arxiv.org/abs/2605.12925) · [PDF](https://arxiv.org/pdf/2605.12925) · [HTML](https://arxiv.org/html/2605.12925)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** AgentLens evaluates a trajectory against a tree constructed from other successful solutions to the same task. Its four weights were selected in a separate pilot with 278 trajectories. [PDF, p. 5](https://arxiv.org/pdf/2605.12925v5#page=5) [PDF, p. 6](https://arxiv.org/pdf/2605.12925v5#page=6) [PDF, p. 7](https://arxiv.org/pdf/2605.12925v5#page=7)

**Key result.** Of 1,136 passing trajectories, 122 (10.7%) were classified as Lucky Pass. Excluding valid alternative strategies reduces the share to 9.4%. The share among passing trajectories ranged from 0.5% to 23.2% across configurations. [PDF, p. 8](https://arxiv.org/pdf/2605.12925v5#page=8) [PDF, p. 35](https://arxiv.org/pdf/2605.12925v5#page=35)

**Limitations and scope.** The sample includes 47 of the 60 tasks considered. [PDF, p. 6](https://arxiv.org/pdf/2605.12925v5#page=6) The label captures behavioral similarity and the verification process. Simple individual matching predicts a pass with higher AUROC, 0.805 versus 0.766. [PDF, p. 7](https://arxiv.org/pdf/2605.12925v5#page=7) [PDF, p. 16](https://arxiv.org/pdf/2605.12925v5#page=16) [PDF, p. 25](https://arxiv.org/pdf/2605.12925v5#page=25)

[Audit report for 2605.12925v5](../reviews/audit-2026-11-19/2605.12925v5.md)

## Overview

The study examines apparent successes where tests pass despite problems in the agent's execution trace. [PDF, p. 1](https://arxiv.org/pdf/2605.12925v5#page=1)

## Source files

arXiv version `2605.12925v5` · PDF pages: 36.

- [Original PDF](https://arxiv.org/pdf/2605.12925v5)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2605.12925.metadata.json)

PDF bookmarks — [Results (p. 7)](https://arxiv.org/pdf/2605.12925v5#page=7) · [Limitations, Future Directions, and Positioning (p. 16)](https://arxiv.org/pdf/2605.12925v5#page=16).

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
