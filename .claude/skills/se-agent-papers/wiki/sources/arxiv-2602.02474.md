---
type: source
title: "MemSkill: Learning and Evolving Memory Skills for Self-Evolving Agents"
created: 2026-11-19
arxiv_id: "2602.02474"
url: "https://arxiv.org/abs/2602.02474"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "self-evolution", "agent-skills", "long-term-memory", "memory-evaluation", "stateful-tool-use", "tool-evaluation"]
source_path: "raw/papers/2602.02474.md"
sources: ["https://arxiv.org/abs/2602.02474"]
ingested: "2026-11-19"
---

# MemSkill: Learning and Evolving Memory Skills for Self-Evolving Agents

**Paper:** [2602.02474](https://arxiv.org/abs/2602.02474) · [PDF](https://arxiv.org/pdf/2602.02474) · [HTML](https://arxiv.org/html/2602.02474)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** A controller selects operations from a memory bank and learns from reward. A separate designer examines recurring failures and proposes new operations and changes to their descriptions. [PDF, p. 4](https://arxiv.org/pdf/2602.02474v3#page=4) [PDF, p. 5](https://arxiv.org/pdf/2602.02474v3#page=5) [PDF, p. 6](https://arxiv.org/pdf/2602.02474v3#page=6)

**Key result.** For LLaMA-3.3-70B on ALFWorld with demonstrations, mean execution accuracy was 80.36%, compared with 77.82% for Mem0 and 74.83% for LightMem. MemSkill scored 44.21 F1 on LoCoMo. [PDF, p. 7](https://arxiv.org/pdf/2602.02474v3#page=7) [PDF, p. 13](https://arxiv.org/pdf/2602.02474v3#page=13)

**Limitations and scope.** The results depend on the model and transfer protocol. Another method achieved higher F1 in some configurations. The authors used a fixed seed and reported no uncertainty intervals. [PDF, p. 7](https://arxiv.org/pdf/2602.02474v3#page=7) [PDF, p. 39](https://arxiv.org/pdf/2602.02474v3#page=39)

[Audit report for 2602.02474v3](../reviews/audit-2026-11-19/2602.02474v3.md)

## Overview

The study investigates how agents learn policies for storing, updating and retrieving memories. [PDF, p. 1](https://arxiv.org/pdf/2602.02474v3#page=1)

## Source files

arXiv version `2602.02474v3` · PDF pages: 43.

- [Original PDF](https://arxiv.org/pdf/2602.02474v3)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2602.02474.metadata.json)

PDF bookmarks — [Experiments (p. 6)](https://arxiv.org/pdf/2602.02474v3#page=6) · [Limitations and Societal Impact (p. 35)](https://arxiv.org/pdf/2602.02474v3#page=35).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Agent self-improvement](../concepts/self-evolution.md)
- [Agent skills](../concepts/agent-skills.md)
- [Long-term memory](../concepts/long-term-memory.md)
- [Memory evaluation](../concepts/memory-evaluation.md)
- [Stateful tool use](../concepts/stateful-tool-use.md)
- [Tool evaluation](../concepts/tool-evaluation.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
