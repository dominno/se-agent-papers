---
type: source
title: "TRACE: A Framework for Analyzing and Enhancing Stepwise Reasoning in Vision-Language Models"
created: 2026-11-19
arxiv_id: "2512.05943"
url: "https://arxiv.org/abs/2512.05943"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "evaluation-metrics", "benchmarks", "observability", "comparison-and-reproducibility"]
source_path: "raw/papers/2512.05943.md"
sources: ["https://arxiv.org/abs/2512.05943"]
ingested: "2026-11-19"
---

# TRACE: A Framework for Analyzing and Enhancing Stepwise Reasoning in Vision-Language Models

**Paper:** [2512.05943](https://arxiv.org/abs/2512.05943) · [PDF](https://arxiv.org/pdf/2512.05943) · [HTML](https://arxiv.org/html/2512.05943)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** The model builds a graph of subquestions about the text and image. TRACE compares answers across paths and marks the earliest departure from the majority on a path ending in error. [PDF, p. 3](https://arxiv.org/pdf/2512.05943v3#page=3) [PDF, p. 4](https://arxiv.org/pdf/2512.05943v3#page=4) [PDF, p. 5](https://arxiv.org/pdf/2512.05943v3#page=5)

**Key result.** Across the four model–dataset pairs, correct trajectories had higher mean consistency. For GPT-4.1 on MMMUPro the means were 0.907 for correct trajectories and 0.787 for incorrect ones. [PDF, p. 4](https://arxiv.org/pdf/2512.05943v3#page=4)

**Limitations and scope.** The authors manually checked 5% of the question sets and discarded sets with below-baseline accuracy. Before filtering, GPT-4.1 accuracy fell from 54.3% to 48.2%. The FFS illustration in Table 2 gives conflicting angle values. [PDF, p. 5](https://arxiv.org/pdf/2512.05943v3#page=5) [PDF, p. 8](https://arxiv.org/pdf/2512.05943v3#page=8) [PDF, p. 9](https://arxiv.org/pdf/2512.05943v3#page=9) [PDF, p. 17](https://arxiv.org/pdf/2512.05943v3#page=17)

[Audit of sections, tables and appendices](../reviews/audit-2026-11-19/2512.05943v3.md)

## Overview

The study evaluates detection of incorrect reasoning steps and the consistency of intermediate outputs from vision-language models. [PDF, p. 1](https://arxiv.org/pdf/2512.05943v3#page=1)

## Source files

arXiv version `2512.05943v3` · PDF pages: 19.

- [Original PDF](https://arxiv.org/pdf/2512.05943v3)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2512.05943.metadata.json)

PDF bookmarks — [Methodology (p. 3)](https://arxiv.org/pdf/2512.05943v3#page=3) · [Experiments and Results (p. 5)](https://arxiv.org/pdf/2512.05943v3#page=5).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Agent observability](../concepts/observability.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
