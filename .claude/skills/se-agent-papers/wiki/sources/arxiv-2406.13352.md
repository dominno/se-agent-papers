---
type: source
title: "AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents"
created: 2026-11-19
arxiv_id: "2406.13352"
url: "https://arxiv.org/abs/2406.13352"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "prompt-optimization", "rag-evaluation", "evaluation-metrics", "llm-as-judge", "benchmarks", "tool-sandboxing", "prompt-injection", "observability"]
source_path: "raw/papers/2406.13352.md"
sources: ["https://arxiv.org/abs/2406.13352"]
ingested: "2026-11-19"
---

# AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents

**Paper:** [2406.13352](https://arxiv.org/abs/2406.13352) · [PDF](https://arxiv.org/pdf/2406.13352) · [HTML](https://arxiv.org/html/2406.13352)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** Four simulated environments cover 97 user tasks and 629 security test cases. The evaluator separately checks task completion and violation of the specified security property. [PDF, p. 4](https://arxiv.org/pdf/2406.13352v3#page=4) [PDF, p. 6](https://arxiv.org/pdf/2406.13352v3#page=6) [PDF, p. 20](https://arxiv.org/pdf/2406.13352v3#page=20)

**Key result.** In Table 5, tool filtering for GPT-4o reduced targeted violations to 6.84% (±2.0 percentage points, 95% CI), compared with 57.69% without a defense. Utility under attack was 56.28% and 50.01%, respectively. [PDF, p. 20](https://arxiv.org/pdf/2406.13352v3#page=20)

**Limitations and scope.** Effectiveness depends on the task and the permissions it requires. When the necessary tools cannot be planned in advance, filtering can reduce utility. [PDF, p. 9](https://arxiv.org/pdf/2406.13352v3#page=9)

[Audit of sections, tables and appendices](../reviews/audit-2026-11-19/2406.13352v3.md)

## Overview

The environment tests agents' resilience to prompt injection in external content and tool outputs. [PDF, p. 1](https://arxiv.org/pdf/2406.13352v3#page=1)

## Source files

arXiv version `2406.13352v3` · PDF pages: 26.

- [Original PDF](https://arxiv.org/pdf/2406.13352v3)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2406.13352.metadata.json)

PDF bookmarks — [Evaluation (p. 6)](https://arxiv.org/pdf/2406.13352v3#page=6).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Prompt optimization](../concepts/prompt-optimization.md)
- [RAG evaluation](../concepts/rag-evaluation.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [LLM-as-a-Judge](../concepts/llm-as-judge.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Tool sandbox](../concepts/tool-sandboxing.md)
- [Prompt injection](../concepts/prompt-injection.md)
- [Agent observability](../concepts/observability.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
