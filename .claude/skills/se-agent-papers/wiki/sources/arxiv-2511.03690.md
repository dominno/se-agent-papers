---
type: source
title: "The OpenHands Software Agent SDK: A Composable and Extensible Foundation for Production Agents"
created: 2026-11-19
arxiv_id: "2511.03690"
url: "https://arxiv.org/abs/2511.03690"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "coding-agents", "architecture-design", "debugging"]
source_path: "raw/papers/2511.03690.md"
sources: ["https://arxiv.org/abs/2511.03690"]
ingested: "2026-11-19"
---

# The OpenHands Software Agent SDK: A Composable and Extensible Foundation for Production Agents

**Paper:** [2511.03690](https://arxiv.org/abs/2511.03690) · [PDF](https://arxiv.org/pdf/2511.03690) · [HTML](https://arxiv.org/html/2511.03690)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** OpenHands V1 separates session state from configuration and stores immutable events. The authors separately analyze logs from a parallel V0/V1 deployment, replay of traces from 433 conversations, and performance on benchmark tasks. [PDF, p. 6](https://arxiv.org/pdf/2511.03690v2#page=6) [PDF, p. 7](https://arxiv.org/pdf/2511.03690v2#page=7) [PDF, p. 12](https://arxiv.org/pdf/2511.03690v2#page=12) [PDF, p. 13](https://arxiv.org/pdf/2511.03690v2#page=13) [PDF, p. 14](https://arxiv.org/pdf/2511.03690v2#page=14)

**Key result.** During a 15-day deployment, failures attributed to the system fell from 78 to 30 per thousand conversations, a decrease of 48 per thousand (61.5% relative to V0). Model-provider failures were excluded. [PDF, p. 12](https://arxiv.org/pdf/2511.03690v2#page=12) [PDF, p. 19](https://arxiv.org/pdf/2511.03690v2#page=19)

**Limitations and scope.** Failure measurements cover the deployment and replayed traces. For the longest conversation (358 events), Table 3 gives 32.1 ms for crash recovery and 18.9 ms for replay alone. The text claims recovery in under 20 ms. [PDF, p. 12](https://arxiv.org/pdf/2511.03690v2#page=12) [PDF, p. 13](https://arxiv.org/pdf/2511.03690v2#page=13) [PDF, p. 16](https://arxiv.org/pdf/2511.03690v2#page=16)

## Overview

The paper describes a modular toolkit for building coding agents, including adapters, a runtime and lifecycle management. [PDF, p. 1](https://arxiv.org/pdf/2511.03690v2#page=1)

[Section and evidence audit](../reviews/audit-2026-11-19/2511.03690v2.md)

## Source files

arXiv version `2511.03690v2` · PDF pages: 19.

- [Original PDF](https://arxiv.org/pdf/2511.03690v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2511.03690.metadata.json)

PDF bookmarks — [Reliability and Evaluation (p. 11)](https://arxiv.org/pdf/2511.03690v2#page=11).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Coding agents](../concepts/coding-agents.md)
- [Software architecture](../concepts/architecture-design.md)
- [Debugging](../concepts/debugging.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
