---
type: source
title: "Evolving to Match Capabilities: Improving Harness Self-Evolution via Skill Adaptation"
created: 2026-11-19
arxiv_id: "2610.33024"
url: "https://arxiv.org/abs/2610.33024"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "self-evolution", "agent-skills"]
source_path: "raw/papers/2610.33024.md"
sources: ["https://arxiv.org/abs/2610.33024"]
ingested: "2026-11-19"
---

# Evolving to Match Capabilities: Improving Harness Self-Evolution via Skill Adaptation

**Paper:** [2610.33024](https://arxiv.org/abs/2610.33024) · [PDF](https://arxiv.org/pdf/2610.33024) · [HTML](https://arxiv.org/html/2610.33024)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** From 607 tasks, the authors selected 103 task–skill pairs for which instructions affected models differently. They compared a one-time instruction rewrite with five rounds of rewriting using execution feedback. [PDF, p. 3](https://arxiv.org/pdf/2610.33024v1#page=3) [PDF, p. 4](https://arxiv.org/pdf/2610.33024v1#page=4) [PDF, p. 7](https://arxiv.org/pdf/2610.33024v1#page=7) [PDF, p. 8](https://arxiv.org/pdf/2610.33024v1#page=8) [PDF, p. 16](https://arxiv.org/pdf/2610.33024v1#page=16)

**Key result.** Kimi-K3 revised instructions for three weaker models, improving their scores by 8.7, 14.1 and 5.1 points over the original instructions. After five rounds of self-revision, all seven models outperformed self-revision without the dedicated instruction. [PDF, p. 7](https://arxiv.org/pdf/2610.33024v1#page=7) [PDF, p. 8](https://arxiv.org/pdf/2610.33024v1#page=8) [PDF, p. 20](https://arxiv.org/pdf/2610.33024v1#page=20)

**Limitations and scope.** Each pair was evaluated once per round. The sample was selected for its response to instructions. The final gap between the two five-round variants was only 0.020–0.051. [PDF, p. 4](https://arxiv.org/pdf/2610.33024v1#page=4) [PDF, p. 9](https://arxiv.org/pdf/2610.33024v1#page=9) [PDF, p. 20](https://arxiv.org/pdf/2610.33024v1#page=20)

[Audit of sections, tables and appendices](../reviews/audit-2026-11-19/2610.33024v1.md)

## Overview

The study adapts agent skills to the capabilities of different models and compares this approach with using a single set of instructions. [PDF, p. 1](https://arxiv.org/pdf/2610.33024v1#page=1)

## Source files

arXiv version `2610.33024v1` · PDF pages: 24.

- [Original PDF](https://arxiv.org/pdf/2610.33024v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2610.33024.metadata.json)

PDF bookmarks — [Framework (p. 3)](https://arxiv.org/pdf/2610.33024v1#page=3) · [Experiments (p. 6)](https://arxiv.org/pdf/2610.33024v1#page=6).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Agent self-improvement](../concepts/self-evolution.md)
- [Agent skills](../concepts/agent-skills.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
