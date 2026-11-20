---
type: source
title: "TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks"
created: 2026-11-19
arxiv_id: "2412.14161"
url: "https://arxiv.org/abs/2412.14161"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "coding-agents", "evaluation-metrics", "benchmarks", "comparison-and-reproducibility", "tool-sandboxing"]
source_path: "raw/papers/2412.14161.md"
sources: ["https://arxiv.org/abs/2412.14161"]
ingested: "2026-11-19"
---

# TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks

**Paper:** [2412.14161](https://arxiv.org/abs/2412.14161) · [PDF](https://arxiv.org/pdf/2412.14161) · [HTML](https://arxiv.org/html/2412.14161)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** Agents completed 175 tasks in a simulated company. The evaluator measures full completion and a separate score that combines checkpoint progress with a completion bonus. [PDF, p. 4](https://arxiv.org/pdf/2412.14161v3#page=4) [PDF, p. 5](https://arxiv.org/pdf/2412.14161v3#page=5) [PDF, p. 7](https://arxiv.org/pdf/2412.14161v3#page=7)

**Key result.** Gemini 2.5 Pro in OpenHands 0.28.1 completed 30.3% of tasks, about 53 of 175. Its score including partial credit was 39.3%, and its mean cost was $4.20 per task. [PDF, p. 7](https://arxiv.org/pdf/2412.14161v3#page=7)

**Limitations and scope.** The sample is limited to work that can be evaluated automatically. The authors did not measure human performance, and some model comparisons used different OpenHands versions. [PDF, p. 7](https://arxiv.org/pdf/2412.14161v3#page=7) [PDF, p. 9](https://arxiv.org/pdf/2412.14161v3#page=9) [PDF, p. 10](https://arxiv.org/pdf/2412.14161v3#page=10)

[Audit of sections, tables and appendices](../reviews/audit-2026-11-19/2412.14161v3.md)

## Overview

The environment simulates digital work in a small company, including web browsing, programming and communicating with colleagues. [PDF, p. 1](https://arxiv.org/pdf/2412.14161v3#page=1)

## Source files

arXiv version `2412.14161v3` · PDF pages: 24.

- [Original PDF](https://arxiv.org/pdf/2412.14161v3)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2412.14161.metadata.json)

PDF bookmarks — [Experimental Results (p. 7)](https://arxiv.org/pdf/2412.14161v3#page=7).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Coding agents](../concepts/coding-agents.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)
- [Tool sandbox](../concepts/tool-sandboxing.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
