---
type: source
title: "SWE-Bench Pro V2: A Cleaner, Harder-to-Game Coding Benchmark"
created: 2026-11-19
arxiv_id: "2610.24206"
url: "https://arxiv.org/abs/2610.24206"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "coding-agents", "evaluation-metrics", "benchmarks", "comparison-and-reproducibility"]
source_path: "raw/papers/2610.24206.md"
sources: ["https://arxiv.org/abs/2610.24206"]
ingested: "2026-11-19"
---

# SWE-Bench Pro V2: A Cleaner, Harder-to-Game Coding Benchmark

**Paper:** [2610.24206](https://arxiv.org/abs/2610.24206) · [PDF](https://arxiv.org/pdf/2610.24206) · [HTML](https://arxiv.org/html/2610.24206)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** After the audit, a second engineer checked the revised instructions without seeing the reference solution. In the main study, patches were evaluated in a clean container. A separate experiment on the execution environment used a different protocol. [PDF, p. 7](https://arxiv.org/pdf/2610.24206v2#page=7) [PDF, p. 8](https://arxiv.org/pdf/2610.24206v2#page=8) [PDF, p. 15](https://arxiv.org/pdf/2610.24206v2#page=15)

**Key result.** Opus 5 (xhigh) with Claude Code solved 638/642 V2 tasks, or 99.4% (95% Wilson interval 98.4–99.8%). Across 11 systems, performance on the 51 Hard tasks ranged from 52.9% to 98.0%. [PDF, p. 8](https://arxiv.org/pdf/2610.24206v2#page=8) [PDF, p. 9](https://arxiv.org/pdf/2610.24206v2#page=9)

**Limitations and scope.** The Hard subset was selected from tasks on which at least two of five model families failed. The authors then changed 39 of 51 instructions. The sample is nonrandom, and solutions from public repositories may have been memorized during training. [PDF, p. 12](https://arxiv.org/pdf/2610.24206v2#page=12) [PDF, p. 15](https://arxiv.org/pdf/2610.24206v2#page=15)

[Section and table audit for 2610.24206v2](../reviews/audit-2026-11-19/2610.24206v2.md)

## Overview

The authors present the revalidated public SWE-Bench Pro V2 dataset and its Hard subset. [PDF, p. 1](https://arxiv.org/pdf/2610.24206v2#page=1)

## Source files

arXiv version `2610.24206v2` · PDF pages: 16.

- [Original PDF](https://arxiv.org/pdf/2610.24206v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2610.24206.metadata.json)

PDF bookmarks — [Methodology (p. 3)](https://arxiv.org/pdf/2610.24206v2#page=3) · [Experiments (p. 8)](https://arxiv.org/pdf/2610.24206v2#page=8).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Coding agents](../concepts/coding-agents.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
