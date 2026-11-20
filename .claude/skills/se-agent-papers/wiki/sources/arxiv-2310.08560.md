---
type: source
title: "MemGPT: Towards LLMs as Operating Systems"
created: 2026-11-19
arxiv_id: "2310.08560"
url: "https://arxiv.org/abs/2310.08560"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["long-term-memory", "memory-hierarchy", "context-window", "retrieval-augmented-generation", "hierarchical-retrieval", "grounded-generation"]
source_path: "raw/papers/2310.08560.md"
sources: ["https://arxiv.org/abs/2310.08560"]
ingested: "2026-11-19"
---

# MemGPT: Towards LLMs as Operating Systems

**Paper:** [2310.08560](https://arxiv.org/abs/2310.08560) · [PDF](https://arxiv.org/pdf/2310.08560) · [HTML](https://arxiv.org/html/2310.08560)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** MemGPT manages working memory, a message queue, conversation history and archival storage. It can retrieve successive pages of results before answering. The comparisons cover three GPT models on dialogue and document tasks. [PDF, p. 2](https://arxiv.org/pdf/2310.08560v2#page=2) [PDF, p. 3](https://arxiv.org/pdf/2310.08560v2#page=3) [PDF, p. 4](https://arxiv.org/pdf/2310.08560v2#page=4)

**Key result.** On DMR, GPT-4 accuracy rose from 32.1% with a history summary to 92.5% with MemGPT. At nested retrieval level 3, MemGPT with GPT-4 reached 100%, the GPT-4 Turbo variant about 60%, and the baselines 0%. [PDF, p. 5](https://arxiv.org/pdf/2310.08560v2#page=5) [PDF, p. 7](https://arxiv.org/pdf/2310.08560v2#page=7) [PDF, p. 8](https://arxiv.org/pdf/2310.08560v2#page=8)

**Limitations and scope.** In DMR the baseline sees a summary, whereas MemGPT can search the full logs. The key–value task is synthetic. Figure 7 shows depths 0–3, although the text on page 8 gives 0–4. [PDF, p. 5](https://arxiv.org/pdf/2310.08560v2#page=5) [PDF, p. 7](https://arxiv.org/pdf/2310.08560v2#page=7) [PDF, p. 8](https://arxiv.org/pdf/2310.08560v2#page=8)

## Overview

The method manages memory hierarchically and moves information between memory levels when the context window is limited. [PDF, p. 1](https://arxiv.org/pdf/2310.08560v2#page=1)

## Section notes

**Mechanism:** MemGPT models memory hierarchically, as in an operating system. Active context is a limited resource, and the agent can call functions to move information between it and external memory. [PDF, p. 2](https://arxiv.org/pdf/2310.08560v2#page=2) · [PDF, p. 3](https://arxiv.org/pdf/2310.08560v2#page=3)

**Evaluation and study settings:** The paper covers long-document analysis and conversations spanning multiple sessions. [PDF, p. 4](https://arxiv.org/pdf/2310.08560v2#page=4)

**Scope and interpretation:** The result does not imply an infinite context window. Performance depends on how the system moves and retrieves information from memory. [PDF, p. 3](https://arxiv.org/pdf/2310.08560v2#page=3) · [PDF, p. 7](https://arxiv.org/pdf/2310.08560v2#page=7)

**Sections checked:** 1 Introduction, Design, Experiments. [Read the paper](https://arxiv.org/html/2310.08560).


[Section and evidence audit](../reviews/audit-2026-11-19/2310.08560v2.md)

## Source files

arXiv version `2310.08560v2` · PDF pages: 13.

- [Original PDF](https://arxiv.org/pdf/2310.08560v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2310.08560.metadata.json)

PDF bookmarks — [Experiments (p. 4)](https://arxiv.org/pdf/2310.08560v2#page=4).

## Related concepts

- [Long-term memory](../concepts/long-term-memory.md)
- [Memory hierarchy](../concepts/memory-hierarchy.md)
- [Context window](../concepts/context-window.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md)
- [Hierarchical retrieval](../concepts/hierarchical-retrieval.md)
- [Source-grounded generation](../concepts/grounded-generation.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.

## Findings and caveats

- [Finding 1 — method](../concepts/finding-2310-08560-1.md)
- [Finding 2 — evaluation](../concepts/finding-2310-08560-2.md)
- [Finding 3 — interpretive caveat](../concepts/finding-2310-08560-3.md)
