---
type: source
title: "Automated Design of Agentic Systems"
created: 2026-11-19
arxiv_id: "2408.08435"
url: "https://arxiv.org/abs/2408.08435"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "task-planning", "architecture-design"]
source_path: "raw/papers/2408.08435.md"
sources: ["https://arxiv.org/abs/2408.08435"]
ingested: "2026-11-19"
---

# Automated Design of Agentic Systems

**Paper:** [2408.08435](https://arxiv.org/abs/2408.08435) · [PDF](https://arxiv.org/pdf/2408.08435) · [HTML](https://arxiv.org/html/2408.08435)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** The GPT-4o meta-agent generates an agent program, tests it and records the result in an archive. GPT-3.5 executed both the generated designs and the baselines in the main reasoning-task comparison. [PDF, p. 4](https://arxiv.org/pdf/2408.08435v2#page=4) [PDF, p. 7](https://arxiv.org/pdf/2408.08435v2#page=7) [PDF, p. 29](https://arxiv.org/pdf/2408.08435v2#page=29)

**Key result.** On DROP, the method scored 79.4 ± 0.8 F1 points, compared with 65.8 ± 0.9 for the best manual approach. On MGSM, accuracy was 53.4 ± 3.5% versus 39.0 ± 3.4%. Table 1 reports 95% bootstrap intervals. [PDF, p. 7](https://arxiv.org/pdf/2408.08435v2#page=7)

**Limitations and scope.** The ARC evaluation used an easy subset with grids of up to 5 × 5. The ranking of agent designs depends on the executor model, and each domain ends in a single scored answer. [PDF, p. 6](https://arxiv.org/pdf/2408.08435v2#page=6) [PDF, p. 9](https://arxiv.org/pdf/2408.08435v2#page=9) [PDF, p. 11](https://arxiv.org/pdf/2408.08435v2#page=11)

[Audit report for 2408.08435v2](../reviews/audit-2026-11-19/2408.08435v2.md)

## Overview

The authors propose a meta-agent that automatically designs and evaluates new agent architectures. [PDF, p. 1](https://arxiv.org/pdf/2408.08435v2#page=1)

## Source files

arXiv version `2408.08435v2` · PDF pages: 34.

- [Original PDF](https://arxiv.org/pdf/2408.08435v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2408.08435.metadata.json)

PDF bookmarks — [Framework Code (p. 23)](https://arxiv.org/pdf/2408.08435v2#page=23) · [Experiments (p. 5)](https://arxiv.org/pdf/2408.08435v2#page=5).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Task planning](../concepts/task-planning.md)
- [Software architecture](../concepts/architecture-design.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
