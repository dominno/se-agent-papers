---
type: source
title: "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses"
created: 2026-11-19
arxiv_id: "2604.25850"
url: "https://arxiv.org/abs/2604.25850"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "coding-agents", "self-evolution", "observability"]
source_path: "raw/papers/2604.25850.md"
sources: ["https://arxiv.org/abs/2604.25850"]
ingested: "2026-11-19"
---

# Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses

**Paper:** [2604.25850](https://arxiv.org/abs/2604.25850) · [PDF](https://arxiv.org/pdf/2604.25850) · [HTML](https://arxiv.org/html/2604.25850)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** Over ten iterations on the same 89 Terminal-Bench 2 tasks, the agent analyzes traces and modifies its execution harness. The best configuration was transferred unchanged to SWE-bench Verified. [PDF, p. 4](https://arxiv.org/pdf/2604.25850v4#page=4) [PDF, p. 5](https://arxiv.org/pdf/2604.25850v4#page=5) [PDF, p. 6](https://arxiv.org/pdf/2604.25850v4#page=6) [PDF, p. 7](https://arxiv.org/pdf/2604.25850v4#page=7)

**Key result.** On Terminal-Bench 2, pass@1 rose from 69.7% to 77.0%. On SWE-bench Verified, the reported aggregate score rose from 75.2% to 75.6%, while mean tokens per trial fell from 526,000 to 461,000. [PDF, p. 6](https://arxiv.org/pdf/2604.25850v4#page=6) [PDF, p. 7](https://arxiv.org/pdf/2604.25850v4#page=7)

**Limitations and scope.** Optimization used the entire Terminal-Bench 2 suite. In Table 2, the counts for the seven named SWE-bench repositories add to 460, while the total row gives 500. This limits verification of the aggregate from the published breakdown. [PDF, p. 6](https://arxiv.org/pdf/2604.25850v4#page=6) [PDF, p. 7](https://arxiv.org/pdf/2604.25850v4#page=7) [PDF, p. 10](https://arxiv.org/pdf/2604.25850v4#page=10) [PDF, p. 17](https://arxiv.org/pdf/2604.25850v4#page=17)

[Audit of sections, tables and appendices](../reviews/audit-2026-11-19/2604.25850v4.md)

## Overview

The method improves the agent harness automatically using execution traces and experimental results. [PDF, p. 1](https://arxiv.org/pdf/2604.25850v4#page=1)

## Source files

arXiv version `2604.25850v4` · PDF pages: 35.

- [Original PDF](https://arxiv.org/pdf/2604.25850v4)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2604.25850.metadata.json)

PDF bookmarks — [Experiments (p. 6)](https://arxiv.org/pdf/2604.25850v4#page=6).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Coding agents](../concepts/coding-agents.md)
- [Agent self-improvement](../concepts/self-evolution.md)
- [Agent observability](../concepts/observability.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
