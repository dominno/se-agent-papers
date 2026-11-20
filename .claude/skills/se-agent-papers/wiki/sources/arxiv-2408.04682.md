---
type: source
title: "ToolSandbox: A Stateful, Conversational, Interactive Evaluation Benchmark for LLM Tool Use Capabilities"
created: 2026-11-19
arxiv_id: "2408.04682"
url: "https://arxiv.org/abs/2408.04682"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "rag-evaluation", "evaluation-metrics", "llm-as-judge", "benchmarks", "stateful-tool-use", "tool-evaluation", "tool-sandboxing", "comparison-and-reproducibility"]
source_path: "raw/papers/2408.04682.md"
sources: ["https://arxiv.org/abs/2408.04682"]
ingested: "2026-11-19"
---

# ToolSandbox: A Stateful, Conversational, Interactive Evaluation Benchmark for LLM Tool Use Capabilities

**Paper:** [2408.04682](https://arxiv.org/abs/2408.04682) · [PDF](https://arxiv.org/pdf/2408.04682) · [HTML](https://arxiv.org/html/2408.04682)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** Across 1,032 scenarios, tools share state and the agent interacts with a simulated user. The score matches completed milestones against a dependency graph. Meeting a forbidden condition sets the score to zero. [PDF, p. 3](https://arxiv.org/pdf/2408.04682v2#page=3) [PDF, p. 4](https://arxiv.org/pdf/2408.04682v2#page=4) [PDF, p. 5](https://arxiv.org/pdf/2408.04682v2#page=5)

**Key result.** In Table 5, GPT-4o achieved the highest average similarity score, 73.0, compared with 69.2 for Claude-3-Opus. On tasks with insufficient information they scored 42.0 and 57.3, respectively. The overall means conceal this difference. [PDF, p. 7](https://arxiv.org/pdf/2408.04682v2#page=7)

**Limitations and scope.** The authors manually define required milestones and verify the scenarios. The simulated user still makes mistakes, and some model interfaces limit support for successive tool responses. [PDF, p. 4](https://arxiv.org/pdf/2408.04682v2#page=4) [PDF, p. 10](https://arxiv.org/pdf/2408.04682v2#page=10) [PDF, p. 18](https://arxiv.org/pdf/2408.04682v2#page=18) [PDF, p. 23](https://arxiv.org/pdf/2408.04682v2#page=23)

## Overview

The evaluation covers state-dependent tool use, interactions and intermediate steps in addition to the outcome of an individual command. [PDF, p. 1](https://arxiv.org/pdf/2408.04682v2#page=1)

## Section notes

**Mechanism:** ToolSandbox evaluates multi-step interactions with stateful tools, including conversation and dependencies between actions. [PDF, p. 3](https://arxiv.org/pdf/2408.04682v2#page=3)

**Evaluation and study settings:** The scenarios cover state dependencies, insufficient information, argument canonicalization and multiple tool calls. [PDF, p. 5](https://arxiv.org/pdf/2408.04682v2#page=5) · [PDF, p. 6](https://arxiv.org/pdf/2408.04682v2#page=6)

**Scope and interpretation:** The simulated toolkits and rules cover only a subset of real production systems. [PDF, p. 10](https://arxiv.org/pdf/2408.04682v2#page=10)

**Sections checked:** 2 ToolSandbox Design, 3 Test Scenarios, 4 Evaluation Results, 7 Limitations. [Read the paper](https://arxiv.org/html/2408.04682).


[Section and evidence audit](../reviews/audit-2026-11-19/2408.04682v2.md)

## Source files

arXiv version `2408.04682v2` · PDF pages: 24.

- [Original PDF](https://arxiv.org/pdf/2408.04682v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2408.04682.metadata.json)

PDF bookmarks — [Evaluation Results (p. 6)](https://arxiv.org/pdf/2408.04682v2#page=6) · [Limitations (p. 10)](https://arxiv.org/pdf/2408.04682v2#page=10).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [RAG evaluation](../concepts/rag-evaluation.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [LLM-as-a-Judge](../concepts/llm-as-judge.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Stateful tool use](../concepts/stateful-tool-use.md)
- [Tool evaluation](../concepts/tool-evaluation.md)
- [Tool sandbox](../concepts/tool-sandboxing.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.

## Findings and caveats

- [Finding 1 — method](../concepts/finding-2408-04682-1.md)
- [Finding 2 — evaluation](../concepts/finding-2408-04682-2.md)
- [Finding 3 — interpretive caveat](../concepts/finding-2408-04682-3.md)
