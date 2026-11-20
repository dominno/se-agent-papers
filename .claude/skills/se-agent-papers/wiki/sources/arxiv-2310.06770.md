---
type: source
title: "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?"
created: 2026-11-19
arxiv_id: "2310.06770"
url: "https://arxiv.org/abs/2310.06770"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "coding-agents", "repository-context", "evaluation-metrics", "benchmarks", "comparison-and-reproducibility"]
source_path: "raw/papers/2310.06770.md"
sources: ["https://arxiv.org/abs/2310.06770"]
ingested: "2026-11-19"
---

# SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

**Paper:** [2310.06770](https://arxiv.org/abs/2310.06770) · [PDF](https://arxiv.org/pdf/2310.06770) · [HTML](https://arxiv.org/html/2310.06770)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** From real issues and patches in 12 Python projects, the authors selected 2,294 cases with executable tests. Evaluation checks whether the issue is resolved and whether previously passing tests still pass. [PDF, p. 2](https://arxiv.org/pdf/2310.06770v3#page=2) [PDF, p. 3](https://arxiv.org/pdf/2310.06770v3#page=3) [PDF, p. 20](https://arxiv.org/pdf/2310.06770v3#page=20)

**Key result.** In v3, Table 5 lists Claude 3 Opus as the BM25 leader with 3.79% of tasks resolved overall and 4.33% on Lite. Claude 2 scored 1.97% on the full set. The adjacent text still names the earlier leader and reports 1.96%. [PDF, p. 6](https://arxiv.org/pdf/2310.06770v3#page=6)

**Limitations and scope.** The score depends partly on file selection. Given fragments located using the reference patch, Opus scored 9.39%. The sample covers selected public Python repositories and their tests. [PDF, p. 3](https://arxiv.org/pdf/2310.06770v3#page=3) [PDF, p. 7](https://arxiv.org/pdf/2310.06770v3#page=7) [PDF, p. 10](https://arxiv.org/pdf/2310.06770v3#page=10)

[Audit of sections, tables and appendices](../reviews/audit-2026-11-19/2310.06770v3.md)

## Overview

The benchmark evaluates fixes for real GitHub issues against existing repositories and their tests. [PDF, p. 1](https://arxiv.org/pdf/2310.06770v3#page=1)

## Source files

arXiv version `2310.06770v3` · PDF pages: 52.

- [Original PDF](https://arxiv.org/pdf/2310.06770v3)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2310.06770.metadata.json)

PDF bookmarks — [Results (p. 6)](https://arxiv.org/pdf/2310.06770v3#page=6).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Coding agents](../concepts/coding-agents.md)
- [Repository context](../concepts/repository-context.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
