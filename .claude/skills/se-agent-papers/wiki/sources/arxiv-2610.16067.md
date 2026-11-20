---
type: source
title: "When Agent Evaluation Becomes Unreliable: An Empirical Study of Oracle Failures and Configuration-Dependent Measurement in an LLM Agent Benchmark"
created: 2026-11-19
arxiv_id: "2610.16067"
url: "https://arxiv.org/abs/2610.16067"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "debugging", "rag-evaluation", "evaluation-metrics", "llm-as-judge", "benchmarks", "fault-recovery", "comparison-and-reproducibility"]
source_path: "raw/papers/2610.16067.md"
sources: ["https://arxiv.org/abs/2610.16067"]
ingested: "2026-11-19"
---

# When Agent Evaluation Becomes Unreliable: An Empirical Study of Oracle Failures and Configuration-Dependent Measurement in an LLM Agent Benchmark

**Paper:** [2610.16067](https://arxiv.org/abs/2610.16067) · [PDF](https://arxiv.org/pdf/2610.16067) · [HTML](https://arxiv.org/html/2610.16067)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** The authors test whether the evaluator alters the state it grades, then replay recorded actions from 4,320 episodes against a clean database. Additional checks examine the effects of domain, language and simulator. [PDF, p. 8](https://arxiv.org/pdf/2610.16067v2#page=8) [PDF, p. 9](https://arxiv.org/pdf/2610.16067v2#page=9) [PDF, p. 12](https://arxiv.org/pdf/2610.16067v2#page=12) [PDF, p. 14](https://arxiv.org/pdf/2610.16067v2#page=14) [PDF, p. 18](https://arxiv.org/pdf/2610.16067v2#page=18)

**Key result.** After replay, database-criterion passes fell from 4,194 to 2,883. Overall success under all scoring rules fell from 94.3% to 65.5%, a drop of 28.8 percentage points. The ordering of model point estimates also changed. [PDF, p. 14](https://arxiv.org/pdf/2610.16067v2#page=14) [PDF, p. 15](https://arxiv.org/pdf/2610.16067v2#page=15)

**Limitations and scope.** The retail sample comprises 30 tasks and one provider. The corrected difference between the two highest-scoring agents was 1.20 points, with an interval that includes zero. [PDF, p. 9](https://arxiv.org/pdf/2610.16067v2#page=9) [PDF, p. 15](https://arxiv.org/pdf/2610.16067v2#page=15) [PDF, p. 21](https://arxiv.org/pdf/2610.16067v2#page=21)

[Audit of sections, tables and appendices](../reviews/audit-2026-11-19/2610.16067v2.md)

## Overview

The study examines evaluator defects that can inflate or distort reported agent performance. [PDF, p. 1](https://arxiv.org/pdf/2610.16067v2#page=1)

## Source files

arXiv version `2610.16067v2` · PDF pages: 29.

- [Original PDF](https://arxiv.org/pdf/2610.16067v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2610.16067.metadata.json)

PDF bookmarks — [Methodology (p. 7)](https://arxiv.org/pdf/2610.16067v2#page=7) · [Results (p. 12)](https://arxiv.org/pdf/2610.16067v2#page=12) · [Threats to Validity (p. 21)](https://arxiv.org/pdf/2610.16067v2#page=21).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Debugging](../concepts/debugging.md)
- [RAG evaluation](../concepts/rag-evaluation.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [LLM-as-a-Judge](../concepts/llm-as-judge.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Crash recovery](../concepts/fault-recovery.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
