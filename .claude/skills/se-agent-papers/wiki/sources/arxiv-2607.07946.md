---
type: source
title: "DeepSWE: Measuring Frontier Coding Agents on Original, Long-Horizon Engineering Tasks"
created: 2026-11-19
arxiv_id: "2607.07946"
url: "https://arxiv.org/abs/2607.07946"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "coding-agents", "context-window", "evaluation-metrics", "benchmarks", "long-horizon-development", "comparison-and-reproducibility"]
source_path: "raw/papers/2607.07946.md"
sources: ["https://arxiv.org/abs/2607.07946"]
ingested: "2026-11-19"
---

# DeepSWE: Measuring Frontier Coding Agents on Original, Long-Horizon Engineering Tasks

**Paper:** [2607.07946](https://arxiv.org/abs/2607.07946) · [PDF](https://arxiv.org/pdf/2607.07946) · [HTML](https://arxiv.org/html/2607.07946)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** The authors built 113 new tasks for 91 repositories. Independent, hidden behavioral tests evaluate solutions without referring to the public reference patch. [PDF, p. 5](https://arxiv.org/pdf/2607.07946v1#page=5) [PDF, p. 6](https://arxiv.org/pdf/2607.07946v1#page=6) [PDF, p. 8](https://arxiv.org/pdf/2607.07946v1#page=8) [PDF, p. 9](https://arxiv.org/pdf/2607.07946v1#page=9)

**Key result.** The verifier and a second judge disagreed on 10/735 DeepSWE runs (1.4%, 95% CI 0.7–2.5%) and 256/789 SWE-Bench Pro runs (32.4%, 95% CI 29.2–35.8%). [PDF, p. 8](https://arxiv.org/pdf/2607.07946v1#page=8)

**Limitations and scope.** A language model served as the judge, so disagreement does not establish the absolute error rate of its judgments. The main results use one shared environment and exclude infrastructure failures. [PDF, p. 8](https://arxiv.org/pdf/2607.07946v1#page=8) [PDF, p. 11](https://arxiv.org/pdf/2607.07946v1#page=11) [PDF, p. 13](https://arxiv.org/pdf/2607.07946v1#page=13) [PDF, p. 19](https://arxiv.org/pdf/2607.07946v1#page=19)

[Section and table audit for 2607.07946v1](../reviews/audit-2026-11-19/2607.07946v1.md)

## Overview

The authors introduce research tasks for evaluating agents on long-horizon engineering work. [PDF, p. 1](https://arxiv.org/pdf/2607.07946v1#page=1)

## Source files

arXiv version `2607.07946v1` · PDF pages: 32.

- [Original PDF](https://arxiv.org/pdf/2607.07946v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2607.07946.metadata.json)

PDF bookmarks — [Results (p. 13)](https://arxiv.org/pdf/2607.07946v1#page=13) · [Limitations (p. 19)](https://arxiv.org/pdf/2607.07946v1#page=19).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Coding agents](../concepts/coding-agents.md)
- [Context window](../concepts/context-window.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Long-term software evolution](../concepts/long-horizon-development.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
