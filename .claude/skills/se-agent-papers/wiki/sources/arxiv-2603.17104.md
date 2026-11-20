---
type: source
title: "When the Specification Emerges: Benchmarking Faithfulness Loss in Long-Horizon Coding Agents"
created: 2026-11-19
arxiv_id: "2603.17104"
url: "https://arxiv.org/abs/2603.17104"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "task-planning", "coding-agents", "context-window", "grounded-generation", "evaluation-metrics", "benchmarks", "long-horizon-development", "comparison-and-reproducibility"]
source_path: "raw/papers/2603.17104.md"
sources: ["https://arxiv.org/abs/2603.17104"]
ingested: "2026-11-19"
---

# When the Specification Emerges: Benchmarking Faithfulness Loss in Long-Horizon Coding Agents

**Paper:** [2603.17104](https://arxiv.org/abs/2603.17104) · [PDF](https://arxiv.org/pdf/2603.17104) · [HTML](https://arxiv.org/html/2603.17104)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** Across 20 ML papers and two platforms, the study compared implementing requirements disclosed in stages with implementing a full specification supplied at the outset. IF50 averages normalized fidelity across 371 components and a code integration metric. [PDF, p. 2](https://arxiv.org/pdf/2603.17104v1#page=2) [PDF, p. 4](https://arxiv.org/pdf/2603.17104v1#page=4) [PDF, p. 5](https://arxiv.org/pdf/2603.17104v1#page=5) [PDF, p. 6](https://arxiv.org/pdf/2603.17104v1#page=6)

**Key result.** On Claude Code, ProjectGuard closed about 90% of the gap in aggregate MCF semantic fidelity (2.718 → 3.000 against a reference of 3.031). The mean of the recovery percentages computed separately for individual papers is 51%. These aggregates use different weighting, and neither measures a 90% recovery in the primary IF50 metric. [PDF, p. 6](https://arxiv.org/pdf/2603.17104v1#page=6) [PDF, p. 8](https://arxiv.org/pdf/2603.17104v1#page=8) [PDF, p. 17](https://arxiv.org/pdf/2603.17104v1#page=17) [PDF, p. 18](https://arxiv.org/pdf/2603.17104v1#page=18)

**Limitations and scope.** The sample consists of synthetic sequences from 20 machine-learning papers and two platforms. On Codex, the MCF difference is already negligible without intervention, although code integration still measurably deteriorates. [PDF, p. 6](https://arxiv.org/pdf/2603.17104v1#page=6) [PDF, p. 8](https://arxiv.org/pdf/2603.17104v1#page=8) [PDF, p. 9](https://arxiv.org/pdf/2603.17104v1#page=9)

## Overview

The evaluation tests whether agents satisfy requirements revealed incrementally during long coding sessions. [PDF, p. 1](https://arxiv.org/pdf/2603.17104v1#page=1)

[Section and evidence audit](../reviews/audit-2026-11-19/2603.17104v1.md)

## Source files

arXiv version `2603.17104v1` · PDF pages: 19.

- [Original PDF](https://arxiv.org/pdf/2603.17104v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2603.17104.metadata.json)

PDF bookmarks — [Experiments (p. 5)](https://arxiv.org/pdf/2603.17104v1#page=5).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Task planning](../concepts/task-planning.md)
- [Coding agents](../concepts/coding-agents.md)
- [Context window](../concepts/context-window.md)
- [Source-grounded generation](../concepts/grounded-generation.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Long-term software evolution](../concepts/long-horizon-development.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
