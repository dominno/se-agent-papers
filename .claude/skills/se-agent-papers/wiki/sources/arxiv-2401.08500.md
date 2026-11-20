---
type: source
title: "Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering"
created: 2026-11-19
arxiv_id: "2401.08500"
url: "https://arxiv.org/abs/2401.08500"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["coding-agents", "prompt-optimization", "workflow-optimization", "benchmarks", "unit-testing", "evaluation-metrics"]
source_path: "raw/papers/2401.08500.md"
sources: ["https://arxiv.org/abs/2401.08500"]
ingested: "2026-11-19"
---

# Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering

**Paper:** [2401.08500](https://arxiv.org/abs/2401.08500) · [PDF](https://arxiv.org/pdf/2401.08500) · [HTML](https://arxiv.org/html/2401.08500)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** AlphaCodium guides a model through problem analysis, test generation and iterative program refinement. [PDF, p. 1](https://arxiv.org/pdf/2401.08500v1#page=1)

**Key result.** On 107 CodeContests validation tasks, GPT-4 achieved 44% pass@5 with AlphaCodium and 19% pass@5 with direct prompting. On 165 test tasks, the corresponding scores were 29% and 12%. Both variants allow five candidates per problem for pass@5. [PDF, p. 3](https://arxiv.org/pdf/2401.08500v1#page=3) [PDF, p. 7](https://arxiv.org/pdf/2401.08500v1#page=7)

**Limitations and scope.** The data come from competitive programming. Pass@5 allows five candidates and does not measure the probability that an agent's first change to an application is correct. [PDF, p. 1](https://arxiv.org/pdf/2401.08500v1#page=1)

[Audit report for 2401.08500v1](../reviews/audit-2026-11-19/2401.08500v1.md)

## Overview

The authors use a multi-stage, test-driven workflow to generate and revise code in place of a single prompt. [PDF, p. 1](https://arxiv.org/pdf/2401.08500v1#page=1)

## Source files

arXiv version `2401.08500v1` · PDF pages: 10.

- [Original PDF](https://arxiv.org/pdf/2401.08500v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2401.08500.metadata.json)

## Related concepts

- [Coding agents](../concepts/coding-agents.md)
- [Prompt optimization](../concepts/prompt-optimization.md)
- [Workflow optimization](../concepts/workflow-optimization.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Unit tests](../concepts/unit-testing.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
