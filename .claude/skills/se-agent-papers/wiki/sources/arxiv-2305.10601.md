---
type: source
title: "Tree of Thoughts: Deliberate Problem Solving with Large Language Models"
created: 2026-11-19
arxiv_id: "2305.10601"
url: "https://arxiv.org/abs/2305.10601"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "task-planning"]
source_path: "raw/papers/2305.10601.md"
sources: ["https://arxiv.org/abs/2305.10601"]
ingested: "2026-11-19"
---

# Tree of Thoughts: Deliberate Problem Solving with Large Language Models

**Paper:** [2305.10601](https://arxiv.org/abs/2305.10601) · [PDF](https://arxiv.org/pdf/2305.10601) · [HTML](https://arxiv.org/html/2305.10601)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** Tree of Thoughts explores multiple candidate reasoning steps, evaluates partial paths and can prune them or backtrack. [PDF, p. 1](https://arxiv.org/pdf/2305.10601v2#page=1)

**Key result.** On 100 Game of 24 problems, GPT-4 with ToT (breadth 5) solved 74 according to Table 2. CoT averaged 4.0% success on a single attempt and solved 49 tasks with best-of-100 selection. The released log from a later ToT run shows 69/100. [PDF, p. 5](https://arxiv.org/pdf/2305.10601v2#page=5) [PDF, p. 6](https://arxiv.org/pdf/2305.10601v2#page=6) [PDF, p. 13](https://arxiv.org/pdf/2305.10601v2#page=13) [Authors' logs](https://github.com/princeton-nlp/tree-of-thought-llm/tree/8050e67d0e3a0fddc424d7fa5801538722a4c4cc/logs/game24)

**Limitations and scope.** The experiment covers three tasks requiring planning or search. The arithmetic game result does not estimate overall model quality. [PDF, p. 1](https://arxiv.org/pdf/2305.10601v2#page=1)

[Audit report for 2305.10601v2](../reviews/audit-2026-11-19/2305.10601v2.md)

## Overview

The method explores alternative reasoning steps and evaluates partial solutions before choosing how to proceed. [PDF, p. 1](https://arxiv.org/pdf/2305.10601v2#page=1)

## Source files

arXiv version `2305.10601v2` · PDF pages: 14.

- [Original PDF](https://arxiv.org/pdf/2305.10601v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2305.10601.metadata.json)

PDF bookmarks — [Experiments (p. 4)](https://arxiv.org/pdf/2305.10601v2#page=4).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Task planning](../concepts/task-planning.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
