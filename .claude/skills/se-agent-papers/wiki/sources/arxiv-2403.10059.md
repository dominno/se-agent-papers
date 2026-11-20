---
type: source
title: "Repoformer: Selective Retrieval for Repository-Level Code Completion"
created: 2026-11-19
arxiv_id: "2403.10059"
url: "https://arxiv.org/abs/2403.10059"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["coding-agents", "repository-context", "retrieval-augmented-generation", "selective-retrieval", "rag-evaluation", "llm-as-judge", "benchmarks", "unit-testing", "evaluation-metrics"]
source_path: "raw/papers/2403.10059.md"
sources: ["https://arxiv.org/abs/2403.10059"]
ingested: "2026-11-19"
---

# Repoformer: Selective Retrieval for Repository-Level Code Completion

**Paper:** [2403.10059](https://arxiv.org/abs/2403.10059) · [PDF](https://arxiv.org/pdf/2403.10059) · [HTML](https://arxiv.org/html/2403.10059)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** Self-supervised labels are derived by comparing completions with and without a retrieved passage. A special token decides whether to retrieve repository context. [PDF, p. 3](https://arxiv.org/pdf/2403.10059v2#page=3) [PDF, p. 4](https://arxiv.org/pdf/2403.10059v2#page=4) [PDF, p. 17](https://arxiv.org/pdf/2403.10059v2#page=17)

**Key result.** With dense retrieval in Table 8, the greedy 1B variant was 71% faster than always retrieving but produced lower code similarity. The threshold variant was 33% faster and improved similarity on both tasks. [PDF, p. 20](https://arxiv.org/pdf/2403.10059v2#page=20)

**Limitations and scope.** Timing results depend on parallel scheduling, retrieval overhead and the decision threshold. Decisions at whole-function level are less well calibrated, especially for the test pass metric. [PDF, p. 7](https://arxiv.org/pdf/2403.10059v2#page=7) [PDF, p. 19](https://arxiv.org/pdf/2403.10059v2#page=19) [PDF, p. 21](https://arxiv.org/pdf/2403.10059v2#page=21)

[Section and table audit for 2403.10059v2](../reviews/audit-2026-11-19/2403.10059v2.md)

## Overview

The method retrieves context selectively when it is expected to help code generation, reducing noise and unnecessary cost. [PDF, p. 1](https://arxiv.org/pdf/2403.10059v2#page=1)

## Section notes

**Mechanism:** Before completing code, the model decides whether to retrieve repository context. Both selection and generation use self-supervised learning. [PDF, p. 3](https://arxiv.org/pdf/2403.10059v2#page=3) · [PDF, p. 4](https://arxiv.org/pdf/2403.10059v2#page=4)

**Evaluation and study settings:** The authors compared repository-level code completion on benchmarks including RepoEval and CrossCodeEval. They also examined retrieval costs and speed. [PDF, p. 5](https://arxiv.org/pdf/2403.10059v2#page=5) · [PDF, p. 7](https://arxiv.org/pdf/2403.10059v2#page=7)

**Scope and interpretation:** The results on the evaluated coding benchmarks do not establish that selective retrieval benefits every agent workflow. [PDF, p. 5](https://arxiv.org/pdf/2403.10059v2#page=5)

**Sections checked:** 3 Approach, 4 Experimental Setup, 5 Results, 6 Analysis. [Read the paper](https://arxiv.org/html/2403.10059).


## Source files

arXiv version `2403.10059v2` · PDF pages: 21.

- [Original PDF](https://arxiv.org/pdf/2403.10059v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2403.10059.metadata.json)

## Related concepts

- [Coding agents](../concepts/coding-agents.md)
- [Repository context](../concepts/repository-context.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md)
- [Selective retrieval](../concepts/selective-retrieval.md)
- [RAG evaluation](../concepts/rag-evaluation.md)
- [LLM-as-a-Judge](../concepts/llm-as-judge.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Unit tests](../concepts/unit-testing.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.

## Findings and caveats

- [Finding 1 — method](../concepts/finding-2403-10059-1.md)
- [Finding 2 — evaluation](../concepts/finding-2403-10059-2.md)
- [Finding 3 — interpretive caveat](../concepts/finding-2403-10059-3.md)
