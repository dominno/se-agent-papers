---
type: source
title: "Observability and Fault Injection for LLM-Based Multi-Agent Systems in Software Engineering"
created: 2026-11-19
arxiv_id: "2608.24271"
url: "https://arxiv.org/abs/2608.24271"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "coding-agents", "debugging", "tool-sandboxing", "prompt-injection", "observability", "fault-recovery"]
source_path: "raw/papers/2608.24271.md"
sources: ["https://arxiv.org/abs/2608.24271"]
ingested: "2026-11-19"
---

# Observability and Fault Injection for LLM-Based Multi-Agent Systems in Software Engineering

**Paper:** [2608.24271](https://arxiv.org/abs/2608.24271) · [PDF](https://arxiv.org/pdf/2608.24271) · [HTML](https://arxiv.org/html/2608.24271)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** llmmas-otel combines OpenTelemetry traces with labels for disturbances at communication boundaries between agents, tools and models. The study used 30 ProgramDev tasks with five repetitions per task and condition, a baseline and two variants that added one second of delay. [PDF, p. 2](https://arxiv.org/pdf/2608.24271v1#page=2) [PDF, p. 3](https://arxiv.org/pdf/2608.24271v1#page=3) [PDF, p. 4](https://arxiv.org/pdf/2608.24271v1#page=4)

**Key result.** Mean elapsed-time increases, in units of added delay per model call or message respectively, were 1.053 and 1.295 in the demonstration and 48.1 and 59.2 in ChatDev. The ChatDev medians were 13.9 and 6.6. [PDF, p. 4](https://arxiv.org/pdf/2608.24271v1#page=4)

**Limitations and scope.** Two systems and two delay scenarios limit generalizability. The table lacks uncertainty intervals, and the ChatDev medians have the reverse ordering, making the means alone difficult to interpret. [PDF, p. 4](https://arxiv.org/pdf/2608.24271v1#page=4)

[Section and table audit for 2608.24271v1](../reviews/audit-2026-11-19/2608.24271v1.md)

## Overview

The method combines distributed tracing of agents with controlled fault injection to diagnose reliability problems. [PDF, p. 1](https://arxiv.org/pdf/2608.24271v1#page=1)

## Source files

arXiv version `2608.24271v1` · PDF pages: 6.

- [Original PDF](https://arxiv.org/pdf/2608.24271v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2608.24271.metadata.json)

PDF bookmarks — [Framework (p. 2)](https://arxiv.org/pdf/2608.24271v1#page=2) · [Limitations and Future Work (p. 5)](https://arxiv.org/pdf/2608.24271v1#page=5).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Coding agents](../concepts/coding-agents.md)
- [Debugging](../concepts/debugging.md)
- [Tool sandbox](../concepts/tool-sandboxing.md)
- [Prompt injection](../concepts/prompt-injection.md)
- [Agent observability](../concepts/observability.md)
- [Crash recovery](../concepts/fault-recovery.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
