---
type: source
title: "RepoZero: Can LLMs Generate a Code Repository from Scratch?"
created: 2026-11-19
arxiv_id: "2605.07122"
url: "https://arxiv.org/abs/2605.07122"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "coding-agents", "repository-context", "evaluation-metrics", "benchmarks", "comparison-and-reproducibility"]
source_path: "raw/papers/2605.07122.md"
sources: ["https://arxiv.org/abs/2605.07122"]
ingested: "2026-11-19"
---

# RepoZero: Can LLMs Generate a Code Repository from Scratch?

**Paper:** [2605.07122](https://arxiv.org/abs/2605.07122) · [PDF](https://arxiv.org/pdf/2605.07122) · [HTML](https://arxiv.org/html/2605.07122)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** RepoZero contains 400 Python→JavaScript test files and 200 C/C++→Rust test files. The agent reproduces the required API behavior. Evaluation compares outputs with a reference implementation, and ACE adds its own tests and iterative code revisions. [PDF, p. 3](https://arxiv.org/pdf/2605.07122v3#page=3) [PDF, p. 4](https://arxiv.org/pdf/2605.07122v3#page=4) [PDF, p. 5](https://arxiv.org/pdf/2605.07122v3#page=5) [PDF, p. 6](https://arxiv.org/pdf/2605.07122v3#page=6)

**Key result.** With Mini-SWE-Agent, Claude-4.6-Sonnet passed an average of 54.70% of Py2JS samples and 47.58% of C2Rust samples. For DeepSeek V3.1 on Py2JS, two ACE iterations raised pass rates from 26.08% to 42.88% in OpenHands-bash and from 43.76% to 52.06% in Mini-SWE-Agent. [PDF, p. 7](https://arxiv.org/pdf/2605.07122v3#page=7) [PDF, p. 8](https://arxiv.org/pdf/2605.07122v3#page=8)

**Limitations and scope.** Matching test outputs does not measure architectural clarity. For DeepSeek V3.1/OpenHands-bash, no weighted mean of the category scores in Supplementary Table 5 with nonnegative weights summing to 1 yields the overall PR in Table 2. [PDF, p. 7](https://arxiv.org/pdf/2605.07122v3#page=7) [PDF, p. 10](https://arxiv.org/pdf/2605.07122v3#page=10) [PDF, p. 13](https://arxiv.org/pdf/2605.07122v3#page=13)

## Overview

The study evaluates building a complete repository from scratch using a specification and executable tests. [PDF, p. 1](https://arxiv.org/pdf/2605.07122v3#page=1)

[Section and evidence audit](../reviews/audit-2026-11-19/2605.07122v3.md)

## Source files

arXiv version `2605.07122v3` · PDF pages: 16.

- [Original PDF](https://arxiv.org/pdf/2605.07122v3)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2605.07122.metadata.json)

PDF bookmarks — [Results and Analysis (p. 6)](https://arxiv.org/pdf/2605.07122v3#page=6).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Coding agents](../concepts/coding-agents.md)
- [Repository context](../concepts/repository-context.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
