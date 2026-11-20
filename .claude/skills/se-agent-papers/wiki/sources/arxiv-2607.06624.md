---
type: source
title: "AgentLens: Production-Assessed Trajectory Reviews for Coding Agent Evaluation"
created: 2026-11-19
arxiv_id: "2607.06624"
url: "https://arxiv.org/abs/2607.06624"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "coding-agents", "rag-evaluation", "evaluation-metrics", "llm-as-judge", "benchmarks", "comparison-and-reproducibility"]
source_path: "raw/papers/2607.06624.md"
sources: ["https://arxiv.org/abs/2607.06624"]
ingested: "2026-11-19"
---

# AgentLens: Production-Assessed Trajectory Reviews for Coding Agent Evaluation

**Paper:** [2607.06624](https://arxiv.org/abs/2607.06624) · [PDF](https://arxiv.org/pdf/2607.06624) · [Read the article online](https://arxiv.org/pdf/2607.06624v2)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** For 16 Java scenarios with two user profiles per scenario, AgentLens combines a set of formal checks with five assessments by a model that reads the execution trace. QI is the mean of the six components. [PDF, p. 3](https://arxiv.org/pdf/2607.06624v2#page=3) [PDF, p. 4](https://arxiv.org/pdf/2607.06624v2#page=4) [PDF, p. 5](https://arxiv.org/pdf/2607.06624v2#page=5)

**Key result.** In Table 6, EAA and Claude Code (xhigh), both using Opus 4.7, passed all formal checks on 81.2% of scenarios. Their quality indices were 81.5 and 76.2, respectively. [PDF, p. 4](https://arxiv.org/pdf/2607.06624v2#page=4) [PDF, p. 10](https://arxiv.org/pdf/2607.06624v2#page=10)

**Limitations and scope.** The sample covers only Java. For 16 of the 32 cases, repeated GLM-5.1 runs produced both passes and failures. With external APIs, provider versions and throughput may affect whether runs finish within the time limit. [PDF, p. 3](https://arxiv.org/pdf/2607.06624v2#page=3) [PDF, p. 7](https://arxiv.org/pdf/2607.06624v2#page=7) [PDF, p. 12](https://arxiv.org/pdf/2607.06624v2#page=12) [PDF, p. 13](https://arxiv.org/pdf/2607.06624v2#page=13)

## Overview

The study evaluates the quality of a coding agent's execution trace alongside its final result. [PDF, p. 1](https://arxiv.org/pdf/2607.06624v2#page=1)

[Section and evidence audit](../reviews/audit-2026-11-19/2607.06624v2.md)

## Source files

arXiv version `2607.06624v2` · PDF pages: 30.

- [Original PDF](https://arxiv.org/pdf/2607.06624v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2607.06624.metadata.json)

PDF bookmarks — [Evaluation (p. 9)](https://arxiv.org/pdf/2607.06624v2#page=9) · [Limitations (p. 12)](https://arxiv.org/pdf/2607.06624v2#page=12).

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
