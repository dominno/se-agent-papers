---
type: source
title: "Self-Evolving Coding Agents via Harness-Policy Optimization"
created: 2026-11-19
arxiv_id: "2610.22791"
url: "https://arxiv.org/abs/2610.22791"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "coding-agents", "self-evolution", "prompt-optimization", "workflow-optimization"]
source_path: "raw/papers/2610.22791.md"
sources: ["https://arxiv.org/abs/2610.22791"]
ingested: "2026-11-19"
---

# Self-Evolving Coding Agents via Harness-Policy Optimization

**Paper:** [2610.22791](https://arxiv.org/abs/2610.22791) · [PDF](https://arxiv.org/pdf/2610.22791) · [HTML](https://arxiv.org/html/2610.22791)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** Self-HPO alternates between selecting harness edits proposed by the current model and updating the policy with RL under the selected variant. The next round uses tasks left unsolved during training. [PDF, p. 3](https://arxiv.org/pdf/2610.22791v1#page=3) [PDF, p. 4](https://arxiv.org/pdf/2610.22791v1#page=4)

**Key result.** Qwen3.5-35B-A3B scored 64.8% on average, compared with an initial 57.8%. Results on Verified, Multilingual and Pro V2 were 69.5%, 59.7% and 65.2%, respectively, averaged over three runs. [PDF, p. 4](https://arxiv.org/pdf/2610.22791v1#page=4) [PDF, p. 5](https://arxiv.org/pdf/2610.22791v1#page=5)

**Limitations and scope.** The study tested one base policy and one initial scaffold. The mean weights the three benchmarks equally. On Verified, Table 3 reports 64.5% for the environment change alone, 64.4% for the final policy alone and 69.5% for the two together. [PDF, p. 4](https://arxiv.org/pdf/2610.22791v1#page=4) [PDF, p. 5](https://arxiv.org/pdf/2610.22791v1#page=5) [PDF, p. 6](https://arxiv.org/pdf/2610.22791v1#page=6)

## Overview

The study investigates joint optimization of a coding agent's harness and policy. [PDF, p. 1](https://arxiv.org/pdf/2610.22791v1#page=1)

[Section and evidence audit](../reviews/audit-2026-11-19/2610.22791v1.md)

## Source files

arXiv version `2610.22791v1` · PDF pages: 24.

- [Original PDF](https://arxiv.org/pdf/2610.22791v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2610.22791.metadata.json)

PDF bookmarks — [Conceptual Comparison with Related Methods (p. 18)](https://arxiv.org/pdf/2610.22791v1#page=18) · [Experiments (p. 4)](https://arxiv.org/pdf/2610.22791v1#page=4).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Coding agents](../concepts/coding-agents.md)
- [Agent self-improvement](../concepts/self-evolution.md)
- [Prompt optimization](../concepts/prompt-optimization.md)
- [Workflow optimization](../concepts/workflow-optimization.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
