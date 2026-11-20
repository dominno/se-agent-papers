---
type: source
title: "Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models"
created: 2026-11-19
arxiv_id: "2305.04091"
url: "https://arxiv.org/abs/2305.04091"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "task-planning", "prompt-optimization"]
source_path: "raw/papers/2305.04091.md"
sources: ["https://arxiv.org/abs/2305.04091"]
ingested: "2026-11-19"
---

# Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**Paper:** [2305.04091](https://arxiv.org/abs/2305.04091) · [PDF](https://arxiv.org/pdf/2305.04091) · [HTML](https://arxiv.org/html/2305.04091)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** The model first develops a plan and solves the task. The final result is extracted from its response. PS+ supplies additional instructions specific to each task type. [PDF, p. 3](https://arxiv.org/pdf/2305.04091v3#page=3) [PDF, p. 4](https://arxiv.org/pdf/2305.04091v3#page=4) [PDF, p. 12](https://arxiv.org/pdf/2305.04091v3#page=12) [PDF, p. 13](https://arxiv.org/pdf/2305.04091v3#page=13) [PDF, p. 14](https://arxiv.org/pdf/2305.04091v3#page=14)

**Key result.** In Tables 2–4, PS+ outperforms zero-shot CoT on all ten datasets. On GSM8K it scores 59.3% versus 56.4%, and on Last Letters it scores 75.2% versus 64.8%. Across six arithmetic tasks, the reported means are 76.7% for PS+ and 77.6% for manually selected CoT demonstrations. [PDF, p. 6](https://arxiv.org/pdf/2305.04091v3#page=6)

**Limitations and scope.** Results depend on instruction wording and primarily cover text-davinci-003. Table 2 reports 59.3% on GSM8K, while the voting experiment's description gives 58.7% for the same variant without voting. [PDF, p. 5](https://arxiv.org/pdf/2305.04091v3#page=5) [PDF, p. 6](https://arxiv.org/pdf/2305.04091v3#page=6) [PDF, p. 7](https://arxiv.org/pdf/2305.04091v3#page=7) [PDF, p. 9](https://arxiv.org/pdf/2305.04091v3#page=9)

## Overview

The method separates planning from execution of subtasks to reduce skipped reasoning steps. [PDF, p. 1](https://arxiv.org/pdf/2305.04091v3#page=1)

[Section and evidence audit](../reviews/audit-2026-11-19/2305.04091v3.md)

## Source files

arXiv version `2305.04091v3` · PDF pages: 24.

- [Original PDF](https://arxiv.org/pdf/2305.04091v3)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2305.04091.metadata.json)

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Task planning](../concepts/task-planning.md)
- [Prompt optimization](../concepts/prompt-optimization.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
