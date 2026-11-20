---
type: source
title: "CodeSpec: Dual Executable Specifications for Agentic Long-Horizon Feature Development"
created: 2026-11-19
arxiv_id: "2607.26777"
url: "https://arxiv.org/abs/2607.26777"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "task-planning", "coding-agents", "context-window", "long-horizon-development"]
source_path: "raw/papers/2607.26777.md"
sources: ["https://arxiv.org/abs/2607.26777"]
ingested: "2026-11-19"
---

# CodeSpec: Dual Executable Specifications for Agentic Long-Horizon Feature Development

**Paper:** [2607.26777](https://arxiv.org/abs/2607.26777) · [PDF](https://arxiv.org/pdf/2607.26777) · [HTML](https://arxiv.org/html/2607.26777)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** CodeSpec converts relationships between requirements and repository components into two executable sets of checks covering architecture and behavior. [PDF, p. 1](https://arxiv.org/pdf/2607.26777v1#page=1)

**Key result.** On FeatureBench Lite/Fast/Full with DeepSeek-V4-Pro, the mean percentage of tests passed per task (%Passed) was 70.7/55.0/49.9%. The agent fully solved 9/30, 17/100 and 28/200 tasks. On Fast, Table 1 gives Mini-SWE-Agent 24 full solutions versus 17 for CodeSpec, contradicting the text’s claim that CodeSpec solved the most tasks. [PDF, p. 5](https://arxiv.org/pdf/2607.26777v1#page=5)

**Limitations and scope.** The Lite, Fast and Full sets contain 30, 100 and 200 tasks, respectively. Performance on the smallest set does not establish performance on the full set. [PDF, p. 5](https://arxiv.org/pdf/2607.26777v1#page=5)

[Audit report for 2607.26777v1](../reviews/audit-2026-11-19/2607.26777v1.md)

## Overview

The method combines executable specifications of behavior and code structure to verify complex feature implementations. [PDF, p. 1](https://arxiv.org/pdf/2607.26777v1#page=1)

## Source files

arXiv version `2607.26777v1` · PDF pages: 8.

- [Original PDF](https://arxiv.org/pdf/2607.26777v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2607.26777.metadata.json)

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Task planning](../concepts/task-planning.md)
- [Coding agents](../concepts/coding-agents.md)
- [Context window](../concepts/context-window.md)
- [Long-term software evolution](../concepts/long-horizon-development.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
