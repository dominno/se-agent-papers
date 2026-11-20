---
type: source
title: "Evo-Harness: Context-to-Harness Skill Compilation for Self-Evolving Agents"
created: 2026-11-19
arxiv_id: "2608.15071"
url: "https://arxiv.org/abs/2608.15071"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "self-evolution", "agent-skills", "context-window"]
source_path: "raw/papers/2608.15071.md"
sources: ["https://arxiv.org/abs/2608.15071"]
ingested: "2026-11-19"
---

# Evo-Harness: Context-to-Harness Skill Compilation for Self-Evolving Agents

**Paper:** [2608.15071](https://arxiv.org/abs/2608.15071) · [PDF](https://arxiv.org/pdf/2608.15071) · [HTML](https://arxiv.org/html/2608.15071)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** With the solver’s weights fixed, a separate stage selects and edits guidance from earlier task runs. Updates are batched. Before the next task, a selector chooses general and topic-specific entries. [PDF, p. 3](https://arxiv.org/pdf/2608.15071v2#page=3) [PDF, p. 4](https://arxiv.org/pdf/2608.15071v2#page=4) [PDF, p. 5](https://arxiv.org/pdf/2608.15071v2#page=5) [PDF, p. 14](https://arxiv.org/pdf/2608.15071v2#page=14)

**Key result.** With Opus 4.6, Evo-Harness outperformed No Evolve and XSkill on five benchmarks. On 89 TerminalBench-2 tasks it scored 73.03%, compared with 62.92% and 66.29%. The appendices describe the results as means over three runs. [PDF, p. 6](https://arxiv.org/pdf/2608.15071v2#page=6) [PDF, p. 12](https://arxiv.org/pdf/2608.15071v2#page=12) [PDF, p. 15](https://arxiv.org/pdf/2608.15071v2#page=15)

**Limitations and scope.** Gains depend on the model and feedback. On SWE-bench Lite, self-evaluation with Opus 4.6 yielded 61.67%, compared with 63.67% without changes. The study did not evaluate multi-agent coordination or physical environments. [PDF, p. 8](https://arxiv.org/pdf/2608.15071v2#page=8) [PDF, p. 9](https://arxiv.org/pdf/2608.15071v2#page=9)

## Overview

The paper describes converting experience from completed tasks into reusable skills and agent configurations. [PDF, p. 1](https://arxiv.org/pdf/2608.15071v2#page=1)

[Section and evidence audit](../reviews/audit-2026-11-19/2608.15071v2.md)

## Source files

arXiv version `2608.15071v2` · PDF pages: 16.

- [Original PDF](https://arxiv.org/pdf/2608.15071v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2608.15071.metadata.json)

PDF bookmarks — [Experiments (p. 5)](https://arxiv.org/pdf/2608.15071v2#page=5).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Agent self-improvement](../concepts/self-evolution.md)
- [Agent skills](../concepts/agent-skills.md)
- [Context window](../concepts/context-window.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
