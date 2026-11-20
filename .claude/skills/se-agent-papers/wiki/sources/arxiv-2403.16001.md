---
type: source
title: "Fine-Grained Assertion-Based Test Selection"
created: 2026-11-19
arxiv_id: "2403.16001"
url: "https://arxiv.org/abs/2403.16001"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["benchmarks", "regression-testing", "unit-testing", "evaluation-metrics"]
source_path: "raw/papers/2403.16001.md"
sources: ["https://arxiv.org/abs/2403.16001"]
ingested: "2026-11-19"
---

# Fine-Grained Assertion-Based Test Selection

**Paper:** [2403.16001](https://arxiv.org/abs/2403.16001) · [PDF](https://arxiv.org/pdf/2403.16001) · [HTML](https://arxiv.org/html/2403.16001)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** The method analyzes statements and selects individual assertions relevant to the code change, instead of selecting entire test classes. [PDF, p. 1](https://arxiv.org/pdf/2403.16001v2#page=1)

**Key result.** Across 11 projects, mean analysis and execution time was 74.33 s versus 200.36 s for the full suite and 119.74 s for Ekstazi. Ratios of means give reductions of 62.90% and 37.92%. The HyRTS comparison covers eight projects (77.51 s versus 83.51 s, a 7.18% reduction). Dependency collection time was measured separately. [PDF, p. 7](https://arxiv.org/pdf/2403.16001v2#page=7) [PDF, p. 8](https://arxiv.org/pdf/2403.16001v2#page=8) [PDF, p. 9](https://arxiv.org/pdf/2403.16001v2#page=9)

**Limitations and scope.** The implementation primarily supports JUnit 4 assertions and tools built on JUnit 4. Fine-grained selection does not support multithreaded tests. [PDF, p. 11](https://arxiv.org/pdf/2403.16001v2#page=11)

[Audit report for 2403.16001v2](../reviews/audit-2026-11-19/2403.16001v2.md)

## Overview

The method selects regression tests at assertion granularity to reduce unnecessary test runs. [PDF, p. 1](https://arxiv.org/pdf/2403.16001v2#page=1)

## Source files

arXiv version `2403.16001v2` · PDF pages: 12.

- [Original PDF](https://arxiv.org/pdf/2403.16001v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2403.16001.metadata.json)

PDF bookmarks — [Approach (p. 2)](https://arxiv.org/pdf/2403.16001v2#page=2) · [Evaluation (p. 5)](https://arxiv.org/pdf/2403.16001v2#page=5).

## Related concepts

- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Regression tests](../concepts/regression-testing.md)
- [Unit tests](../concepts/unit-testing.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
