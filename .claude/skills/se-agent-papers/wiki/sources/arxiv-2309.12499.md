---
type: source
title: "CodePlan: Repository-level Coding using LLMs and Planning"
created: 2026-11-19
arxiv_id: "2309.12499"
url: "https://arxiv.org/abs/2309.12499"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "task-planning", "coding-agents", "repository-context"]
source_path: "raw/papers/2309.12499.md"
sources: ["https://arxiv.org/abs/2309.12499"]
ingested: "2026-11-19"
---

# CodePlan: Repository-level Coding using LLMs and Planning

**Paper:** [2309.12499](https://arxiv.org/abs/2309.12499) · [PDF](https://arxiv.org/pdf/2309.12499) · [HTML](https://arxiv.org/html/2309.12499)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** CodePlan plans block edits from an incremental dependency graph and the effects of earlier changes. The model receives context from the editing history and from code that depends on the modified block. [PDF, p. 5](https://arxiv.org/pdf/2309.12499v1#page=5) [PDF, p. 7](https://arxiv.org/pdf/2309.12499v1#page=7) [PDF, p. 10](https://arxiv.org/pdf/2309.12499v1#page=10)

**Key result.** Five of six repositories passed the correctness checks: three C# migrations, two of which required a second iteration, and two of three Python tasks. Build-Repair and Pyright-Repair passed none. [PDF, p. 14](https://arxiv.org/pdf/2309.12499v1#page=14) [PDF, p. 19](https://arxiv.org/pdf/2309.12499v1#page=19)

**Limitations and scope.** Two C# repositories were internal. The ablation removed both context types together on Int-1, so it does not isolate the effect of either type or estimate performance on arbitrary tasks. [PDF, p. 14](https://arxiv.org/pdf/2309.12499v1#page=14) [PDF, p. 22](https://arxiv.org/pdf/2309.12499v1#page=22) [PDF, p. 23](https://arxiv.org/pdf/2309.12499v1#page=23) [PDF, p. 29](https://arxiv.org/pdf/2309.12499v1#page=29)

[Section and table audit for 2309.12499v1](../reviews/audit-2026-11-19/2309.12499v1.md)

## Overview

The study examines planning for multi-file repository changes, accounting for dependencies and the effects of edits. [PDF, p. 1](https://arxiv.org/pdf/2309.12499v1#page=1)

## Source files

arXiv version `2309.12499v1` · PDF pages: 34.

- [Original PDF](https://arxiv.org/pdf/2309.12499v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2309.12499.metadata.json)

PDF bookmarks — [5 Results and Analysis (p. 17)](https://arxiv.org/pdf/2309.12499v1#page=17) · [6 Limitations and Threats to Validity (p. 28)](https://arxiv.org/pdf/2309.12499v1#page=28).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Task planning](../concepts/task-planning.md)
- [Coding agents](../concepts/coding-agents.md)
- [Repository context](../concepts/repository-context.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
