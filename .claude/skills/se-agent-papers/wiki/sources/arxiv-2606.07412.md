---
type: source
title: "Socratic-SWE: Self-Evolving Coding Agents via Trace-Derived Agent Skills"
created: 2026-11-19
arxiv_id: "2606.07412"
url: "https://arxiv.org/abs/2606.07412"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "coding-agents", "self-evolution", "agent-skills", "observability"]
source_path: "raw/papers/2606.07412.md"
sources: ["https://arxiv.org/abs/2606.07412"]
ingested: "2026-11-19"
---

# Socratic-SWE: Self-Evolving Coding Agents via Trace-Derived Agent Skills

**Paper:** [2606.07412](https://arxiv.org/abs/2606.07412) · [PDF](https://arxiv.org/pdf/2606.07412) · [HTML](https://arxiv.org/html/2606.07412)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** Qwen3.5-9B learns two roles on code-repair tasks using historical trajectories, test-based verification and a comparison of the training signal against external validation. Each of the three rounds uses 12,000 examples. [PDF, p. 5](https://arxiv.org/pdf/2606.07412v1#page=5) [PDF, p. 6](https://arxiv.org/pdf/2606.07412v1#page=6) [PDF, p. 7](https://arxiv.org/pdf/2606.07412v1#page=7)

**Key result.** After three rounds on SWE-bench Verified, the method solved 252/500 tasks (50.40%), compared with 213 for the base model and 235 for SSR. After five rounds it reached 52.00%. [PDF, p. 7](https://arxiv.org/pdf/2606.07412v1#page=7) [PDF, p. 8](https://arxiv.org/pdf/2606.07412v1#page=8) [PDF, p. 9](https://arxiv.org/pdf/2606.07412v1#page=9)

**Limitations and scope.** The experiment uses a fixed pool of repositories and requires reliable tests. In proof C.1, the mean reward includes the current sample. Before normalization, the stated estimator scales the true gradient by (K−1)/K in expectation. [PDF, p. 10](https://arxiv.org/pdf/2606.07412v1#page=10) [PDF, p. 15](https://arxiv.org/pdf/2606.07412v1#page=15)

[Audit of sections, tables and appendices](../reviews/audit-2026-11-19/2606.07412v1.md)

## Overview

The method uses coding-agent trajectories and failures to develop and evaluate new skills. [PDF, p. 1](https://arxiv.org/pdf/2606.07412v1#page=1)

## Source files

arXiv version `2606.07412v1` · PDF pages: 21.

- [Original PDF](https://arxiv.org/pdf/2606.07412v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2606.07412.metadata.json)

PDF bookmarks — [Methodology (p. 4)](https://arxiv.org/pdf/2606.07412v1#page=4) · [Experiments (p. 7)](https://arxiv.org/pdf/2606.07412v1#page=7).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Coding agents](../concepts/coding-agents.md)
- [Agent self-improvement](../concepts/self-evolution.md)
- [Agent skills](../concepts/agent-skills.md)
- [Agent observability](../concepts/observability.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
