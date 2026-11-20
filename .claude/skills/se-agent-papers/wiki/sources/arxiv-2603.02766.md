---
type: source
title: "EvoSkill: Automated Skill Discovery for Multi-Agent Systems"
created: 2026-11-19
arxiv_id: "2603.02766"
url: "https://arxiv.org/abs/2603.02766"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "self-evolution", "agent-skills", "claim-verification"]
source_path: "raw/papers/2603.02766.md"
sources: ["https://arxiv.org/abs/2603.02766"]
ingested: "2026-11-19"
---

# EvoSkill: Automated Skill Discovery for Multi-Agent Systems

**Paper:** [2603.02766](https://arxiv.org/abs/2603.02766) · [PDF](https://arxiv.org/pdf/2603.02766) · [HTML](https://arxiv.org/html/2603.02766)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** EvoSkill analyzes failed runs and edits skill files while keeping model weights frozen. Validation performance determines which variants it retains. [PDF, p. 1](https://arxiv.org/pdf/2603.02766v1#page=1)

**Key result.** On OfficeQA, Table 1 reports an increase in exact match from 60.6% to 68.1% after combining skills (+7.5 percentage points). The Figure 2 caption and main text report 67.9% (+7.3 percentage points). The authors did not publish an analysis of variance across seeds. [PDF, p. 6](https://arxiv.org/pdf/2603.02766v1#page=6)

**Limitations and scope.** Transfer without fine-tuning was demonstrated for particular task pairs, including skills developed on SealQA and applied to BrowseComp. [PDF, p. 1](https://arxiv.org/pdf/2603.02766v1#page=1)

[Audit report for 2603.02766v1](../reviews/audit-2026-11-19/2603.02766v1.md)

## Overview

The study investigates automatic discovery, modification and evaluation of skills used by agent teams. [PDF, p. 1](https://arxiv.org/pdf/2603.02766v1#page=1)

## Source files

arXiv version `2603.02766v1` · PDF pages: 22.

- [Original PDF](https://arxiv.org/pdf/2603.02766v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2603.02766.metadata.json)

PDF bookmarks — [Methodology (p. 2)](https://arxiv.org/pdf/2603.02766v1#page=2) · [Experiments (p. 5)](https://arxiv.org/pdf/2603.02766v1#page=5).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Agent self-improvement](../concepts/self-evolution.md)
- [Agent skills](../concepts/agent-skills.md)
- [Claim verification](../concepts/claim-verification.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
