---
type: source
title: "Does mutation testing improve testing practices?"
created: 2026-11-19
arxiv_id: "2103.07189"
url: "https://arxiv.org/abs/2103.07189"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["benchmarks", "unit-testing", "mutation-testing", "regression-testing", "evaluation-metrics"]
source_path: "raw/papers/2103.07189.md"
sources: ["https://arxiv.org/abs/2103.07189"]
ingested: "2026-11-19"
---

# Does mutation testing improve testing practices?

**Paper:** [2103.07189](https://arxiv.org/abs/2103.07189) · [PDF](https://arxiv.org/pdf/2103.07189) · [HTML](https://arxiv.org/html/2103.07189)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** In Google projects, the authors compared files exposed to mutation-testing results with files exposed to coverage feedback alone. They also replayed mutations before and after 1,502 high-priority bug fixes in four languages. [PDF, p. 3](https://arxiv.org/pdf/2103.07189v1#page=3) [PDF, p. 7](https://arxiv.org/pdf/2103.07189v1#page=7) [PDF, p. 8](https://arxiv.org/pdf/2103.07189v1#page=8)

**Key result.** File exposure to mutation testing correlated with the mean number of modified test hunks (ρ = 0.90) and with mutant survival (ρ = −0.50). For 1,043/1,502 defects (69.44%), the authors identified a mutant killed by the test that exposed the defect. [PDF, p. 4](https://arxiv.org/pdf/2103.07189v1#page=4) [PDF, p. 6](https://arxiv.org/pdf/2103.07189v1#page=6) [PDF, p. 8](https://arxiv.org/pdf/2103.07189v1#page=8)

**Limitations and scope.** Projects participated voluntarily. The file was the unit of exposure. The defect analysis excluded changes with more than 500 test targets, among other exclusions. A link to a regression test indicates that review could potentially have detected the defect. [PDF, p. 2](https://arxiv.org/pdf/2103.07189v1#page=2) [PDF, p. 7](https://arxiv.org/pdf/2103.07189v1#page=7) [PDF, p. 8](https://arxiv.org/pdf/2103.07189v1#page=8) [PDF, p. 10](https://arxiv.org/pdf/2103.07189v1#page=10)

[Audit of sections, tables and appendices](../reviews/audit-2026-11-19/2103.07189v1.md)

## Overview

The study tests whether introducing code mutations reveals gaps in test suites and improves testing practices. [PDF, p. 1](https://arxiv.org/pdf/2103.07189v1#page=1)

## Source files

arXiv version `2103.07189v1` · PDF pages: 12.

- [Original PDF](https://arxiv.org/pdf/2103.07189v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2103.07189.metadata.json)

PDF bookmarks — [V Threats To Validity (p. 10)](https://arxiv.org/pdf/2103.07189v1#page=10).

## Related concepts

- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Unit tests](../concepts/unit-testing.md)
- [Mutation testing](../concepts/mutation-testing.md)
- [Regression tests](../concepts/regression-testing.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
