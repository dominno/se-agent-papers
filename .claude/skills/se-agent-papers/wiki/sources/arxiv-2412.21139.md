---
type: source
title: "Training Software Engineering Agents and Verifiers with SWE-Gym"
created: 2026-11-19
arxiv_id: "2412.21139"
url: "https://arxiv.org/abs/2412.21139"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "coding-agents", "evaluation-metrics", "benchmarks", "comparison-and-reproducibility"]
source_path: "raw/papers/2412.21139.md"
sources: ["https://arxiv.org/abs/2412.21139"]
ingested: "2026-11-19"
---

# Training Software Engineering Agents and Verifiers with SWE-Gym

**Paper:** [2412.21139](https://arxiv.org/abs/2412.21139) · [PDF](https://arxiv.org/pdf/2412.21139) · [HTML](https://arxiv.org/html/2412.21139)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** Starting from 64,689 issues, the authors constructed 2,438 executable tasks from 11 Python repositories. Unit tests selected training trajectories and labeled examples for the verifier. [PDF, p. 3](https://arxiv.org/pdf/2412.21139v2#page=3) [PDF, p. 4](https://arxiv.org/pdf/2412.21139v2#page=4) [PDF, p. 5](https://arxiv.org/pdf/2412.21139v2#page=5) [PDF, p. 7](https://arxiv.org/pdf/2412.21139v2#page=7)

**Key result.** On SWE-Bench Verified, OpenHands 32B achieved 20.6% after fine-tuning and 32.0% when a verifier selected among 16 attempts. On Lite, a separate agent, MoatlessTools 32B with a 32B verifier, achieved 26.0% with eight attempts according to Figure 7 and Table 5. [PDF, p. 6](https://arxiv.org/pdf/2412.21139v2#page=6) [PDF, p. 7](https://arxiv.org/pdf/2412.21139v2#page=7) [PDF, p. 13](https://arxiv.org/pdf/2412.21139v2#page=13) [PDF, p. 19](https://arxiv.org/pdf/2412.21139v2#page=19)

**Limitations and scope.** Training covered 11 selected projects. Results depend on trial count, the agent harness and selection quality. Section 5.1.2 reports 26.3% for Lite, while Figure 7 and Table 5 give 26.0%. [PDF, p. 4](https://arxiv.org/pdf/2412.21139v2#page=4) [PDF, p. 7](https://arxiv.org/pdf/2412.21139v2#page=7) [PDF, p. 8](https://arxiv.org/pdf/2412.21139v2#page=8) [PDF, p. 13](https://arxiv.org/pdf/2412.21139v2#page=13) [PDF, p. 19](https://arxiv.org/pdf/2412.21139v2#page=19)

## Overview

The authors provide executable tasks and environments for developing and evaluating coding agents and verifiers. [PDF, p. 1](https://arxiv.org/pdf/2412.21139v2#page=1)

[Section and evidence audit](../reviews/audit-2026-11-19/2412.21139v2.md)

## Source files

arXiv version `2412.21139v2` · PDF pages: 21.

- [Original PDF](https://arxiv.org/pdf/2412.21139v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2412.21139.metadata.json)

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Coding agents](../concepts/coding-agents.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
