---
type: source
title: "Phantom Guardrails: When Self-Improving Agent Harnesses Fix Failures That Never Happened"
created: 2026-11-19
arxiv_id: "2607.13083"
url: "https://arxiv.org/abs/2607.13083"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "debugging", "self-evolution", "fault-recovery"]
source_path: "raw/papers/2607.13083.md"
sources: ["https://arxiv.org/abs/2607.13083"]
ingested: "2026-11-19"
---

# Phantom Guardrails: When Self-Improving Agent Harnesses Fix Failures That Never Happened

**Paper:** [2607.13083](https://arxiv.org/abs/2607.13083) · [PDF](https://arxiv.org/pdf/2607.13083) · [HTML](https://arxiv.org/html/2607.13083)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** The authors construct a deterministic environment in which the correct response is to leave the state unchanged, then independently check each reported rule violation. [PDF, p. 1](https://arxiv.org/pdf/2607.13083v1#page=1)

**Key result.** Under the primary five-model protocol, an unnecessary guard appeared in 15/60 trials with the benign pattern and 0/60 without it. The 95% Wilson interval for the first proportion was 16–37%. GLM-5.1 accounted for 11 of the 15 cases. [PDF, p. 4](https://arxiv.org/pdf/2607.13083v1#page=4) [PDF, p. 13](https://arxiv.org/pdf/2607.13083v1#page=13)

**Limitations and scope.** The permissible behaviors are known in advance in this environment. The observed rate does not estimate how often these changes occur in real repositories. [PDF, p. 1](https://arxiv.org/pdf/2607.13083v1#page=1)

[Audit report for 2607.13083v1](../reviews/audit-2026-11-19/2607.13083v1.md)

## Overview

The study investigates apparent security improvements made in response to problems for which there is no observational evidence. [PDF, p. 1](https://arxiv.org/pdf/2607.13083v1#page=1)

## Source files

arXiv version `2607.13083v1` · PDF pages: 13.

- [Original PDF](https://arxiv.org/pdf/2607.13083v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2607.13083.metadata.json)

PDF bookmarks — [4 Results (p. 3)](https://arxiv.org/pdf/2607.13083v1#page=3) · [5 Discussion and Limitations (p. 6)](https://arxiv.org/pdf/2607.13083v1#page=6).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Debugging](../concepts/debugging.md)
- [Agent self-improvement](../concepts/self-evolution.md)
- [Crash recovery](../concepts/fault-recovery.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
