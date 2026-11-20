---
type: source
title: "Promptbreeder: Self-Referential Self-Improvement Via Prompt Evolution"
created: 2026-11-19
arxiv_id: "2309.16797"
url: "https://arxiv.org/abs/2309.16797"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["self-evolution", "prompt-optimization", "workflow-optimization"]
source_path: "raw/papers/2309.16797.md"
sources: ["https://arxiv.org/abs/2309.16797"]
ingested: "2026-11-19"
---

# Promptbreeder: Self-Referential Self-Improvement Via Prompt Evolution

**Paper:** [2309.16797](https://arxiv.org/abs/2309.16797) · [PDF](https://arxiv.org/pdf/2309.16797) · [HTML](https://arxiv.org/html/2309.16797)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** The population includes task-solving instructions and instructions for mutating them. PaLM 2-L proposes variants, which are evaluated on batches of labeled training examples. [PDF, p. 5](https://arxiv.org/pdf/2309.16797v1#page=5) [PDF, p. 6](https://arxiv.org/pdf/2309.16797v1#page=6) [PDF, p. 7](https://arxiv.org/pdf/2309.16797v1#page=7) [PDF, p. 8](https://arxiv.org/pdf/2309.16797v1#page=8)

**Key result.** On zero-shot GSM8K, Promptbreeder achieved 83.9%, versus 80.2% for OPRO and 77.9% for APE, all using PaLM 2-L. On 24 instruction-induction tasks, the few-shot columns show 10 wins, 11 ties and 3 losses against APE. [PDF, p. 2](https://arxiv.org/pdf/2309.16797v1#page=2) [PDF, p. 35](https://arxiv.org/pdf/2309.16797v1#page=35) [PDF, p. 36](https://arxiv.org/pdf/2309.16797v1#page=36)

**Limitations and scope.** Selection requires domain data and an evaluation function. Some baselines in Table 1 used a different model. For four datasets, PB used its own split into two halves. [PDF, p. 2](https://arxiv.org/pdf/2309.16797v1#page=2) [PDF, p. 5](https://arxiv.org/pdf/2309.16797v1#page=5) [PDF, p. 25](https://arxiv.org/pdf/2309.16797v1#page=25)

## Overview

The method evolves sets of prompts while also improving the instructions that generate new variants. [PDF, p. 1](https://arxiv.org/pdf/2309.16797v1#page=1)

[Section and evidence audit](../reviews/audit-2026-11-19/2309.16797v1.md)

## Source files

arXiv version `2309.16797v1` · PDF pages: 64.

- [Original PDF](https://arxiv.org/pdf/2309.16797v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2309.16797.metadata.json)

PDF bookmarks — [Experiments (p. 8)](https://arxiv.org/pdf/2309.16797v1#page=8).

## Related concepts

- [Agent self-improvement](../concepts/self-evolution.md)
- [Prompt optimization](../concepts/prompt-optimization.md)
- [Workflow optimization](../concepts/workflow-optimization.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
