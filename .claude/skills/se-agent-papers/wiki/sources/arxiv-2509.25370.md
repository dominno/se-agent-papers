---
type: source
title: "Where LLM Agents Fail and How They can Learn From Failures"
created: 2026-11-19
arxiv_id: "2509.25370"
url: "https://arxiv.org/abs/2509.25370"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "coding-agents", "debugging", "fault-recovery"]
source_path: "raw/papers/2509.25370.md"
sources: ["https://arxiv.org/abs/2509.25370"]
ingested: "2026-11-19"
---

# Where LLM Agents Fail and How They can Learn From Failures

**Paper:** [2509.25370](https://arxiv.org/abs/2509.25370) · [PDF](https://arxiv.org/pdf/2509.25370) · [HTML](https://arxiv.org/html/2509.25370)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** The authors evaluate localization of the root-cause step, module and error type on 200 annotated failed runs from ALFWorld, WebShop and GAIA. The agent can then resume execution at the identified step. [PDF, p. 4](https://arxiv.org/pdf/2509.25370v1#page=4) [PDF, p. 6](https://arxiv.org/pdf/2509.25370v1#page=6) [PDF, p. 7](https://arxiv.org/pdf/2509.25370v1#page=7)

**Key result.** Averaging the environments equally, all diagnostic elements were correct in 24.3% of cases, compared with 0.3% for the baseline. Step localization alone achieved 45.0%, compared with 28.0%. [PDF, p. 7](https://arxiv.org/pdf/2509.25370v1#page=7)

**Limitations and scope.** The dataset contains selected failed runs from three domains. Human annotators agreed on the module label with Cohen's κ = 0.55. [PDF, p. 4](https://arxiv.org/pdf/2509.25370v1#page=4) [PDF, p. 12](https://arxiv.org/pdf/2509.25370v1#page=12)

[Audit of sections, tables and appendices](../reviews/audit-2026-11-19/2509.25370v1.md)

## Overview

The paper classifies language-agent failures and examines how agents can improve by learning from earlier errors. [PDF, p. 1](https://arxiv.org/pdf/2509.25370v1#page=1)

## Source files

arXiv version `2509.25370v1` · PDF pages: 32.

- [Original PDF](https://arxiv.org/pdf/2509.25370v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2509.25370.metadata.json)

PDF bookmarks — [Experiments and Results (p. 6)](https://arxiv.org/pdf/2509.25370v1#page=6).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Coding agents](../concepts/coding-agents.md)
- [Debugging](../concepts/debugging.md)
- [Crash recovery](../concepts/fault-recovery.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
