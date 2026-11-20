---
type: source
title: "Mixture-of-Agents Enhances Large Language Model Capabilities"
created: 2026-11-19
arxiv_id: "2406.04692"
url: "https://arxiv.org/abs/2406.04692"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "stateful-tool-use", "tool-evaluation", "tool-sandboxing"]
source_path: "raw/papers/2406.04692.md"
sources: ["https://arxiv.org/abs/2406.04692"]
ingested: "2026-11-19"
---

# Mixture-of-Agents Enhances Large Language Model Capabilities

**Paper:** [2406.04692](https://arxiv.org/abs/2406.04692) · [PDF](https://arxiv.org/pdf/2406.04692) · [HTML](https://arxiv.org/html/2406.04692)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** Models run in layers. Each model in a subsequent layer uses the preceding models' answers to formulate its own. [PDF, p. 1](https://arxiv.org/pdf/2406.04692v1#page=1)

**Key result.** On 805 AlpacaEval 2.0 instructions, the open-model MoA configuration achieved a length-controlled win rate of 65.1 ± 0.6% over three runs, compared with 57.5% for GPT-4o. The 7.6-point difference compares the systems against the same GPT-4 Preview reference response. [PDF, p. 5](https://arxiv.org/pdf/2406.04692v1#page=5)

**Limitations and scope.** The successive layers must finish before the final answer can begin, increasing time to first token. [PDF, p. 9](https://arxiv.org/pdf/2406.04692v1#page=9)

[Audit report for 2406.04692v1](../reviews/audit-2026-11-19/2406.04692v1.md)

## Overview

The method aggregates responses from multiple language models in successive layers as they solve a task. [PDF, p. 1](https://arxiv.org/pdf/2406.04692v1#page=1)

## Source files

arXiv version `2406.04692v1` · PDF pages: 15.

- [Original PDF](https://arxiv.org/pdf/2406.04692v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2406.04692.metadata.json)

PDF bookmarks — [Mixture-of-Agents Methodology (p. 3)](https://arxiv.org/pdf/2406.04692v1#page=3) · [Evaluation (p. 4)](https://arxiv.org/pdf/2406.04692v1#page=4).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Stateful tool use](../concepts/stateful-tool-use.md)
- [Tool evaluation](../concepts/tool-evaluation.md)
- [Tool sandbox](../concepts/tool-sandboxing.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
