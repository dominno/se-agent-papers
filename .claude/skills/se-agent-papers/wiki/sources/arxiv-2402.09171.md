---
type: source
title: "Automated Unit Test Improvement using Large Language Models at Meta"
created: 2026-11-19
arxiv_id: "2402.09171"
url: "https://arxiv.org/abs/2402.09171"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["benchmarks", "unit-testing", "evaluation-metrics"]
source_path: "raw/papers/2402.09171.md"
sources: ["https://arxiv.org/abs/2402.09171"]
ingested: "2026-11-19"
---

# Automated Unit Test Improvement using Large Language Models at Meta

**Paper:** [2402.09171](https://arxiv.org/abs/2402.09171) · [PDF](https://arxiv.org/pdf/2402.09171) · [HTML](https://arxiv.org/html/2402.09171)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** TestGen-LLM extends existing Kotlin test classes. A candidate must compile, pass five runs and increase line coverage over the existing build target. [PDF, p. 2](https://arxiv.org/pdf/2402.09171v1#page=2) [PDF, p. 3](https://arxiv.org/pdf/2402.09171v1#page=3) [PDF, p. 6](https://arxiv.org/pdf/2402.09171v1#page=6)

**Key result.** Among 86 Reels and Stories components, 75% of classes received at least one test that compiled, 57% at least one that passed consistently and 25% at least one that increased coverage. Separately, across three deployments, Section 4 reports improvement in 196/1,979 classes (9.90%). The abstract gives 11.5%. [PDF, p. 1](https://arxiv.org/pdf/2402.09171v1#page=1) [PDF, p. 6](https://arxiv.org/pdf/2402.09171v1#page=6) [PDF, p. 7](https://arxiv.org/pdf/2402.09171v1#page=7)

**Limitations and scope.** Greater line coverage does not directly measure better fault detection. In the November deployment, an engineer rejected a test that passed the filters and increased coverage but contained no assertions. [PDF, p. 5](https://arxiv.org/pdf/2402.09171v1#page=5) [PDF, p. 10](https://arxiv.org/pdf/2402.09171v1#page=10)

[Section and table audit for 2402.09171v1](../reviews/audit-2026-11-19/2402.09171v1.md)

## Overview

The study describes how a language model extends existing tests in an industrial setting. Candidates are filtered for compilation, stable execution and increased coverage. [PDF, p. 1](https://arxiv.org/pdf/2402.09171v1#page=1)

## Source files

**Paper license notice.** The arXiv record lists CC BY 4.0. The first page also carries an ACM notice on personal and classroom copying and other uses. [PDF, p. 1](https://arxiv.org/pdf/2402.09171v1#page=1)

arXiv version `2402.09171v1` · PDF pages: 12.

- [Original PDF](https://arxiv.org/pdf/2402.09171v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2402.09171.metadata.json)

PDF bookmarks — [4 Quantitative results from deployment (p. 7)](https://arxiv.org/pdf/2402.09171v1#page=7).

## Related concepts

- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Unit tests](../concepts/unit-testing.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
