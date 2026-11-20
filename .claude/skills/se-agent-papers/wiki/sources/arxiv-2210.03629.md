---
type: source
title: "ReAct: Synergizing Reasoning and Acting in Language Models"
created: 2026-11-19
arxiv_id: "2210.03629"
url: "https://arxiv.org/abs/2210.03629"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "task-planning"]
source_path: "raw/papers/2210.03629.md"
sources: ["https://arxiv.org/abs/2210.03629"]
ingested: "2026-11-19"
---

# ReAct: Synergizing Reasoning and Acting in Language Models

**Paper:** [2210.03629](https://arxiv.org/abs/2210.03629) · [PDF](https://arxiv.org/pdf/2210.03629) · [HTML](https://arxiv.org/html/2210.03629)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** ReAct interleaves reasoning and actions, using the results as new observations. The authors compare full trajectories with variants that remove reasoning or action. [PDF, p. 2](https://arxiv.org/pdf/2210.03629v3#page=2) [PDF, p. 3](https://arxiv.org/pdf/2210.03629v3#page=3) [PDF, p. 5](https://arxiv.org/pdf/2210.03629v3#page=5)

**Key result.** On ALFWorld, the best of six ReAct configurations achieved 71% success (mean 57%), compared with 37% for the best of eight BUTLER configurations. On WebShop, ReAct scored 40.0%, IL 29.1% and IL+RL 28.7%. [PDF, p. 8](https://arxiv.org/pdf/2210.03629v3#page=8)

**Limitations and scope.** On HotpotQA, ReAct alone scores 27.4 exact match, compared with 33.4 for CoT-SC. Retrieval can return incorrect information, and interactive results depend on the demonstrations chosen. [PDF, p. 5](https://arxiv.org/pdf/2210.03629v3#page=5) [PDF, p. 6](https://arxiv.org/pdf/2210.03629v3#page=6) [PDF, p. 8](https://arxiv.org/pdf/2210.03629v3#page=8) [PDF, p. 33](https://arxiv.org/pdf/2210.03629v3#page=33)

[Section and table audit for 2210.03629v3](../reviews/audit-2026-11-19/2210.03629v3.md)

## Overview

The method interleaves planning and acting with information returned by tools during interactive tasks. [PDF, p. 1](https://arxiv.org/pdf/2210.03629v3#page=1)

## Source files

arXiv version `2210.03629v3` · PDF pages: 33.

- [Original PDF](https://arxiv.org/pdf/2210.03629v3)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2210.03629.metadata.json)

PDF bookmarks — [A Additional Results (p. 14)](https://arxiv.org/pdf/2210.03629v3#page=14).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Task planning](../concepts/task-planning.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
