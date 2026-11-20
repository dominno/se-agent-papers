---
type: source
title: "$\\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains"
created: 2026-11-19
arxiv_id: "2406.12045"
url: "https://arxiv.org/abs/2406.12045"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "evaluation-metrics", "benchmarks", "stateful-tool-use", "tool-evaluation", "tool-sandboxing", "comparison-and-reproducibility"]
source_path: "raw/papers/2406.12045.md"
sources: ["https://arxiv.org/abs/2406.12045"]
ingested: "2026-11-19"
---

# $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

**Paper:** [2406.12045](https://arxiv.org/abs/2406.12045) · [PDF](https://arxiv.org/pdf/2406.12045) · [HTML](https://arxiv.org/html/2406.12045)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** A model plays the user, while the agent acts through APIs under domain policy. The verifier compares the database state with the goal and checks required information when the task calls for it. [PDF, p. 3](https://arxiv.org/pdf/2406.12045v1#page=3) [PDF, p. 4](https://arxiv.org/pdf/2406.12045v1#page=4) [PDF, p. 5](https://arxiv.org/pdf/2406.12045v1#page=5)

**Key result.** GPT-4o with function calling had an average single-trial success rate of 61.2% in retail and 35.2% in airline tasks. In retail, the probability of passing all eight trials of the same task fell below 25%. [PDF, p. 7](https://arxiv.org/pdf/2406.12045v1#page=7)

**Limitations and scope.** The sample includes two domains and a simulated customer. The 48.2% mean weights the domains equally despite their different task counts, 115 and 50. [PDF, p. 5](https://arxiv.org/pdf/2406.12045v1#page=5) [PDF, p. 7](https://arxiv.org/pdf/2406.12045v1#page=7) [PDF, p. 9](https://arxiv.org/pdf/2406.12045v1#page=9)

[Audit report for 2406.12045v1](../reviews/audit-2026-11-19/2406.12045v1.md)

## Overview

The evaluation tests adherence to policy and the required final system state during multi-step interactions involving tools. [PDF, p. 1](https://arxiv.org/pdf/2406.12045v1#page=1)

## Source files

arXiv version `2406.12045v1` · PDF pages: 50.

- [Original PDF](https://arxiv.org/pdf/2406.12045v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2406.12045.metadata.json)

PDF bookmarks — [Experiments (p. 6)](https://arxiv.org/pdf/2406.12045v1#page=6).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Stateful tool use](../concepts/stateful-tool-use.md)
- [Tool evaluation](../concepts/tool-evaluation.md)
- [Tool sandbox](../concepts/tool-sandboxing.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
