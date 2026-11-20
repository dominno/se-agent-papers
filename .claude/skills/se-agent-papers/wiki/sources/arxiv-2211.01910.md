---
type: source
title: "Large Language Models Are Human-Level Prompt Engineers"
created: 2026-11-19
arxiv_id: "2211.01910"
url: "https://arxiv.org/abs/2211.01910"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["prompt-optimization", "workflow-optimization", "benchmarks"]
source_path: "raw/papers/2211.01910.md"
sources: ["https://arxiv.org/abs/2211.01910"]
ingested: "2026-11-19"
---

# Large Language Models Are Human-Level Prompt Engineers

**Paper:** [2211.01910](https://arxiv.org/abs/2211.01910) · [PDF](https://arxiv.org/pdf/2211.01910) · [HTML](https://arxiv.org/html/2211.01910)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** APE generates candidate instructions from demonstrations and selects them using execution scores or the log probability of the correct answer. [PDF, p. 3](https://arxiv.org/pdf/2211.01910v2#page=3) [PDF, p. 4](https://arxiv.org/pdf/2211.01910v2#page=4) [PDF, p. 5](https://arxiv.org/pdf/2211.01910v2#page=5)

**Key result.** Across 24 induction tasks, the interquartile mean was 0.810, compared with 0.749 for human-written instructions. Across the 21 selected BIG-Bench tasks in Table 6, APE won 13, tied four and lost four. [PDF, p. 6](https://arxiv.org/pdf/2211.01910v2#page=6) [PDF, p. 21](https://arxiv.org/pdf/2211.01910v2#page=21)

**Limitations and scope.** The “human-level” result concerns the quality of instructions evaluated using this model. Five tasks were reevaluated after changing hyperparameters. In three of the five, the mean remained slightly below the human baseline. [PDF, p. 6](https://arxiv.org/pdf/2211.01910v2#page=6) [PDF, p. 34](https://arxiv.org/pdf/2211.01910v2#page=34)

[Audit report for 2211.01910v2](../reviews/audit-2026-11-19/2211.01910v2.md)

## Overview

The method automates the generation and evaluation of candidate instructions for a language model. [PDF, p. 1](https://arxiv.org/pdf/2211.01910v2#page=1)

## Source files

arXiv version `2211.01910v2` · PDF pages: 43.

- [Original PDF](https://arxiv.org/pdf/2211.01910v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2211.01910.metadata.json)

PDF bookmarks — [C Additional Results (p. 20)](https://arxiv.org/pdf/2211.01910v2#page=20).

## Related concepts

- [Prompt optimization](../concepts/prompt-optimization.md)
- [Workflow optimization](../concepts/workflow-optimization.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
