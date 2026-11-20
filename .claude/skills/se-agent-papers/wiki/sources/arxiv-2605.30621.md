---
type: source
title: "Harness Updating Is Not Harness Benefit: Disentangling Evolution Capabilities in Self-Evolving LLM Agents"
created: 2026-11-19
arxiv_id: "2605.30621"
url: "https://arxiv.org/abs/2605.30621"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "self-evolution"]
source_path: "raw/papers/2605.30621.md"
sources: ["https://arxiv.org/abs/2605.30621"]
ingested: "2026-11-19"
---

# Harness Updating Is Not Harness Benefit: Disentangling Evolution Capabilities in Self-Evolving LLM Agents

**Paper:** [2605.30621](https://arxiv.org/abs/2605.30621) · [PDF](https://arxiv.org/pdf/2605.30621) · [HTML](https://arxiv.org/html/2605.30621)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** With model weights frozen, the authors measured the mean effect of instruction changes across three executors and each executor’s largest gain across three authors of changes. The evaluation used SWE-bench Verified, MCP-Atlas and SkillsBench. [PDF, p. 4](https://arxiv.org/pdf/2605.30621v2#page=4) [PDF, p. 5](https://arxiv.org/pdf/2605.30621v2#page=5) [PDF, p. 16](https://arxiv.org/pdf/2605.30621v2#page=16) [PDF, p. 17](https://arxiv.org/pdf/2605.30621v2#page=17)

**Key result.** The largest executor gains were 19.3 points for Qwen3-235B on SWE, 7.0 for GPT-OSS-120B on MCP and 15.1 for Haiku 4.5 on SkillsBench. Weaker executors were less likely to load instructions. [PDF, p. 8](https://arxiv.org/pdf/2605.30621v2#page=8) [PDF, p. 20](https://arxiv.org/pdf/2605.30621v2#page=20)

**Limitations and scope.** Results depend on the fixed set of models and on reporting the largest of three gains for the executor. A model judged instruction adherence among trajectories in which the instructions had been loaded. Model weights were held fixed. [PDF, p. 5](https://arxiv.org/pdf/2605.30621v2#page=5) [PDF, p. 8](https://arxiv.org/pdf/2605.30621v2#page=8) [PDF, p. 10](https://arxiv.org/pdf/2605.30621v2#page=10) [PDF, p. 21](https://arxiv.org/pdf/2605.30621v2#page=21) [PDF, p. 25](https://arxiv.org/pdf/2605.30621v2#page=25) [PDF, p. 26](https://arxiv.org/pdf/2605.30621v2#page=26)

## Overview

The study distinguishes an agent's ability to change its harness from its ability to use the resulting change effectively. [PDF, p. 1](https://arxiv.org/pdf/2605.30621v2#page=1)

[Section and evidence audit](../reviews/audit-2026-11-19/2605.30621v2.md)

## Source files

arXiv version `2605.30621v2` · PDF pages: 27.

- [Original PDF](https://arxiv.org/pdf/2605.30621v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2605.30621.metadata.json)

PDF bookmarks — [Experiments (p. 5)](https://arxiv.org/pdf/2605.30621v2#page=5) · [Limitations (p. 10)](https://arxiv.org/pdf/2605.30621v2#page=10).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Agent self-improvement](../concepts/self-evolution.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
