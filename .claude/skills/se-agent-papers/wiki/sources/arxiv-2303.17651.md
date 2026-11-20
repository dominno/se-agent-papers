---
type: source
title: "Self-Refine: Iterative Refinement with Self-Feedback"
created: 2026-11-19
arxiv_id: "2303.17651"
url: "https://arxiv.org/abs/2303.17651"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "prompt-optimization", "workflow-optimization"]
source_path: "raw/papers/2303.17651.md"
sources: ["https://arxiv.org/abs/2303.17651"]
ingested: "2026-11-19"
---

# Self-Refine: Iterative Refinement with Self-Feedback

**Paper:** [2303.17651](https://arxiv.org/abs/2303.17651) · [PDF](https://arxiv.org/pdf/2303.17651) · [HTML](https://arxiv.org/html/2303.17651)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** The same model generates an answer, critiques it and revises its output. At inference time it can repeat these steps using earlier feedback. [PDF, p. 2](https://arxiv.org/pdf/2303.17651v2#page=2) [PDF, p. 3](https://arxiv.org/pdf/2303.17651v2#page=3)

**Key result.** The arithmetic mean of the 21 differences in Table 1 (seven tasks and three models) was 18.7 points across different metrics. Gains on mathematics were 0–0.2 points, while preference for GPT-4 dialogue responses rose by 49.2 points. [PDF, p. 5](https://arxiv.org/pdf/2303.17651v2#page=5) [PDF, p. 28](https://arxiv.org/pdf/2303.17651v2#page=28)

**Limitations and scope.** The method depends on detecting an error. In mathematics, ChatGPT often accepted its own answer without revision. An external signal that an answer is wrong changes the experimental setting. [PDF, p. 6](https://arxiv.org/pdf/2303.17651v2#page=6) [PDF, p. 9](https://arxiv.org/pdf/2303.17651v2#page=9) [PDF, p. 22](https://arxiv.org/pdf/2303.17651v2#page=22)

[Section and table audit for 2303.17651v2](../reviews/audit-2026-11-19/2303.17651v2.md)

## Overview

The method iteratively generates, evaluates and revises responses while keeping model weights fixed. [PDF, p. 1](https://arxiv.org/pdf/2303.17651v2#page=1)

## Source files

arXiv version `2303.17651v2` · PDF pages: 54.

- [Original PDF](https://arxiv.org/pdf/2303.17651v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2303.17651.metadata.json)

PDF bookmarks — [Evaluation (p. 4)](https://arxiv.org/pdf/2303.17651v2#page=4) · [Limitations and Discussion (p. 9)](https://arxiv.org/pdf/2303.17651v2#page=9).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Prompt optimization](../concepts/prompt-optimization.md)
- [Workflow optimization](../concepts/workflow-optimization.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
