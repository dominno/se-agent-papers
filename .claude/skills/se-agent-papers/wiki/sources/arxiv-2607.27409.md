---
type: source
title: "SWE-NFI: Studying and Benchmarking Coding Agents for Non-Functional Improvements"
created: 2026-11-19
arxiv_id: "2607.27409"
url: "https://arxiv.org/abs/2607.27409"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "coding-agents", "evaluation-metrics", "benchmarks", "architecture-erosion", "comparison-and-reproducibility"]
source_path: "raw/papers/2607.27409.md"
sources: ["https://arxiv.org/abs/2607.27409"]
ingested: "2026-11-19"
---

# SWE-NFI: Studying and Benchmarking Coding Agents for Non-Functional Improvements

**Paper:** [2607.27409](https://arxiv.org/abs/2607.27409) · [PDF](https://arxiv.org/pdf/2607.27409) · [Read the article online](https://arxiv.org/pdf/2607.27409v2)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** SWE-NFI contains 188 tasks from 48 Python projects, with five trials for each of eight configurations. The authors assessed the change in the percentage of rules satisfied for the target quality attribute only after checking syntax and task-specific behavior. [PDF, p. 5](https://arxiv.org/pdf/2607.27409v2#page=5) [PDF, p. 6](https://arxiv.org/pdf/2607.27409v2#page=6)

**Key result.** The highest five-run mean for passing functional checks was 70.0% valid outputs (Claude Code Agent). Individual runs of this configuration reached 71.9%. Mean improvement in the Logic Patterns score ranged from 0.0 to 1.3 percentage points for the agent configurations and was 1.5 points for the human reference. [PDF, p. 8](https://arxiv.org/pdf/2607.27409v2#page=8) [PDF, p. 9](https://arxiv.org/pdf/2607.27409v2#page=9)

**Limitations and scope.** Mean NFI scores include only outputs that passed the task checks. The comparison with historical human changes is descriptive. The dataset was drawn from positively rated changes, and the multi-file subset contains only one Logic Patterns task. [PDF, p. 5](https://arxiv.org/pdf/2607.27409v2#page=5) [PDF, p. 6](https://arxiv.org/pdf/2607.27409v2#page=6) [PDF, p. 11](https://arxiv.org/pdf/2607.27409v2#page=11)

[Audit of sections, tables and appendices](../reviews/audit-2026-11-19/2607.27409v2.md)

## Overview

The study evaluates refactoring and code-quality improvements that preserve required functionality. [PDF, p. 1](https://arxiv.org/pdf/2607.27409v2#page=1)

## Source files

arXiv version `2607.27409v2` · PDF pages: 13.

- [Original PDF](https://arxiv.org/pdf/2607.27409v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2607.27409.metadata.json)

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Coding agents](../concepts/coding-agents.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Architectural erosion](../concepts/architecture-erosion.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
