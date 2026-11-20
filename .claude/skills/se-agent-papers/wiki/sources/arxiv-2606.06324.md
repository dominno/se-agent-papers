---
type: source
title: "From Failed Trajectories to Reliable LLM Agents: Diagnosing and Repairing Harness Flaws"
created: 2026-11-19
arxiv_id: "2606.06324"
url: "https://arxiv.org/abs/2606.06324"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "debugging", "self-evolution", "fault-recovery"]
source_path: "raw/papers/2606.06324.md"
sources: ["https://arxiv.org/abs/2606.06324"]
ingested: "2026-11-19"
---

# From Failed Trajectories to Reliable LLM Agents: Diagnosing and Repairing Harness Flaws

**Paper:** [2606.06324](https://arxiv.org/abs/2606.06324) · [PDF](https://arxiv.org/pdf/2606.06324) · [HTML](https://arxiv.org/html/2606.06324)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** HarnessFix links trajectory steps to data flow, control decisions and specific implementation elements. Recurring diagnoses narrow the scope of repairs. Changes undergo regression checks on a held-out validation set. [PDF, p. 4](https://arxiv.org/pdf/2606.06324v2#page=4) [PDF, p. 6](https://arxiv.org/pdf/2606.06324v2#page=6) [PDF, p. 7](https://arxiv.org/pdf/2606.06324v2#page=7)

**Key result.** In Table VI, the full method increased task completion over the variant without regression checks by 6.1 percentage points on GAIA, 4.0 on SWE-bench Verified, 3.7 on AppWorld and 2.0 on Terminal-Bench. These are means over three runs with GPT-5 mini. [PDF, p. 8](https://arxiv.org/pdf/2606.06324v2#page=8) [PDF, p. 9](https://arxiv.org/pdf/2606.06324v2#page=9)

**Limitations and scope.** Patch acceptance depends on the validation tasks. Transfer without another repair was demonstrated on GAIA. Token costs cover offline adaptation. Table III also reports a gain of 5.9 percentage points for DeepSeek on AppWorld, below the lower bound given in the abstract. [PDF, p. 1](https://arxiv.org/pdf/2606.06324v2#page=1) [PDF, p. 7](https://arxiv.org/pdf/2606.06324v2#page=7) [PDF, p. 9](https://arxiv.org/pdf/2606.06324v2#page=9) [PDF, p. 10](https://arxiv.org/pdf/2606.06324v2#page=10)

[Section and table audit for 2606.06324v2](../reviews/audit-2026-11-19/2606.06324v2.md)

## Overview

The method analyzes failed trajectories, attributes failures to components of the agent harness and proposes targeted fixes. [PDF, p. 1](https://arxiv.org/pdf/2606.06324v2#page=1)

## Source files

arXiv version `2606.06324v2` · PDF pages: 13.

- [Original PDF](https://arxiv.org/pdf/2606.06324v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2606.06324.metadata.json)

PDF bookmarks — [Approach (p. 3)](https://arxiv.org/pdf/2606.06324v2#page=3) · [Results and Analysis (p. 8)](https://arxiv.org/pdf/2606.06324v2#page=8).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Debugging](../concepts/debugging.md)
- [Agent self-improvement](../concepts/self-evolution.md)
- [Crash recovery](../concepts/fault-recovery.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
