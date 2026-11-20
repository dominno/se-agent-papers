---
type: source
title: "SWE-Synth: Synthesizing Verifiable Bug-Fix Data to Enable Large Language Models in Resolving Real-World Bugs"
created: 2026-11-19
arxiv_id: "2504.14757"
url: "https://arxiv.org/abs/2504.14757"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "coding-agents", "debugging", "evaluation-metrics", "benchmarks", "comparison-and-reproducibility"]
source_path: "raw/papers/2504.14757.md"
sources: ["https://arxiv.org/abs/2504.14757"]
ingested: "2026-11-19"
---

# SWE-Synth: Synthesizing Verifiable Bug-Fix Data to Enable Large Language Models in Resolving Real-World Bugs

**Paper:** [2504.14757](https://arxiv.org/abs/2504.14757) · [PDF](https://arxiv.org/pdf/2504.14757) · [HTML](https://arxiv.org/html/2504.14757)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** An LLM reimplements a component of a working project. Existing tests detect deviations, and verified repair trajectories provide fine-tuning data. The authors collected 9,459 variants across seven Python projects. [PDF, p. 4](https://arxiv.org/pdf/2504.14757v2#page=4) [PDF, p. 6](https://arxiv.org/pdf/2504.14757v2#page=6) [PDF, p. 8](https://arxiv.org/pdf/2504.14757v2#page=8) [PDF, p. 9](https://arxiv.org/pdf/2504.14757v2#page=9)

**Key result.** For Qwen2.5-Coder-14B on SWE-bench Lite, the best result after training on synthetic data was 15.3% resolved, compared with 13.0% after training on SWE-Gym Full, a gain of 2.3 percentage points. [PDF, p. 13](https://arxiv.org/pdf/2504.14757v2#page=13) [PDF, p. 14](https://arxiv.org/pdf/2504.14757v2#page=14)

**Limitations and scope.** The scaling comparison varies both the number and the selection of examples. Passing the tests does not imply success on the authors' separate correctness measure. [PDF, p. 11](https://arxiv.org/pdf/2504.14757v2#page=11) [PDF, p. 12](https://arxiv.org/pdf/2504.14757v2#page=12) [PDF, p. 13](https://arxiv.org/pdf/2504.14757v2#page=13) [PDF, p. 18](https://arxiv.org/pdf/2504.14757v2#page=18)

[Audit of sections, tables and appendices](../reviews/audit-2026-11-19/2504.14757v2.md)

## Overview

The study describes synthetic generation of code-repair tasks, executable verification and data for model development. [PDF, p. 1](https://arxiv.org/pdf/2504.14757v2#page=1)

## Source files

arXiv version `2504.14757v2` · PDF pages: 27.

- [Original PDF](https://arxiv.org/pdf/2504.14757v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2504.14757.metadata.json)

PDF bookmarks — [Empirical evaluation (p. 10)](https://arxiv.org/pdf/2504.14757v2#page=10).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Coding agents](../concepts/coding-agents.md)
- [Debugging](../concepts/debugging.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
