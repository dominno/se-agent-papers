---
type: source
title: "Debugging the Debuggers: Failure-Anchored Structured Recovery for Software Engineering Agents"
created: 2026-11-19
arxiv_id: "2605.08717"
url: "https://arxiv.org/abs/2605.08717"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "coding-agents", "debugging", "claim-verification", "observability", "fault-recovery"]
source_path: "raw/papers/2605.08717.md"
sources: ["https://arxiv.org/abs/2605.08717"]
ingested: "2026-11-19"
---

# Debugging the Debuggers: Failure-Anchored Structured Recovery for Software Engineering Agents

**Paper:** [2605.08717](https://arxiv.org/abs/2605.08717) · [PDF](https://arxiv.org/pdf/2605.08717) · [HTML](https://arxiv.org/html/2605.08717)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** PROBE connects telemetry from a failed task to a diagnosis and checks whether the resulting guidance is grounded in the data, actionable and within the agent’s capabilities. All methods were allowed a single repair attempt on each of three benchmarks. [PDF, p. 5](https://arxiv.org/pdf/2605.08717v2#page=5) [PDF, p. 6](https://arxiv.org/pdf/2605.08717v2#page=6) [PDF, p. 7](https://arxiv.org/pdf/2605.08717v2#page=7)

**Key result.** PROBE matched the agreed root-cause category in 168/257 cases (65.37%) and repaired 56/257 (21.79%). Each of the two summary-based baselines repaired 24/257 cases (9.34%). [PDF, p. 7](https://arxiv.org/pdf/2605.08717v2#page=7) [PDF, p. 8](https://arxiv.org/pdf/2605.08717v2#page=8)

**Limitations and scope.** The study considered only initially unsolved tasks and allowed one further attempt. Matching the diagnosis to the label was unnecessary for success under the metric used. In the patch preparation or submission category, 15 cases were repaired and 12 diagnoses matched. [PDF, p. 7](https://arxiv.org/pdf/2605.08717v2#page=7) [PDF, p. 8](https://arxiv.org/pdf/2605.08717v2#page=8) [PDF, p. 10](https://arxiv.org/pdf/2605.08717v2#page=10)

[Section and table audit for 2605.08717v2](../reviews/audit-2026-11-19/2605.08717v2.md)

## Overview

PROBE collects structured failure telemetry, diagnoses the problem and provides controlled guidance when the coding agent retries. [PDF, p. 1](https://arxiv.org/pdf/2605.08717v2#page=1)

## Source files

arXiv version `2605.08717v2` · PDF pages: 12.

- [Original PDF](https://arxiv.org/pdf/2605.08717v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2605.08717.metadata.json)

PDF bookmarks — [4 Experiments (p. 6)](https://arxiv.org/pdf/2605.08717v2#page=6) · [6 Discussion and Limitations (p. 10)](https://arxiv.org/pdf/2605.08717v2#page=10).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Coding agents](../concepts/coding-agents.md)
- [Debugging](../concepts/debugging.md)
- [Claim verification](../concepts/claim-verification.md)
- [Agent observability](../concepts/observability.md)
- [Crash recovery](../concepts/fault-recovery.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
