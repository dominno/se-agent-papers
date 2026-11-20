---
type: source
title: "RepoCoder: Repository-Level Code Completion Through Iterative Retrieval and Generation"
created: 2026-11-19
arxiv_id: "2303.12570"
url: "https://arxiv.org/abs/2303.12570"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["coding-agents", "repository-context", "retrieval-augmented-generation", "rag-evaluation", "llm-as-judge", "benchmarks", "unit-testing", "evaluation-metrics"]
source_path: "raw/papers/2303.12570.md"
sources: ["https://arxiv.org/abs/2303.12570"]
ingested: "2026-11-19"
---

# RepoCoder: Repository-Level Code Completion Through Iterative Retrieval and Generation

**Paper:** [2303.12570](https://arxiv.org/abs/2303.12570) · [PDF](https://arxiv.org/pdf/2303.12570) · [HTML](https://arxiv.org/html/2303.12570)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** RepoCoder first retrieves repository code similar to the context in the open file, then adds part of a generated continuation to the query and repeats generation. RepoEval distinguishes line, API-call and function-body completion. [PDF, p. 3](https://arxiv.org/pdf/2303.12570v3#page=3) [PDF, p. 4](https://arxiv.org/pdf/2303.12570v3#page=4) [PDF, p. 5](https://arxiv.org/pdf/2303.12570v3#page=5)

**Key result.** Across 1,600 API calls, GPT-3.5-Turbo achieved 49.19% exact match after two rounds, compared with 47.69% after one round and 34.06% with only the current file. Across 373 function bodies, 42.63% passed tests after two rounds, compared with 38.34% after one and 23.32% with only the current file. Appendix D confirms the second-round API score with 787 matches. [PDF, p. 6](https://arxiv.org/pdf/2303.12570v3#page=6) [PDF, p. 13](https://arxiv.org/pdf/2303.12570v3#page=13)

**Limitations and scope.** Tables 2b and 8 disagree about the third and fourth rounds for GPT-3.5-Turbo on the API task. Additional rounds can lose correct matches and increase latency. Exact match excludes equivalent formulations. [PDF, p. 6](https://arxiv.org/pdf/2303.12570v3#page=6) [PDF, p. 9](https://arxiv.org/pdf/2303.12570v3#page=9) [PDF, p. 13](https://arxiv.org/pdf/2303.12570v3#page=13)

[Audit of sections, tables and appendices](../reviews/audit-2026-11-19/2303.12570v3.md)

## Overview

The method iteratively retrieves related code and completes implementations across a repository. [PDF, p. 1](https://arxiv.org/pdf/2303.12570v3#page=1)

## Source files

arXiv version `2303.12570v3` · PDF pages: 14.

- [Original PDF](https://arxiv.org/pdf/2303.12570v3)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2303.12570.metadata.json)

## Related concepts

- [Coding agents](../concepts/coding-agents.md)
- [Repository context](../concepts/repository-context.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md)
- [RAG evaluation](../concepts/rag-evaluation.md)
- [LLM-as-a-Judge](../concepts/llm-as-judge.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Unit tests](../concepts/unit-testing.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
