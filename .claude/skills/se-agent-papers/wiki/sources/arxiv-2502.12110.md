---
type: source
title: "A-MEM: Agentic Memory for LLM Agents"
created: 2026-11-19
arxiv_id: "2502.12110"
url: "https://arxiv.org/abs/2502.12110"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "long-term-memory", "memory-evaluation"]
source_path: "raw/papers/2502.12110.md"
sources: ["https://arxiv.org/abs/2502.12110"]
ingested: "2026-11-19"
---

# A-MEM: Agentic Memory for LLM Agents

**Paper:** [2502.12110](https://arxiv.org/abs/2502.12110) · [PDF](https://arxiv.org/pdf/2502.12110) · [HTML](https://arxiv.org/html/2502.12110)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** The model describes a new note, retrieves candidate links and can update the context of older entries. The authors evaluated it on LoCoMo and DialSim and ablated the linking and updating mechanisms. [PDF, p. 3](https://arxiv.org/pdf/2502.12110v11#page=3) [PDF, p. 4](https://arxiv.org/pdf/2502.12110v11#page=4) [PDF, p. 5](https://arxiv.org/pdf/2502.12110v11#page=5) [PDF, p. 7](https://arxiv.org/pdf/2502.12110v11#page=7)

**Key result.** On LoCoMo with GPT-4o-mini, F1 improved over MemGPT by 20.33 points on temporal questions and 0.37 on multi-hop questions. On adversarial questions, full history performed better, 69.23 versus 50.03. [PDF, p. 6](https://arxiv.org/pdf/2502.12110v11#page=6)

**Limitations and scope.** The number of entries retrieved depends on model and category. GPT-4o-mini used about 85% fewer context tokens than MemGPT (2,520 versus 16,977). This measure differs from the time needed for vector search. [PDF, p. 6](https://arxiv.org/pdf/2502.12110v11#page=6) [PDF, p. 8](https://arxiv.org/pdf/2502.12110v11#page=8) [PDF, p. 18](https://arxiv.org/pdf/2502.12110v11#page=18)

[Audit of sections, tables and appendices](../reviews/audit-2026-11-19/2502.12110v11.md)

## Overview

The memory system organizes information into a network of linked notes that it updates dynamically. [PDF, p. 1](https://arxiv.org/pdf/2502.12110v11#page=1)

## Source files

arXiv version `2502.12110v11` · PDF pages: 28.

- [Original PDF](https://arxiv.org/pdf/2502.12110v11)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2502.12110.metadata.json)

PDF bookmarks — [Experiment (p. 5)](https://arxiv.org/pdf/2502.12110v11#page=5) · [Limitations (p. 9)](https://arxiv.org/pdf/2502.12110v11#page=9).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Long-term memory](../concepts/long-term-memory.md)
- [Memory evaluation](../concepts/memory-evaluation.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
