---
type: source
title: "SWE-Chain: Benchmarking Coding Agents on Chained Release-Level Package Upgrades"
created: 2026-11-19
arxiv_id: "2605.14415"
url: "https://arxiv.org/abs/2605.14415"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "coding-agents", "evaluation-metrics", "benchmarks", "long-horizon-development", "regression-testing", "comparison-and-reproducibility"]
source_path: "raw/papers/2605.14415.md"
sources: ["https://arxiv.org/abs/2605.14415"]
ingested: "2026-11-19"
---

# SWE-Chain: Benchmarking Coding Agents on Chained Release-Level Package Upgrades

**Paper:** [2605.14415](https://arxiv.org/abs/2605.14415) · [PDF](https://arxiv.org/pdf/2605.14415) · [HTML](https://arxiv.org/html/2605.14415)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** The agent applies each successive package update to its own output from the previous stage. Specifications are derived from release notes and code diffs. Evaluation distinguishes passing update-related tests from regressions in previously passing tests. [PDF, p. 3](https://arxiv.org/pdf/2605.14415v1#page=3) [PDF, p. 4](https://arxiv.org/pdf/2605.14415v1#page=4) [PDF, p. 5](https://arxiv.org/pdf/2605.14415v1#page=5) [PDF, p. 6](https://arxiv.org/pdf/2605.14415v1#page=6)

**Key result.** In Build+Fix mode, Claude Code with Opus 4.7 averaged 60.8% on the resolving metric for update-related tests, 80.6% precision and 68.5% F1. The final test pass rate was 91.9%. [PDF, p. 5](https://arxiv.org/pdf/2605.14415v1#page=5) [PDF, p. 6](https://arxiv.org/pdf/2605.14415v1#page=6)

**Limitations and scope.** The authors did not obtain human ratings of specification quality for the 155 release transitions and 1,660 tasks. They studied 12 Python package chains and did not repeat the main agent runs because of cost. [PDF, p. 16](https://arxiv.org/pdf/2605.14415v1#page=16) [PDF, p. 37](https://arxiv.org/pdf/2605.14415v1#page=37)

## Overview

The benchmark tests whether agents maintain quality across related software updates and successive releases. [PDF, p. 1](https://arxiv.org/pdf/2605.14415v1#page=1)

[Section and evidence audit](../reviews/audit-2026-11-19/2605.14415v1.md)

## Source files

arXiv version `2605.14415v1` · PDF pages: 37.

- [Original PDF](https://arxiv.org/pdf/2605.14415v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2605.14415.metadata.json)

PDF bookmarks — [Results (p. 6)](https://arxiv.org/pdf/2605.14415v1#page=6) · [Limitations (p. 37)](https://arxiv.org/pdf/2605.14415v1#page=37).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Coding agents](../concepts/coding-agents.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Long-term software evolution](../concepts/long-horizon-development.md)
- [Regression tests](../concepts/regression-testing.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
