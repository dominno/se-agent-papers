---
type: source
title: "ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs"
created: 2026-11-19
arxiv_id: "2307.16789"
url: "https://arxiv.org/abs/2307.16789"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "benchmarks", "stateful-tool-use", "tool-evaluation", "tool-sandboxing"]
source_path: "raw/papers/2307.16789.md"
sources: ["https://arxiv.org/abs/2307.16789"]
ingested: "2026-11-19"
---

# ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs

**Paper:** [2307.16789](https://arxiv.org/abs/2307.16789) · [PDF](https://arxiv.org/pdf/2307.16789) · [HTML](https://arxiv.org/html/2307.16789)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** Using interfaces from RapidAPI, ChatGPT generated instructions and API-call trajectories. These data were used to fine-tune LLaMA-2 7B and train an API retriever. ToolEval assesses task completion and preference between solutions. [PDF, p. 3](https://arxiv.org/pdf/2307.16789v2#page=3) [PDF, p. 4](https://arxiv.org/pdf/2307.16789v2#page=4) [PDF, p. 6](https://arxiv.org/pdf/2307.16789v2#page=6) [PDF, p. 7](https://arxiv.org/pdf/2307.16789v2#page=7)

**Key result.** With the same DFSDT strategy and the correct API set supplied, mean pass rates were 66.7% for ToolLLaMA and 64.8% for ChatGPT. Against the same ChatGPT-ReAct baseline, their respective preference scores were 60.0% and 64.3%. [PDF, p. 8](https://arxiv.org/pdf/2307.16789v2#page=8)

**Limitations and scope.** On transfer to HuggingFace, ToolLLaMA AST accuracy rose from 16.77% to 88.80% when the correct API was supplied in place of retrieval. The automated judge agreed with humans on 80.3% of pairwise comparisons. [PDF, p. 9](https://arxiv.org/pdf/2307.16789v2#page=9) [PDF, p. 16](https://arxiv.org/pdf/2307.16789v2#page=16)

[Audit of sections, tables and appendices](../reviews/audit-2026-11-19/2307.16789v2.md)

## Overview

ToolBench provides methods for training and evaluating agents that call real APIs. [PDF, p. 1](https://arxiv.org/pdf/2307.16789v2#page=1)

## Source files

arXiv version `2307.16789v2` · PDF pages: 24.

- [Original PDF](https://arxiv.org/pdf/2307.16789v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2307.16789.metadata.json)

PDF bookmarks — [Dataset Construction (p. 3)](https://arxiv.org/pdf/2307.16789v2#page=3) · [Experiments (p. 6)](https://arxiv.org/pdf/2307.16789v2#page=6).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Stateful tool use](../concepts/stateful-tool-use.md)
- [Tool evaluation](../concepts/tool-evaluation.md)
- [Tool sandbox](../concepts/tool-sandboxing.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
