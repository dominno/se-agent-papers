---
type: source
title: "NL2Repo-Bench: Towards Long-Horizon Repository Generation Evaluation of Coding Agents"
created: 2026-11-19
arxiv_id: "2512.12730"
url: "https://arxiv.org/abs/2512.12730"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "coding-agents", "repository-context", "context-window", "rag-evaluation", "evaluation-metrics", "llm-as-judge", "benchmarks", "long-horizon-development", "stateful-tool-use", "tool-evaluation", "comparison-and-reproducibility"]
source_path: "raw/papers/2512.12730.md"
sources: ["https://arxiv.org/abs/2512.12730"]
ingested: "2026-11-19"
---

# NL2Repo-Bench: Towards Long-Horizon Repository Generation Evaluation of Coding Agents

**Paper:** [2512.12730](https://arxiv.org/abs/2512.12730) · [PDF](https://arxiv.org/pdf/2512.12730) · [HTML](https://arxiv.org/html/2512.12730)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** The agent receives a specification in an empty directory and generates a Python library. The original tests are run independently to evaluate it. The study covered 104 projects in nine categories. [PDF, p. 6](https://arxiv.org/pdf/2512.12730v2#page=6) [PDF, p. 7](https://arxiv.org/pdf/2512.12730v2#page=7) [PDF, p. 8](https://arxiv.org/pdf/2512.12730v2#page=8)

**Key result.** Sonnet-4.5 in Claude Code achieved the highest mean test pass rate, 40.2%. It passed all tests in 3 of 104 projects. Given access to the tests, the agent passed 59.4% of tests and all tests in 18 projects. [PDF, p. 9](https://arxiv.org/pdf/2512.12730v2#page=9) [PDF, p. 18](https://arxiv.org/pdf/2512.12730v2#page=18)

**Limitations and scope.** The test measures reconstruction of libraries from specifications written with access to the original project, without further user consultation. Difficulty is stratified by the length of the original code. [PDF, p. 6](https://arxiv.org/pdf/2512.12730v2#page=6) [PDF, p. 7](https://arxiv.org/pdf/2512.12730v2#page=7) [PDF, p. 8](https://arxiv.org/pdf/2512.12730v2#page=8) [PDF, p. 23](https://arxiv.org/pdf/2512.12730v2#page=23) [PDF, p. 25](https://arxiv.org/pdf/2512.12730v2#page=25)

## Overview

The benchmark evaluates whether agents can generate complete repositories from natural-language requirements. [PDF, p. 1](https://arxiv.org/pdf/2512.12730v2#page=1)

[Section and evidence audit](../reviews/audit-2026-11-19/2512.12730v2.md)

## Source files

arXiv version `2512.12730v2` · PDF pages: 25.

- [Original PDF](https://arxiv.org/pdf/2512.12730v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2512.12730.metadata.json)

PDF bookmarks — [Available Tools in OpenHands CodeAct Framework (p. 23)](https://arxiv.org/pdf/2512.12730v2#page=23) · [Experiments (p. 7)](https://arxiv.org/pdf/2512.12730v2#page=7).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Coding agents](../concepts/coding-agents.md)
- [Repository context](../concepts/repository-context.md)
- [Context window](../concepts/context-window.md)
- [RAG evaluation](../concepts/rag-evaluation.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [LLM-as-a-Judge](../concepts/llm-as-judge.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Long-term software evolution](../concepts/long-horizon-development.md)
- [Stateful tool use](../concepts/stateful-tool-use.md)
- [Tool evaluation](../concepts/tool-evaluation.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
