---
type: source
title: "Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents"
created: 2026-11-19
arxiv_id: "2505.22954"
url: "https://arxiv.org/abs/2505.22954"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "self-evolution", "benchmarks"]
source_path: "raw/papers/2505.22954.md"
sources: ["https://arxiv.org/abs/2505.22954"]
ingested: "2026-11-19"
---

# Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents

**Paper:** [2505.22954](https://arxiv.org/abs/2505.22954) · [PDF](https://arxiv.org/pdf/2505.22954) · [HTML](https://arxiv.org/html/2505.22954)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** DGM selects a parent agent's code from an archive, creates a variant and evaluates it on tasks in stages. The archive maintenance and parent selection mechanisms remain fixed. [PDF, p. 4](https://arxiv.org/pdf/2505.22954v3#page=4) [PDF, p. 5](https://arxiv.org/pdf/2505.22954v3#page=5) [PDF, p. 6](https://arxiv.org/pdf/2505.22954v3#page=6)

**Key result.** After 80 iterations, scores rose from 20.0% to 50.0% on 200 SWE-bench tasks and from 14.0% to 38.0% on 50 Polyglot tasks. On the full Polyglot set they rose from 14.2% to 30.7%. [PDF, p. 6](https://arxiv.org/pdf/2505.22954v3#page=6) [PDF, p. 7](https://arxiv.org/pdf/2505.22954v3#page=7) [PDF, p. 36](https://arxiv.org/pdf/2505.22954v3#page=36)

**Limitations and scope.** Agent selection is empirical and benchmark-dependent. The estimated cost of one DGM run on SWE-bench is approximately $22,000, compared with approximately $10,000 for one baseline method. [PDF, p. 6](https://arxiv.org/pdf/2505.22954v3#page=6) [PDF, p. 9](https://arxiv.org/pdf/2505.22954v3#page=9) [PDF, p. 32](https://arxiv.org/pdf/2505.22954v3#page=32)

[Section and table audit for 2505.22954v3](../reviews/audit-2026-11-19/2505.22954v3.md)

## Overview

The agent edits its own code, tests variants and retains successful changes in an evolutionary archive. [PDF, p. 1](https://arxiv.org/pdf/2505.22954v3#page=1)

## Source files

arXiv version `2505.22954v3` · PDF pages: 72.

- [Original PDF](https://arxiv.org/pdf/2505.22954v3)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2505.22954.metadata.json)

PDF bookmarks — [Experiments (p. 5)](https://arxiv.org/pdf/2505.22954v3#page=5) · [Conclusion and Limitations (p. 9)](https://arxiv.org/pdf/2505.22954v3#page=9).

Title in the retrieved arXiv record: Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents.

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Agent self-improvement](../concepts/self-evolution.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
