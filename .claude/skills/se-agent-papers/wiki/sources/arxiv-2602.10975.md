---
type: source
title: "FeatureBench: Benchmarking Agentic Coding for Complex Feature Development"
created: 2026-11-19
arxiv_id: "2602.10975"
url: "https://arxiv.org/abs/2602.10975"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "coding-agents", "evaluation-metrics", "benchmarks", "acceptance-testing", "comparison-and-reproducibility"]
source_path: "raw/papers/2602.10975.md"
sources: ["https://arxiv.org/abs/2602.10975"]
ingested: "2026-11-19"
---

# FeatureBench: Benchmarking Agentic Coding for Complex Feature Development

**Paper:** [2602.10975](https://arxiv.org/abs/2602.10975) · [PDF](https://arxiv.org/pdf/2602.10975) · [HTML](https://arxiv.org/html/2602.10975)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** The authors derived 200 tasks from the tests and dependencies of 24 real Python repositories. They check that tests fail after a function is removed, run regression tests and verify that applying the reference solution restores functionality. [PDF, p. 4](https://arxiv.org/pdf/2602.10975v1#page=4) [PDF, p. 5](https://arxiv.org/pdf/2602.10975v1#page=5) [PDF, p. 6](https://arxiv.org/pdf/2602.10975v1#page=6) [PDF, p. 19](https://arxiv.org/pdf/2602.10975v1#page=19)

**Key result.** On the Full set, GPT-5.1-Codex in Codex had the highest complete solution rate, 12.5% (25/200). Opus 4.5 achieved 11.0% in Claude Code and 10.5% in OpenHands. [PDF, p. 6](https://arxiv.org/pdf/2602.10975v1#page=6) [PDF, p. 7](https://arxiv.org/pdf/2602.10975v1#page=7) [PDF, p. 19](https://arxiv.org/pdf/2602.10975v1#page=19)

**Limitations and scope.** Performance depends on access to tests and the agent interface. When the tests were revealed on Lite, GPT-5.1-Codex improved from 20.0% to 63.3%. Recognizing cross-file dependencies was one source of errors. [PDF, p. 6](https://arxiv.org/pdf/2602.10975v1#page=6) [PDF, p. 8](https://arxiv.org/pdf/2602.10975v1#page=8) [PDF, p. 9](https://arxiv.org/pdf/2602.10975v1#page=9)

## Overview

The benchmark evaluates implementation of complex features spanning multiple files, modules and dependencies. [PDF, p. 1](https://arxiv.org/pdf/2602.10975v1#page=1)

[Section and evidence audit](../reviews/audit-2026-11-19/2602.10975v1.md)

## Source files

arXiv version `2602.10975v1` · PDF pages: 37.

- [Original PDF](https://arxiv.org/pdf/2602.10975v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2602.10975.metadata.json)

PDF bookmarks — [Experiments (p. 6)](https://arxiv.org/pdf/2602.10975v1#page=6).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Coding agents](../concepts/coding-agents.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Acceptance tests](../concepts/acceptance-testing.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
