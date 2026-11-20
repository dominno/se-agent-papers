---
type: source
title: "OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments"
created: 2026-11-19
arxiv_id: "2404.07972"
url: "https://arxiv.org/abs/2404.07972"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "evaluation-metrics", "benchmarks", "comparison-and-reproducibility", "tool-sandboxing"]
source_path: "raw/papers/2404.07972.md"
sources: ["https://arxiv.org/abs/2404.07972"]
ingested: "2026-11-19"
---

# OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments

**Paper:** [2404.07972](https://arxiv.org/abs/2404.07972) · [PDF](https://arxiv.org/pdf/2404.07972) · [HTML](https://arxiv.org/html/2404.07972)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** OSWorld restores the initial desktop state and uses a script to check the result. Its main benchmark contains 369 Ubuntu tasks, including 101 cross-application tasks. It also provides 43 Windows tasks. [PDF, p. 3](https://arxiv.org/pdf/2404.07972v2#page=3) [PDF, p. 6](https://arxiv.org/pdf/2404.07972v2#page=6) [PDF, p. 8](https://arxiv.org/pdf/2404.07972v2#page=8)

**Key result.** In Table 5, GPT-4 with the accessibility tree achieved the highest model score, 12.24%. Humans scored 72.36%, a difference of 60.12 percentage points. [PDF, p. 9](https://arxiv.org/pdf/2404.07972v2#page=9) [PDF, p. 10](https://arxiv.org/pdf/2404.07972v2#page=10)

**Limitations and scope.** Window size and layout affect interface behavior. Across 28 selected tasks, resizing reduced the score from 50.79% to 15.04%. The result does not estimate the effect across all 369 tasks. [PDF, p. 14](https://arxiv.org/pdf/2404.07972v2#page=14)

[Section and table audit for 2404.07972v2](../reviews/audit-2026-11-19/2404.07972v2.md)

## Overview

The benchmark tests agents in real desktop environments and automatically evaluates task completion. [PDF, p. 1](https://arxiv.org/pdf/2404.07972v2#page=1)

## Source files

arXiv version `2404.07972v2` · PDF pages: 51.

- [Original PDF](https://arxiv.org/pdf/2404.07972v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2404.07972.metadata.json)

PDF bookmarks — [Details of Baseline Methods (p. 34)](https://arxiv.org/pdf/2404.07972v2#page=34).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)
- [Tool sandbox](../concepts/tool-sandboxing.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
