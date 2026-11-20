---
type: source
title: "SWE-MeM: Learning Adaptive Memory Management for Long-Horizon Coding Agents"
created: 2026-11-19
arxiv_id: "2606.28434"
url: "https://arxiv.org/abs/2606.28434"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "coding-agents", "long-term-memory", "memory-evaluation", "context-window", "long-horizon-development"]
source_path: "raw/papers/2606.28434.md"
sources: ["https://arxiv.org/abs/2606.28434"]
ingested: "2026-11-19"
---

# SWE-MeM: Learning Adaptive Memory Management for Long-Horizon Coding Agents

**Paper:** [2606.28434](https://arxiv.org/abs/2606.28434) · [PDF](https://arxiv.org/pdf/2606.28434) · [HTML](https://arxiv.org/html/2606.28434)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** SWE-MeM trains an agent to decide when, what and how to compress in its interaction history while resolving an issue. Training combines memory-management demonstrations with a task-completion reward. [PDF, p. 1](https://arxiv.org/pdf/2606.28434v1#page=1)

**Key result.** On SWE-bench Verified with a 32K context, supervised learning followed by RL yielded 43.4% for 4B and 60.2% for 30B. The 30B model reached 58.8% with SFT alone, a gain of 1.4 percentage points after RL. [PDF, p. 7](https://arxiv.org/pdf/2606.28434v1#page=7) [PDF, p. 8](https://arxiv.org/pdf/2606.28434v1#page=8)

**Limitations and scope.** The remaining token budget is one signal for compression. Comparisons between memory policies depend on the context window available. [PDF, p. 16](https://arxiv.org/pdf/2606.28434v1#page=16)

[Audit report for 2606.28434v1](../reviews/audit-2026-11-19/2606.28434v1.md)

## Overview

The authors propose adaptive context and memory management for multi-stage coding tasks. [PDF, p. 1](https://arxiv.org/pdf/2606.28434v1#page=1)

## Source files

arXiv version `2606.28434v1` · PDF pages: 30.

- [Original PDF](https://arxiv.org/pdf/2606.28434v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2606.28434.metadata.json)

PDF bookmarks — [Proposed Approach (p. 2)](https://arxiv.org/pdf/2606.28434v1#page=2) · [Experiment (p. 6)](https://arxiv.org/pdf/2606.28434v1#page=6).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Coding agents](../concepts/coding-agents.md)
- [Long-term memory](../concepts/long-term-memory.md)
- [Memory evaluation](../concepts/memory-evaluation.md)
- [Context window](../concepts/context-window.md)
- [Long-term software evolution](../concepts/long-horizon-development.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
