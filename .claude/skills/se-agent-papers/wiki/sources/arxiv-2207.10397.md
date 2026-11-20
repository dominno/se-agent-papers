---
type: source
title: "CodeT: Code Generation with Generated Tests"
created: 2026-11-19
arxiv_id: "2207.10397"
url: "https://arxiv.org/abs/2207.10397"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["coding-agents", "benchmarks", "unit-testing", "evaluation-metrics"]
source_path: "raw/papers/2207.10397.md"
sources: ["https://arxiv.org/abs/2207.10397"]
ingested: "2026-11-19"
---

# CodeT: Code Generation with Generated Tests

**Paper:** [2207.10397](https://arxiv.org/abs/2207.10397) · [PDF](https://arxiv.org/pdf/2207.10397) · [HTML](https://arxiv.org/html/2207.10397)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** CodeT uses the same model to generate programs and tests, groups programs by their execution results, and ranks groups using group size and the number of tests passed. Separate reference tests measure final pass@k. [PDF, p. 2](https://arxiv.org/pdf/2207.10397v2#page=2) [PDF, p. 3](https://arxiv.org/pdf/2207.10397v2#page=3) [PDF, p. 4](https://arxiv.org/pdf/2207.10397v2#page=4) [PDF, p. 5](https://arxiv.org/pdf/2207.10397v2#page=5) [PDF, p. 12](https://arxiv.org/pdf/2207.10397v2#page=12)

**Key result.** On HumanEval with input/output examples removed from the prompts, code-davinci-002 achieved 65.8% pass@1 after CodeT selection, compared with 47.0% for the baseline (+18.8 percentage points). With the original prompts, the figures were 74.8% and 47.6%. [PDF, p. 5](https://arxiv.org/pdf/2207.10397v2#page=5) [PDF, p. 12](https://arxiv.org/pdf/2207.10397v2#page=12)

**Limitations and scope.** Baseline pass@1 uses one greedy generation. CodeT selects among 100 candidates. A group that consistently solves a misinterpreted task can rank first, particularly when edge-case tests are missing. [PDF, p. 5](https://arxiv.org/pdf/2207.10397v2#page=5) [PDF, p. 12](https://arxiv.org/pdf/2207.10397v2#page=12) [PDF, p. 18](https://arxiv.org/pdf/2207.10397v2#page=18) [PDF, p. 19](https://arxiv.org/pdf/2207.10397v2#page=19)

## Overview

The method generates tests for alternative code solutions and uses agreement between outputs to select an implementation. [PDF, p. 1](https://arxiv.org/pdf/2207.10397v2#page=1)

[Section and evidence audit](../reviews/audit-2026-11-19/2207.10397v2.md)

## Source files

arXiv version `2207.10397v2` · PDF pages: 19.

- [Original PDF](https://arxiv.org/pdf/2207.10397v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2207.10397.metadata.json)

PDF bookmarks — [2 Methodology (p. 2)](https://arxiv.org/pdf/2207.10397v2#page=2) · [4 Experimental Results (p. 5)](https://arxiv.org/pdf/2207.10397v2#page=5).

## Related concepts

- [Coding agents](../concepts/coding-agents.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Unit tests](../concepts/unit-testing.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
