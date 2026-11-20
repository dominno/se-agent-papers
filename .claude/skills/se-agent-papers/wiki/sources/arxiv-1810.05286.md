---
type: source
title: "Predictive Test Selection"
created: 2026-11-19
arxiv_id: "1810.05286"
url: "https://arxiv.org/abs/1810.05286"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["benchmarks", "regression-testing", "unit-testing", "evaluation-metrics"]
source_path: "raw/papers/1810.05286.md"
sources: ["https://arxiv.org/abs/1810.05286"]
ingested: "2026-11-19"
---

# Predictive Test Selection

**Paper:** [1810.05286](https://arxiv.org/abs/1810.05286) · [PDF](https://arxiv.org/pdf/1810.05286) · [HTML](https://arxiv.org/html/1810.05286)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** Gradient-boosted trees score change–test-target pairs in Facebook’s CI. The system combines threshold-based and rank-based selection. For sampled changes, the authors ran every dependent target and investigated failures through reruns. [PDF, p. 5](https://arxiv.org/pdf/1810.05286v2#page=5) [PDF, p. 6](https://arxiv.org/pdf/1810.05286v2#page=6) [PDF, p. 7](https://arxiv.org/pdf/1810.05286v2#page=7)

**Key result.** At change integration, the system selected fewer than 33% of the change-dependent targets and detected over 95% of target failures and over 99.9% of faulty changes. It required roughly one-third as many executions and half as many machines as selection from the dependency graph. [PDF, p. 4](https://arxiv.org/pdf/1810.05286v2#page=4) [PDF, p. 8](https://arxiv.org/pdf/1810.05286v2#page=8)

**Limitations and scope.** Repeated runs can miss flaky behavior. With 15% selection and no filtering of flaky outcomes during training, the combined metric suggested about 90% detection, compared with about 70% for consistent failures. Deployment results include a subsequent full stabilization stage. [PDF, p. 3](https://arxiv.org/pdf/1810.05286v2#page=3) [PDF, p. 7](https://arxiv.org/pdf/1810.05286v2#page=7) [PDF, p. 9](https://arxiv.org/pdf/1810.05286v2#page=9)

## Overview

The study examines how selecting tests relevant to a code change can shorten regression testing. [PDF, p. 1](https://arxiv.org/pdf/1810.05286v2#page=1)

[Section and evidence audit](../reviews/audit-2026-11-19/1810.05286v2.md)

## Source files

arXiv version `1810.05286v2` · PDF pages: 10.

- [Original PDF](https://arxiv.org/pdf/1810.05286v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/1810.05286.metadata.json)

## Related concepts

- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Regression tests](../concepts/regression-testing.md)
- [Unit tests](../concepts/unit-testing.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
