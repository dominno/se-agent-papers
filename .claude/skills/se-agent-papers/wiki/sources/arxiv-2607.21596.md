---
type: source
title: "FlowEvo: Self-Evolving Agents through the Co-Evolution of Workflows and Executable Skills"
created: 2026-11-19
arxiv_id: "2607.21596"
url: "https://arxiv.org/abs/2607.21596"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "self-evolution", "workflow-optimization", "agent-skills"]
source_path: "raw/papers/2607.21596.md"
sources: ["https://arxiv.org/abs/2607.21596"]
ingested: "2026-11-19"
---

# FlowEvo: Self-Evolving Agents through the Co-Evolution of Workflows and Executable Skills

**Paper:** [2607.21596](https://arxiv.org/abs/2607.21596) · [PDF](https://arxiv.org/pdf/2607.21596) · [HTML](https://arxiv.org/html/2607.21596)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** FlowEvo stores validated execution patterns, chooses between direct reuse and generating a new workflow with their help, and tracks outcomes. It can exclude harmful patterns from active retrieval. [PDF, p. 3](https://arxiv.org/pdf/2607.21596v2#page=3) [PDF, p. 4](https://arxiv.org/pdf/2607.21596v2#page=4) [PDF, p. 5](https://arxiv.org/pdf/2607.21596v2#page=5) [PDF, p. 18](https://arxiv.org/pdf/2607.21596v2#page=18)

**Key result.** On ALFWorld with GPT-4o-mini, success was 85.6% (standard deviation 3.8 percentage points, three runs), compared with 59.2% for AFlow. In the ablation, adding pattern reuse to registration alone gained 41.8 points. [PDF, p. 6](https://arxiv.org/pdf/2607.21596v2#page=6) [PDF, p. 8](https://arxiv.org/pdf/2607.21596v2#page=8)

**Limitations and scope.** Performance improved over ExpeL in 49/50 model–dataset combinations. The exception was Qwen3-8B on MATH-500. In one ALFWorld run, 34 of the 101 cases of reuse under the broader definition went beyond reusing the template alone. [PDF, p. 8](https://arxiv.org/pdf/2607.21596v2#page=8) [PDF, p. 24](https://arxiv.org/pdf/2607.21596v2#page=24)

## Overview

The method improves agents' action sequences and builds executable skills for reuse. [PDF, p. 1](https://arxiv.org/pdf/2607.21596v2#page=1)

[Section and evidence audit](../reviews/audit-2026-11-19/2607.21596v2.md)

## Source files

arXiv version `2607.21596v2` · PDF pages: 25.

- [Original PDF](https://arxiv.org/pdf/2607.21596v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2607.21596.metadata.json)

PDF bookmarks — [Framework Thresholds and Configuration Constants (p. 21)](https://arxiv.org/pdf/2607.21596v2#page=21) · [Experiments (p. 5)](https://arxiv.org/pdf/2607.21596v2#page=5).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Agent self-improvement](../concepts/self-evolution.md)
- [Workflow optimization](../concepts/workflow-optimization.md)
- [Agent skills](../concepts/agent-skills.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
