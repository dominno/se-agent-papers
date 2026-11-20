---
type: source
title: "Decentralized Multi-Agent Coordination and Communication in Shared Codebases"
created: 2026-11-19
arxiv_id: "2611.00314"
url: "https://arxiv.org/abs/2611.00314"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "task-planning", "parallelism", "coding-agents", "repository-context", "agent-communication"]
source_path: "raw/papers/2611.00314.md"
sources: ["https://arxiv.org/abs/2611.00314"]
ingested: "2026-11-19"
---

# Decentralized Multi-Agent Coordination and Communication in Shared Codebases

**Paper:** [2611.00314](https://arxiv.org/abs/2611.00314) · [PDF](https://arxiv.org/pdf/2611.00314) · [HTML](https://arxiv.org/html/2611.00314)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** ParallACT compares a single agent that sees both specifications with pairs of agents under different conditions of visibility, ordering and communication. The 155 pairs include 85 conflicting and 70 complementary pairs. [PDF, p. 4](https://arxiv.org/pdf/2611.00314v1#page=4) [PDF, p. 5](https://arxiv.org/pdf/2611.00314v1#page=5) [PDF, p. 15](https://arxiv.org/pdf/2611.00314v1#page=15)

**Key result.** Across 50 conflicting tasks in the Opus 4.8 subset, the oracle passed 31/50 (62%) and parallel agents unaware of one another passed 8/50 (16%). Messaging raised the rate to 20%, while sequential A→B execution reached 54%. [PDF, p. 8](https://arxiv.org/pdf/2611.00314v1#page=8) [PDF, p. 22](https://arxiv.org/pdf/2611.00314v1#page=22) [PDF, p. 27](https://arxiv.org/pdf/2611.00314v1#page=27)

**Limitations and scope.** The authors deliberately paired two agents with interdependent tasks. The results do not estimate the frequency of such conflicts in ordinary work. [PDF, p. 12](https://arxiv.org/pdf/2611.00314v1#page=12) [PDF, p. 15](https://arxiv.org/pdf/2611.00314v1#page=15)

[Section and table audit for 2611.00314v1](../reviews/audit-2026-11-19/2611.00314v1.md)

## Overview

The study examines conflicting requirements and coordination between agents working concurrently in one repository. [PDF, p. 1](https://arxiv.org/pdf/2611.00314v1#page=1)

## Source files

arXiv version `2611.00314v1` · PDF pages: 38.

- [Original PDF](https://arxiv.org/pdf/2611.00314v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2611.00314.metadata.json)

PDF bookmarks — [Results & Analysis (p. 7)](https://arxiv.org/pdf/2611.00314v1#page=7).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Task planning](../concepts/task-planning.md)
- [Parallelism](../concepts/parallelism.md)
- [Coding agents](../concepts/coding-agents.md)
- [Repository context](../concepts/repository-context.md)
- [Agent communication](../concepts/agent-communication.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
