---
type: source
title: "TRAJDEBUG: Tracing Error Lifecycle to Identify Critical Failures in Long-Horizon Agent Trajectories"
created: 2026-11-19
arxiv_id: "2608.06346"
url: "https://arxiv.org/abs/2608.06346"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "debugging", "context-window", "claim-verification", "long-horizon-development", "observability", "fault-recovery"]
source_path: "raw/papers/2608.06346.md"
sources: ["https://arxiv.org/abs/2608.06346"]
ingested: "2026-11-19"
---

# TRAJDEBUG: Tracing Error Lifecycle to Identify Critical Failures in Long-Horizon Agent Trajectories

**Paper:** [2608.06346](https://arxiv.org/abs/2608.06346) · [PDF](https://arxiv.org/pdf/2608.06346) · [HTML](https://arxiv.org/html/2608.06346)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** TrajErrBench contains 486 manually labeled failed runs, including 400 from τ²-Bench and 86 from SWE-Bench Pro. It tests whether a method can locate the error responsible for the final failure. [PDF, p. 2](https://arxiv.org/pdf/2608.06346v1#page=2)

**Key result.** For exact identification of the critical step, TrajDebug achieved 34.11% macro-averaged across seven subsets. Across all 869 trajectories, it identified 363 steps correctly (41.77%). A voting variant at similar cost achieved a macro-average of 29.56%. [PDF, p. 6](https://arxiv.org/pdf/2608.06346v1#page=6) [PDF, p. 23](https://arxiv.org/pdf/2608.06346v1#page=23) [PDF, p. 24](https://arxiv.org/pdf/2608.06346v1#page=24)

**Limitations and scope.** Root-cause attribution still depends on a language model's interpretation, even when it must cite evidence from the trajectory. [PDF, p. 9](https://arxiv.org/pdf/2608.06346v1#page=9)

[Audit report for 2608.06346v1](../reviews/audit-2026-11-19/2608.06346v1.md)

## Overview

The study follows errors through long agent trajectories and attributes failures to critical steps. [PDF, p. 1](https://arxiv.org/pdf/2608.06346v1#page=1)

## Source files

arXiv version `2608.06346v1` · PDF pages: 24.

- [Original PDF](https://arxiv.org/pdf/2608.06346v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2608.06346.metadata.json)

PDF bookmarks — [Experiments (p. 5)](https://arxiv.org/pdf/2608.06346v1#page=5) · [Limitations (p. 9)](https://arxiv.org/pdf/2608.06346v1#page=9).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Debugging](../concepts/debugging.md)
- [Context window](../concepts/context-window.md)
- [Claim verification](../concepts/claim-verification.md)
- [Long-term software evolution](../concepts/long-horizon-development.md)
- [Agent observability](../concepts/observability.md)
- [Crash recovery](../concepts/fault-recovery.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
