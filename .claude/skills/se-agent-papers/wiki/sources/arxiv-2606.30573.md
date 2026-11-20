---
type: source
title: "SWE-INTERACT: Reimagining SWE Benchmarks as User-Driven Long-Horizon Coding Sessions"
created: 2026-11-19
arxiv_id: "2606.30573"
url: "https://arxiv.org/abs/2606.30573"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "task-planning", "coding-agents", "context-window", "evaluation-metrics", "benchmarks", "long-horizon-development", "acceptance-testing", "comparison-and-reproducibility"]
source_path: "raw/papers/2606.30573.md"
sources: ["https://arxiv.org/abs/2606.30573"]
ingested: "2026-11-19"
---

# SWE-INTERACT: Reimagining SWE Benchmarks as User-Driven Long-Horizon Coding Sessions

**Paper:** [2606.30573](https://arxiv.org/abs/2606.30573) · [PDF](https://arxiv.org/pdf/2606.30573) · [HTML](https://arxiv.org/html/2606.30573)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** The original verifier evaluated 75 manually selected tasks from three benchmarks. In one configuration, the agent received the full specification up front. In the other, a simulated user with access to the repository disclosed it in stages. [PDF, p. 3](https://arxiv.org/pdf/2606.30573v1#page=3) [PDF, p. 4](https://arxiv.org/pdf/2606.30573v1#page=4) [PDF, p. 5](https://arxiv.org/pdf/2606.30573v1#page=5)

**Key result.** GPT-5.5 scored 48.0% in the single-turn setting and 37/150 (24.7%) interactively. Opus 4.8 scored 50.7% and 40/150 (26.7%), respectively. Both simulators used the same 75 tasks. [PDF, p. 5](https://arxiv.org/pdf/2606.30573v1#page=5) [PDF, p. 13](https://arxiv.org/pdf/2606.30573v1#page=13)

**Limitations and scope.** The study selected one predominant persona and tasks with layered requirements. About 12% of the labels assigned to 287 failed runs concerned a requirement the user had not disclosed. This limits attribution of failures to the agent. [PDF, p. 3](https://arxiv.org/pdf/2606.30573v1#page=3) [PDF, p. 4](https://arxiv.org/pdf/2606.30573v1#page=4) [PDF, p. 7](https://arxiv.org/pdf/2606.30573v1#page=7) [PDF, p. 8](https://arxiv.org/pdf/2606.30573v1#page=8)

[Audit of sections, tables and appendices](../reviews/audit-2026-11-19/2606.30573v1.md)

## Overview

The study evaluates coding agents working with a user over multiple turns as requirements change. [PDF, p. 1](https://arxiv.org/pdf/2606.30573v1#page=1)

## Source files

arXiv version `2606.30573v1` · PDF pages: 23.

- [Original PDF](https://arxiv.org/pdf/2606.30573v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2606.30573.metadata.json)

PDF bookmarks — [Experimental Results (p. 4)](https://arxiv.org/pdf/2606.30573v1#page=4).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Task planning](../concepts/task-planning.md)
- [Coding agents](../concepts/coding-agents.md)
- [Context window](../concepts/context-window.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Long-term software evolution](../concepts/long-horizon-development.md)
- [Acceptance tests](../concepts/acceptance-testing.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
