---
type: source
title: "Agentless: Demystifying LLM-based Software Engineering Agents"
created: 2026-11-19
arxiv_id: "2407.01489"
url: "https://arxiv.org/abs/2407.01489"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "coding-agents", "debugging", "observability"]
source_path: "raw/papers/2407.01489.md"
sources: ["https://arxiv.org/abs/2407.01489"]
ingested: "2026-11-19"
---

# Agentless: Demystifying LLM-based Software Engineering Agents

**Paper:** [2407.01489](https://arxiv.org/abs/2407.01489) · [PDF](https://arxiv.org/pdf/2407.01489) · [HTML](https://arxiv.org/html/2407.01489)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** Agentless localizes edits hierarchically, generates patches and filters them with regression and reproduction tests before voting. [PDF, p. 5](https://arxiv.org/pdf/2407.01489v2#page=5) [PDF, p. 7](https://arxiv.org/pdf/2407.01489v2#page=7) [PDF, p. 8](https://arxiv.org/pdf/2407.01489v2#page=8) [PDF, p. 9](https://arxiv.org/pdf/2407.01489v2#page=9)

**Key result.** GPT-4o solved 96/300 SWE-bench Lite issues (32%) at an average cost of $0.70. It solved 84/249 on Lite-S (33.73%) and 194/500 on Verified (38.80%). [PDF, p. 10](https://arxiv.org/pdf/2407.01489v2#page=10) [PDF, p. 17](https://arxiv.org/pdf/2407.01489v2#page=17) [PDF, p. 18](https://arxiv.org/pdf/2407.01489v2#page=18)

**Limitations and scope.** Lite-S excludes problematic issues, changing the evaluated population and the ranking of some methods. Of the tests Agentless generated, 94 correctly identified the issue as resolved after the reference patch was applied. [PDF, p. 12](https://arxiv.org/pdf/2407.01489v2#page=12) [PDF, p. 15](https://arxiv.org/pdf/2407.01489v2#page=15) [PDF, p. 16](https://arxiv.org/pdf/2407.01489v2#page=16) [PDF, p. 17](https://arxiv.org/pdf/2407.01489v2#page=17)

[Section and table audit for 2407.01489v2](../reviews/audit-2026-11-19/2407.01489v2.md)

## Overview

The method localizes the fault, generates a patch and validates it through a simple sequence of steps. [PDF, p. 1](https://arxiv.org/pdf/2407.01489v2#page=1)

## Source files

arXiv version `2407.01489v2` · PDF pages: 25.

- [Original PDF](https://arxiv.org/pdf/2407.01489v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2407.01489.metadata.json)

PDF bookmarks — [Evaluation (p. 10)](https://arxiv.org/pdf/2407.01489v2#page=10) · [Threats to Validity (p. 18)](https://arxiv.org/pdf/2407.01489v2#page=18).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Coding agents](../concepts/coding-agents.md)
- [Debugging](../concepts/debugging.md)
- [Agent observability](../concepts/observability.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
