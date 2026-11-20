---
type: source
title: "Don't Blame the Large Language Model: How Agent Harness Evolution Shapes Coding Agent Quality"
created: 2026-11-19
arxiv_id: "2607.03691"
url: "https://arxiv.org/abs/2607.03691"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "coding-agents", "self-evolution"]
source_path: "raw/papers/2607.03691.md"
sources: ["https://arxiv.org/abs/2607.03691"]
ingested: "2026-11-19"
---

# Don't Blame the Large Language Model: How Agent Harness Evolution Shapes Coding Agent Quality

**Paper:** [2607.03691](https://arxiv.org/abs/2607.03691) · [PDF](https://arxiv.org/pdf/2607.03691) · [HTML](https://arxiv.org/html/2607.03691)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** Using the same Qwen3-Next-80B-A3B-Instruct model, the authors ran two trials for each of 35 Qwen Code versions on 50 SWE-bench Verified tasks, for 3,500 trials. [PDF, p. 10](https://arxiv.org/pdf/2607.03691v2#page=10) [PDF, p. 17](https://arxiv.org/pdf/2607.03691v2#page=17) [PDF, p. 18](https://arxiv.org/pdf/2607.03691v2#page=18)

**Key result.** Across versions, repair rates ranged from 23.0% to 39.0%, averaging 30.5%. Correlation with release order did not reach significance (ρ=0.208, p=0.231), while token usage increased (ρ=0.751, p<0.0001). [PDF, p. 18](https://arxiv.org/pdf/2607.03691v2#page=18) [PDF, p. 19](https://arxiv.org/pdf/2607.03691v2#page=19) [PDF, p. 20](https://arxiv.org/pdf/2607.03691v2#page=20)

**Limitations and scope.** Two runs agreed on the repair outcome in 87.7% of cases. The sample excluded very difficult tasks. Relationships between components and outcomes are observational. [PDF, p. 10](https://arxiv.org/pdf/2607.03691v2#page=10) [PDF, p. 31](https://arxiv.org/pdf/2607.03691v2#page=31) [PDF, p. 32](https://arxiv.org/pdf/2607.03691v2#page=32) [PDF, p. 34](https://arxiv.org/pdf/2607.03691v2#page=34)

[Section and table audit for 2607.03691v2](../reviews/audit-2026-11-19/2607.03691v2.md)

## Overview

The study shows how changing the tools or runtime environment can alter performance while keeping the model fixed. [PDF, p. 1](https://arxiv.org/pdf/2607.03691v2#page=1)

## Source files

**Paper license notice.** The arXiv record lists CC BY 4.0. The first page also carries an ACM notice on personal and classroom copying and other uses. [PDF, p. 1](https://arxiv.org/pdf/2607.03691v2#page=1)

arXiv version `2607.03691v2` · PDF pages: 46.

- [Original PDF](https://arxiv.org/pdf/2607.03691v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2607.03691.metadata.json)

PDF bookmarks — [3 Methodology (p. 7)](https://arxiv.org/pdf/2607.03691v2#page=7) · [9 Threats to Validity (p. 34)](https://arxiv.org/pdf/2607.03691v2#page=34).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Coding agents](../concepts/coding-agents.md)
- [Agent self-improvement](../concepts/self-evolution.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
