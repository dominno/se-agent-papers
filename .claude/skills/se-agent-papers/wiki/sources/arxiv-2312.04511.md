---
type: source
title: "An LLM Compiler for Parallel Function Calling"
created: 2026-11-19
arxiv_id: "2312.04511"
url: "https://arxiv.org/abs/2312.04511"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "task-planning", "parallelism", "workflow-optimization"]
source_path: "raw/papers/2312.04511.md"
sources: ["https://arxiv.org/abs/2312.04511"]
ingested: "2026-11-19"
---

# An LLM Compiler for Parallel Function Calling

**Paper:** [2312.04511](https://arxiv.org/abs/2312.04511) · [PDF](https://arxiv.org/pdf/2312.04511) · [HTML](https://arxiv.org/html/2312.04511)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** The planner builds a graph of tool calls. The dispatcher substitutes results from prior operations and launches ready calls in parallel. The system also supports streaming plans and replanning. [PDF, p. 4](https://arxiv.org/pdf/2312.04511v3#page=4) [PDF, p. 5](https://arxiv.org/pdf/2312.04511v3#page=5)

**Key result.** For movie recommendations, latency fell from 20.47 to 5.47 s for GPT (3.74× speedup) and from 33.37 to 11.83 s for LLaMA-2 (2.82×). The ReAct baseline received an additional instruction to reduce looping and premature termination. [PDF, p. 6](https://arxiv.org/pdf/2312.04511v3#page=6) [PDF, p. 7](https://arxiv.org/pdf/2312.04511v3#page=7)

**Limitations and scope.** Planning overhead and dependencies limit speedup. For LLaMA-2 on ParallelQA, the times in Table 1 are inconsistent with the reported 2.27× speedup. On 500 WebShop tasks using GPT-3.5, the improvement in success rate came with longer runtime. [PDF, p. 6](https://arxiv.org/pdf/2312.04511v3#page=6) [PDF, p. 9](https://arxiv.org/pdf/2312.04511v3#page=9) [PDF, p. 16](https://arxiv.org/pdf/2312.04511v3#page=16)

[Audit of sections, tables and appendices](../reviews/audit-2026-11-19/2312.04511v3.md)

## Overview

The authors represent tool calls as a dependency graph and execute independent operations in parallel. [PDF, p. 1](https://arxiv.org/pdf/2312.04511v3#page=1)

## Source files

arXiv version `2312.04511v3` · PDF pages: 22.

- [Original PDF](https://arxiv.org/pdf/2312.04511v3)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2312.04511.metadata.json)

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Task planning](../concepts/task-planning.md)
- [Parallelism](../concepts/parallelism.md)
- [Workflow optimization](../concepts/workflow-optimization.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
