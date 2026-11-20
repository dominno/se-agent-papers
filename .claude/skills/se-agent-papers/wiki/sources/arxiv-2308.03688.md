---
type: source
title: "AgentBench: Evaluating LLMs as Agents"
created: 2026-11-19
arxiv_id: "2308.03688"
url: "https://arxiv.org/abs/2308.03688"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "task-planning", "rag-evaluation", "evaluation-metrics", "llm-as-judge", "benchmarks", "tool-evaluation"]
source_path: "raw/papers/2308.03688.md"
sources: ["https://arxiv.org/abs/2308.03688"]
ingested: "2026-11-19"
---

# AgentBench: Evaluating LLMs as Agents

**Paper:** [2308.03688](https://arxiv.org/abs/2308.03688) · [PDF](https://arxiv.org/pdf/2308.03688) · [HTML](https://arxiv.org/html/2308.03688)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** AgentBench evaluates 29 models in eight environments with actions, observations and interaction limits. Its overall OA score is a weighted aggregate of environment-specific metrics. [PDF, p. 3](https://arxiv.org/pdf/2308.03688v3#page=3) [PDF, p. 5](https://arxiv.org/pdf/2308.03688v3#page=5) [PDF, p. 6](https://arxiv.org/pdf/2308.03688v3#page=6) [PDF, p. 7](https://arxiv.org/pdf/2308.03688v3#page=7)

**Key result.** In Table 3, GPT-4-0613 scored 4.01 on OA, compared with 3.11 for Claude 3 Opus. In the database environment Claude Opus led, 51.7 to 32.0. [PDF, p. 7](https://arxiv.org/pdf/2308.03688v3#page=7)

**Limitations and scope.** The mean score does not distinguish an invalid action, a formatting error and an exhausted budget. In the household environment, invalid actions accounted for 64.1% of terminations, averaged over models. [PDF, p. 8](https://arxiv.org/pdf/2308.03688v3#page=8) [PDF, p. 45](https://arxiv.org/pdf/2308.03688v3#page=45) [PDF, p. 46](https://arxiv.org/pdf/2308.03688v3#page=46)

[Section and table audit for 2308.03688v3](../reviews/audit-2026-11-19/2308.03688v3.md)

## Overview

The study compares agent reasoning and decisions across eight interactive environments and identifies recurring causes of failure. [PDF, p. 1](https://arxiv.org/pdf/2308.03688v3#page=1)

## Source files

arXiv version `2308.03688v3` · PDF pages: 58.

- [Original PDF](https://arxiv.org/pdf/2308.03688v3)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2308.03688.metadata.json)

PDF bookmarks — [Evaluation of AgentBench (p. 5)](https://arxiv.org/pdf/2308.03688v3#page=5).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Task planning](../concepts/task-planning.md)
- [RAG evaluation](../concepts/rag-evaluation.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [LLM-as-a-Judge](../concepts/llm-as-judge.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Tool evaluation](../concepts/tool-evaluation.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
