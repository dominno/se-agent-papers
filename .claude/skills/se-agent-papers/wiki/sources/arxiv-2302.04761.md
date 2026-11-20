---
type: source
title: "Toolformer: Language Models Can Teach Themselves to Use Tools"
created: 2026-11-19
arxiv_id: "2302.04761"
url: "https://arxiv.org/abs/2302.04761"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "task-planning", "stateful-tool-use", "tool-evaluation", "tool-sandboxing"]
source_path: "raw/papers/2302.04761.md"
sources: ["https://arxiv.org/abs/2302.04761"]
ingested: "2026-11-19"
---

# Toolformer: Language Models Can Teach Themselves to Use Tools

**Paper:** [2302.04761](https://arxiv.org/abs/2302.04761) · [PDF](https://arxiv.org/pdf/2302.04761) · [HTML](https://arxiv.org/html/2302.04761)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** Toolformer proposes calls to five text-based APIs and retains calls whose results sufficiently reduce loss on subsequent tokens. It fine-tunes GPT-J on the augmented corpus. [PDF, p. 2](https://arxiv.org/pdf/2302.04761v1#page=2) [PDF, p. 3](https://arxiv.org/pdf/2302.04761v1#page=3) [PDF, p. 4](https://arxiv.org/pdf/2302.04761v1#page=4)

**Key result.** On zero-shot SVAMP, the same model scored 29.4 with tools and 6.3 with tool calls disabled. With calls disabled, Toolformer had a perplexity of 10.3 on WikiText and 10.5 on held-out CCNet, matching GPT-J fine-tuned on CCNet. [PDF, p. 6](https://arxiv.org/pdf/2302.04761v1#page=6) [PDF, p. 8](https://arxiv.org/pdf/2302.04761v1#page=8)

**Limitations and scope.** Decoding allowed at most one tool call per example. The training data do not teach the model to combine multiple tool responses, and the decision to call a tool does not account for its cost. [PDF, p. 6](https://arxiv.org/pdf/2302.04761v1#page=6) [PDF, p. 11](https://arxiv.org/pdf/2302.04761v1#page=11)

[Section and table audit for 2302.04761v1](../reviews/audit-2026-11-19/2302.04761v1.md)

## Overview

The method uses self-supervised learning to choose API tools, specify arguments and use their results in subsequent generation. [PDF, p. 1](https://arxiv.org/pdf/2302.04761v1#page=1)

## Source files

arXiv version `2302.04761v1` · PDF pages: 17.

- [Original PDF](https://arxiv.org/pdf/2302.04761v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2302.04761.metadata.json)

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Task planning](../concepts/task-planning.md)
- [Stateful tool use](../concepts/stateful-tool-use.md)
- [Tool evaluation](../concepts/tool-evaluation.md)
- [Tool sandbox](../concepts/tool-sandboxing.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
