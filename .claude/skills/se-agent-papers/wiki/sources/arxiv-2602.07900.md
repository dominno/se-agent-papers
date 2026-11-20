---
type: source
title: "Rethinking the Value of Agent-Generated Tests for LLM-Based Software Engineering Agents"
created: 2026-11-19
arxiv_id: "2602.07900"
url: "https://arxiv.org/abs/2602.07900"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "coding-agents", "benchmarks", "unit-testing", "evaluation-metrics"]
source_path: "raw/papers/2602.07900.md"
sources: ["https://arxiv.org/abs/2602.07900"]
ingested: "2026-11-19"
---

# Rethinking the Value of Agent-Generated Tests for LLM-Based Software Engineering Agents

**Paper:** [2602.07900](https://arxiv.org/abs/2602.07900) · [PDF](https://arxiv.org/pdf/2602.07900) · [HTML](https://arxiv.org/html/2602.07900)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** The authors examined 5,000 mini-SWE-agent trajectories. The baseline comprised 3,000 attempts by six models on the same 500 SWE-bench Verified tasks. A further 2,000 attempts used four models with a revised instruction about writing new test files. [PDF, p. 2](https://arxiv.org/pdf/2602.07900v3#page=2) [PDF, p. 3](https://arxiv.org/pdf/2602.07900v3#page=3)

**Key result.** After the instruction change, the four models solved 0, 5, 13 and 9 fewer tasks out of 500, respectively. No comparison reached significance in an exact McNemar test with Holm correction. For GPT-5.2, a net change of zero included 27 newly solved tasks and 27 previously solved tasks lost. [PDF, p. 8](https://arxiv.org/pdf/2602.07900v3#page=8) [PDF, p. 9](https://arxiv.org/pdf/2602.07900v3#page=9) [PDF, p. 10](https://arxiv.org/pdf/2602.07900v3#page=10)

**Limitations and scope.** Each condition was observed once per task. Some comparisons used different harness versions or API access. The confidence intervals include practically important declines, such as −6.4 to +1.2 percentage points for Kimi. [PDF, p. 8](https://arxiv.org/pdf/2602.07900v3#page=8) [PDF, p. 9](https://arxiv.org/pdf/2602.07900v3#page=9)

[Audit of sections, tables and appendices](../reviews/audit-2026-11-19/2602.07900v3.md)

## Overview

The study examines the value of agent-generated tests and the limits of increasing test counts alone. [PDF, p. 1](https://arxiv.org/pdf/2602.07900v3#page=1)

## Source files

arXiv version `2602.07900v3` · PDF pages: 12.

- [Original PDF](https://arxiv.org/pdf/2602.07900v3)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2602.07900.metadata.json)

PDF bookmarks — [Methodology (p. 2)](https://arxiv.org/pdf/2602.07900v3#page=2).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Coding agents](../concepts/coding-agents.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Unit tests](../concepts/unit-testing.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
