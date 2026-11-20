---
type: source
title: "ViBench 2.0: A Benchmark for Long-Horizon Software Building"
created: 2026-11-19
arxiv_id: "2611.05620"
url: "https://arxiv.org/abs/2611.05620"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "context-window", "evaluation-metrics", "benchmarks", "long-horizon-development", "comparison-and-reproducibility"]
source_path: "raw/papers/2611.05620.md"
sources: ["https://arxiv.org/abs/2611.05620"]
ingested: "2026-11-19"
---

# ViBench 2.0: A Benchmark for Long-Horizon Software Building

**Paper:** [2611.05620](https://arxiv.org/abs/2611.05620) · [PDF](https://arxiv.org/pdf/2611.05620) · [HTML](https://arxiv.org/html/2611.05620)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** Each of nine models built four independent versions of each of 17 products. Requirements were disclosed in stages. Browser-based test plans assessed the final application. When a plan returned no verdict, the product was scored on its remaining plans. [PDF, p. 2](https://arxiv.org/pdf/2611.05620v1#page=2) [PDF, p. 4](https://arxiv.org/pdf/2611.05620v1#page=4) [PDF, p. 5](https://arxiv.org/pdf/2611.05620v1#page=5) [PDF, p. 13](https://arxiv.org/pdf/2611.05620v1#page=13)

**Key result.** GPT-6.1 Sol achieved the highest whole-product pass rate (44/68 = 64.7%) and passed 96.9% of plans. GPT-6 Astra achieved the highest plan pass rate, 98.0%, and passed 60.3% of whole builds. The models’ 95% intervals for pass@1 overlapped. [PDF, p. 5](https://arxiv.org/pdf/2611.05620v1#page=5) [PDF, p. 17](https://arxiv.org/pdf/2611.05620v1#page=17) [PDF, p. 18](https://arxiv.org/pdf/2611.05620v1#page=18)

**Limitations and scope.** Eight of the 17 products are publicly available. Scoring evaluates functionality through the interface. Judge validation covered 96 assessments with a visible defect. All three checks were excluded for one of the 34 seeded defects. [PDF, p. 6](https://arxiv.org/pdf/2611.05620v1#page=6) [PDF, p. 7](https://arxiv.org/pdf/2611.05620v1#page=7) [PDF, p. 14](https://arxiv.org/pdf/2611.05620v1#page=14)

[Audit of sections, tables and appendices](../reviews/audit-2026-11-19/2611.05620v1.md)

## Overview

The benchmark evaluates complete applications developed across multiple feature requests, with final product behavior tested in the browser. [PDF, p. 1](https://arxiv.org/pdf/2611.05620v1#page=1)

## Source files

arXiv version `2611.05620v1` · PDF pages: 18.

- [Original PDF](https://arxiv.org/pdf/2611.05620v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2611.05620.metadata.json)

PDF bookmarks — [Results (p. 5)](https://arxiv.org/pdf/2611.05620v1#page=5).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Context window](../concepts/context-window.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Long-term software evolution](../concepts/long-horizon-development.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
