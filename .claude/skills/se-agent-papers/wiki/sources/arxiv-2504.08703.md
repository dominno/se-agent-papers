---
type: source
title: "SWE-PolyBench: A Multi-Language Benchmark for Repository-Level Evaluation of Coding Agents"
created: 2026-11-19
arxiv_id: "2504.08703"
url: "https://arxiv.org/abs/2504.08703"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "coding-agents", "repository-context", "rag-evaluation", "evaluation-metrics", "llm-as-judge", "benchmarks", "comparison-and-reproducibility"]
source_path: "raw/papers/2504.08703.md"
sources: ["https://arxiv.org/abs/2504.08703"]
ingested: "2026-11-19"
---

# SWE-PolyBench: A Multi-Language Benchmark for Repository-Level Evaluation of Coding Agents

**Paper:** [2504.08703](https://arxiv.org/abs/2504.08703) · [PDF](https://arxiv.org/pdf/2504.08703) · [HTML](https://arxiv.org/html/2504.08703)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** SWE-PolyBench evaluates executable patches for bug fixes, new features and refactorings across 21 repositories. The authors supplement test outcomes with syntax-tree metrics. [PDF, p. 1](https://arxiv.org/pdf/2504.08703v3#page=1)

**Key result.** In the reported comparison with SWE-bench, a PolyBench task required changes to 63% more files on average. [PDF, p. 4](https://arxiv.org/pdf/2504.08703v3#page=4)

**Limitations and scope.** The released corpus and abstract report 1,017 JavaScript tasks, whereas Table 9 lists 1,078. JavaScript and TypeScript account for most tasks in the results directory. Java accounts for 165. [PDF, p. 1](https://arxiv.org/pdf/2504.08703v3#page=1) [PDF, p. 20](https://arxiv.org/pdf/2504.08703v3#page=20)

[Audit report for 2504.08703v3](../reviews/audit-2026-11-19/2504.08703v3.md)

## Overview

The study compares coding agents on repository-level tasks in several programming languages. [PDF, p. 1](https://arxiv.org/pdf/2504.08703v3#page=1)

## Source files

arXiv version `2504.08703v3` · PDF pages: 20.

- [Original PDF](https://arxiv.org/pdf/2504.08703v3)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2504.08703.metadata.json)

PDF bookmarks — [Limitations (p. 10)](https://arxiv.org/pdf/2504.08703v3#page=10).

Title in the retrieved arXiv record: SWE-PolyBench: A multi-language benchmark for repository level evaluation of coding agents.

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Coding agents](../concepts/coding-agents.md)
- [Repository context](../concepts/repository-context.md)
- [RAG evaluation](../concepts/rag-evaluation.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [LLM-as-a-Judge](../concepts/llm-as-judge.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
