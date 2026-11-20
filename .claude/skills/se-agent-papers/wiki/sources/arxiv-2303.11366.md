---
type: source
title: "Reflexion: Language Agents with Verbal Reinforcement Learning"
created: 2026-11-19
arxiv_id: "2303.11366"
url: "https://arxiv.org/abs/2303.11366"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "self-evolution"]
source_path: "raw/papers/2303.11366.md"
sources: ["https://arxiv.org/abs/2303.11366"]
ingested: "2026-11-19"
---

# Reflexion: Language Agents with Verbal Reinforcement Learning

**Paper:** [2303.11366](https://arxiv.org/abs/2303.11366) · [PDF](https://arxiv.org/pdf/2303.11366) · [HTML](https://arxiv.org/html/2303.11366)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** Reflexion stores a written reflection on a trial in episodic memory. The agent consults it in the next trial without changing its weights. [PDF, p. 1](https://arxiv.org/pdf/2303.11366v4#page=1)

**Key result.** On HumanEval Python, the final program submitted by Reflexion achieved 91.0% pass@1 versus 80.1% for a single GPT-4 generation. On MBPP Python, the corresponding scores were 77.1% and 80.1%. Reflexion could use its own tests and make repeated attempts before submitting a program. [PDF, p. 7](https://arxiv.org/pdf/2303.11366v4#page=7) [PDF, p. 8](https://arxiv.org/pdf/2303.11366v4#page=8)

**Limitations and scope.** Automated testing is more difficult for nondeterministic functions and code that depends on hardware, services or concurrency. [PDF, p. 9](https://arxiv.org/pdf/2303.11366v4#page=9)

[Audit report for 2303.11366v4](../reviews/audit-2026-11-19/2303.11366v4.md)

## Overview

The method improves agent behavior through feedback and stored reflections without updating model weights. [PDF, p. 1](https://arxiv.org/pdf/2303.11366v4#page=1)

## Source files

arXiv version `2303.11366v4` · PDF pages: 19.

- [Original PDF](https://arxiv.org/pdf/2303.11366v4)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2303.11366.metadata.json)

PDF bookmarks — [Experiments (p. 5)](https://arxiv.org/pdf/2303.11366v4#page=5) · [Limitations (p. 9)](https://arxiv.org/pdf/2303.11366v4#page=9).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Agent self-improvement](../concepts/self-evolution.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
