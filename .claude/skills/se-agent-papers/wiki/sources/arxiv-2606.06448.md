---
type: source
title: "Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads"
created: 2026-11-19
arxiv_id: "2606.06448"
url: "https://arxiv.org/abs/2606.06448"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "long-term-memory", "memory-evaluation", "context-window", "long-horizon-development", "stateful-tool-use", "tool-evaluation"]
source_path: "raw/papers/2606.06448.md"
sources: ["https://arxiv.org/abs/2606.06448"]
ingested: "2026-11-19"
---

# Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads

**Paper:** [2606.06448](https://arxiv.org/abs/2606.06448) · [PDF](https://arxiv.org/pdf/2606.06448) · [HTML](https://arxiv.org/html/2606.06448)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** The authors profile ten memory systems on two benchmarks, separating the time and cost of memory construction, retrieval and response generation. [PDF, p. 1](https://arxiv.org/pdf/2606.06448v2#page=1)

**Key result.** On 300 LongMemEval questions with a local Qwen3-32B, BM25 and GraphRAG achieved 47.0% and 46.0% accuracy according to an LLM judge. Building memory and answering the queries consumed 582 and 2,082 kJ of GPU energy, respectively. The cost breakdown depended on how many queries used the built memory. [PDF, p. 6](https://arxiv.org/pdf/2606.06448v2#page=6) [PDF, p. 9](https://arxiv.org/pdf/2606.06448v2#page=9)

**Limitations and scope.** The main energy measurement covers five long histories. The dataset favors some lexical methods. The freshness measurement covers 20 physics tasks at a simulated five-second interval. [PDF, p. 4](https://arxiv.org/pdf/2606.06448v2#page=4) [PDF, p. 8](https://arxiv.org/pdf/2606.06448v2#page=8) [PDF, p. 9](https://arxiv.org/pdf/2606.06448v2#page=9)

[Audit report for 2606.06448v2](../reviews/audit-2026-11-19/2606.06448v2.md)

## Overview

The study characterizes the cost and access patterns of memory reads and writes in long-running agent tasks. [PDF, p. 1](https://arxiv.org/pdf/2606.06448v2#page=1)

## Source files

arXiv version `2606.06448v2` · PDF pages: 14.

- [Original PDF](https://arxiv.org/pdf/2606.06448v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2606.06448.metadata.json)

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Long-term memory](../concepts/long-term-memory.md)
- [Memory evaluation](../concepts/memory-evaluation.md)
- [Context window](../concepts/context-window.md)
- [Long-term software evolution](../concepts/long-horizon-development.md)
- [Stateful tool use](../concepts/stateful-tool-use.md)
- [Tool evaluation](../concepts/tool-evaluation.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
