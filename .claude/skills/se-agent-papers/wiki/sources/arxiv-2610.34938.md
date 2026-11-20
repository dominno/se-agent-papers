---
type: source
title: "How Do Coding-Agent Harnesses Self-Evolve? An Empirical Study of Retrospective Adaptation"
created: 2026-11-19
arxiv_id: "2610.34938"
url: "https://arxiv.org/abs/2610.34938"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "coding-agents", "self-evolution"]
source_path: "raw/papers/2610.34938.md"
sources: ["https://arxiv.org/abs/2610.34938"]
ingested: "2026-11-19"
---

# How Do Coding-Agent Harnesses Self-Evolve? An Empirical Study of Retrospective Adaptation

**Paper:** [2610.34938](https://arxiv.org/abs/2610.34938) · [PDF](https://arxiv.org/pdf/2610.34938) · [HTML](https://arxiv.org/html/2610.34938)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** Claude Code worked on 30 SWE-bench Verified tasks. Of 125 proposals from retrospectives, 24 were implemented. Eleven resulting adaptations and one written by the authors were compared in 13 transfer trials on other issues from the same repositories, with five sessions per variant. [PDF, p. 2](https://arxiv.org/pdf/2610.34938v1#page=2) [PDF, p. 3](https://arxiv.org/pdf/2610.34938v1#page=3)

**Key result.** In seven trials where at least three baseline sessions encountered the problem, repeated actions disappeared in two cases (5/5 → 0/5 and 3/5 → 0/5), fell in one (5/5 → 2/5) and did not decrease in four. A separate Sphinx control trial showed an increase from 0/5 to 4/5. [PDF, p. 3](https://arxiv.org/pdf/2610.34938v1#page=3) [PDF, p. 4](https://arxiv.org/pdf/2610.34938v1#page=4)

**Limitations and scope.** Purposive selection of issues that reproduce the problem limits estimates of how often the benefit occurs in routine work. Labels were not fully blinded. Task success differed by at most one session between variants in each comparison. [PDF, p. 4](https://arxiv.org/pdf/2610.34938v1#page=4)

## Overview

The study tests whether changes proposed after reviewing a session reduce problems on later tasks. [PDF, p. 1](https://arxiv.org/pdf/2610.34938v1#page=1)

[Section and evidence audit](../reviews/audit-2026-11-19/2610.34938v1.md)

## Source files

arXiv version `2610.34938v1` · PDF pages: 5.

- [Original PDF](https://arxiv.org/pdf/2610.34938v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2610.34938.metadata.json)

PDF bookmarks — [Results (p. 3)](https://arxiv.org/pdf/2610.34938v1#page=3) · [Threats to validity (p. 4)](https://arxiv.org/pdf/2610.34938v1#page=4).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Coding agents](../concepts/coding-agents.md)
- [Agent self-improvement](../concepts/self-evolution.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
