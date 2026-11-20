---
type: source
title: "Multi-agent Architecture Search via Agentic Supernet"
created: 2026-11-19
arxiv_id: "2502.04180"
url: "https://arxiv.org/abs/2502.04180"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "task-planning", "architecture-design"]
source_path: "raw/papers/2502.04180.md"
sources: ["https://arxiv.org/abs/2502.04180"]
ingested: "2026-11-19"
---

# Multi-agent Architecture Search via Agentic Supernet

**Paper:** [2502.04180](https://arxiv.org/abs/2502.04180) · [PDF](https://arxiv.org/pdf/2502.04180) · [HTML](https://arxiv.org/html/2502.04180)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** MaAS selects agent-team layers and operators for each query. It learns a distribution over architectures with a penalty for token cost and revises operators using textual feedback. [PDF, p. 3](https://arxiv.org/pdf/2502.04180v2#page=3) [PDF, p. 4](https://arxiv.org/pdf/2502.04180v2#page=4) [PDF, p. 5](https://arxiv.org/pdf/2502.04180v2#page=5)

**Key result.** On the MATH test, MaAS scored 51.82%, compared with 51.28% for AFlow. Their API costs were $3.38 and $22.50 for training and $0.42 and $1.66 for inference, respectively. [PDF, p. 7](https://arxiv.org/pdf/2502.04180v2#page=7)

**Limitations and scope.** The cost comparison uses a particular MATH split (119/486) and API configuration. On GAIA Level 3, MaAS scored 6.25% and TapeAgent 10.20%, so the aggregate advantage does not hold for every category. [PDF, p. 6](https://arxiv.org/pdf/2502.04180v2#page=6) [PDF, p. 7](https://arxiv.org/pdf/2502.04180v2#page=7) [PDF, p. 17](https://arxiv.org/pdf/2502.04180v2#page=17)

[Section and table audit for 2502.04180v2](../reviews/audit-2026-11-19/2502.04180v2.md)

## Overview

The study compares agent configurations and team sizes in terms of problem type, output quality and computational cost. [PDF, p. 1](https://arxiv.org/pdf/2502.04180v2#page=1)

## Source files

arXiv version `2502.04180v2` · PDF pages: 19.

- [Original PDF](https://arxiv.org/pdf/2502.04180v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2502.04180.metadata.json)

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Task planning](../concepts/task-planning.md)
- [Software architecture](../concepts/architecture-design.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
