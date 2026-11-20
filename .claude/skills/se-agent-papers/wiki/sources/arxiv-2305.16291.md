---
type: source
title: "Voyager: An Open-Ended Embodied Agent with Large Language Models"
created: 2026-11-19
arxiv_id: "2305.16291"
url: "https://arxiv.org/abs/2305.16291"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "agent-skills", "long-term-memory"]
source_path: "raw/papers/2305.16291.md"
sources: ["https://arxiv.org/abs/2305.16291"]
ingested: "2026-11-19"
---

# Voyager: An Open-Ended Embodied Agent with Large Language Models

**Paper:** [2305.16291](https://arxiv.org/abs/2305.16291) · [PDF](https://arxiv.org/pdf/2305.16291) · [HTML](https://arxiv.org/html/2305.16291)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** Voyager combines an automatic curriculum, a library of executable skills and iterative program refinement using game state, errors and execution feedback. [PDF, p. 3](https://arxiv.org/pdf/2305.16291v2#page=3) [PDF, p. 4](https://arxiv.org/pdf/2305.16291v2#page=4) [PDF, p. 5](https://arxiv.org/pdf/2305.16291v2#page=5) [PDF, p. 19](https://arxiv.org/pdf/2305.16291v2#page=19)

**Key result.** Within 160 iterations, Voyager discovered 63 items, about 3.3 times as many as the baselines. It acquired iron tools in 3/3 runs and diamond tools in 1/3. [PDF, p. 7](https://arxiv.org/pdf/2305.16291v2#page=7)

**Limitations and scope.** The transfer test covers four new goals in a new world in the same game. Both the goal-proposing model and the verifier can err, and the interface supplies game state and prewritten execution routines. [PDF, p. 8](https://arxiv.org/pdf/2305.16291v2#page=8) [PDF, p. 10](https://arxiv.org/pdf/2305.16291v2#page=10) [PDF, p. 38](https://arxiv.org/pdf/2305.16291v2#page=38)

[Section and table audit for 2305.16291v2](../reviews/audit-2026-11-19/2305.16291v2.md)

## Overview

The paper presents an agent that builds a library of executable skills and reuses them in later tasks. [PDF, p. 1](https://arxiv.org/pdf/2305.16291v2#page=1)

## Source files

arXiv version `2305.16291v2` · PDF pages: 42.

- [Original PDF](https://arxiv.org/pdf/2305.16291v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2305.16291.metadata.json)

PDF bookmarks — [Experiments (p. 6)](https://arxiv.org/pdf/2305.16291v2#page=6) · [Limitations and Future Work (p. 10)](https://arxiv.org/pdf/2305.16291v2#page=10).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Agent skills](../concepts/agent-skills.md)
- [Long-term memory](../concepts/long-term-memory.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
