---
type: source
title: "Trial by Trace: Benchmarking AI Agent Harnesses for Reliability and Failure Attribution"
created: 2026-11-19
arxiv_id: "2610.32285"
url: "https://arxiv.org/abs/2610.32285"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "debugging", "self-evolution", "evaluation-metrics", "benchmarks", "observability", "fault-recovery", "comparison-and-reproducibility"]
source_path: "raw/papers/2610.32285.md"
sources: ["https://arxiv.org/abs/2610.32285"]
ingested: "2026-11-19"
---

# Trial by Trace: Benchmarking AI Agent Harnesses for Reliability and Failure Attribution

**Paper:** [2610.32285](https://arxiv.org/abs/2610.32285) · [PDF](https://arxiv.org/pdf/2610.32285) · [HTML](https://arxiv.org/html/2610.32285)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** TraceTrial-Bench pairs native traces with additional environment evidence. It evaluates task criteria separately from environment criteria across 95 tasks, nine model configurations and four environments. [PDF, p. 9](https://arxiv.org/pdf/2610.32285v1#page=9) [PDF, p. 11](https://arxiv.org/pdf/2610.32285v1#page=11) [PDF, p. 14](https://arxiv.org/pdf/2610.32285v1#page=14)

**Key result.** In 1,065 of 3,420 runs (31.1%), the task passed despite at least one unmet environment criterion. Both layers passed in 286 of 3,420 runs (8.4%). [PDF, p. 16](https://arxiv.org/pdf/2610.32285v1#page=16) [PDF, p. 19](https://arxiv.org/pdf/2610.32285v1#page=19)

**Limitations and scope.** The study selected one run per combination. Some mechanisms appear in only one task. The fraction of detected links between errors cannot estimate what proportion of errors the environment caused. [PDF, p. 14](https://arxiv.org/pdf/2610.32285v1#page=14) [PDF, p. 18](https://arxiv.org/pdf/2610.32285v1#page=18) [PDF, p. 19](https://arxiv.org/pdf/2610.32285v1#page=19) [PDF, p. 20](https://arxiv.org/pdf/2610.32285v1#page=20)

[Audit report for 2610.32285v1](../reviews/audit-2026-11-19/2610.32285v1.md)

## Overview

The study evaluates agent infrastructure reliability and traces failures to their sources using execution traces. [PDF, p. 1](https://arxiv.org/pdf/2610.32285v1#page=1)

## Source files

arXiv version `2610.32285v1` · PDF pages: 50.

- [Original PDF](https://arxiv.org/pdf/2610.32285v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2610.32285.metadata.json)

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Debugging](../concepts/debugging.md)
- [Agent self-improvement](../concepts/self-evolution.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Agent observability](../concepts/observability.md)
- [Crash recovery](../concepts/fault-recovery.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
