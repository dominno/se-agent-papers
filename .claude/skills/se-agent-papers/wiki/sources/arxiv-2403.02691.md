---
type: source
title: "InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents"
created: 2026-11-19
arxiv_id: "2403.02691"
url: "https://arxiv.org/abs/2403.02691"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "prompt-optimization", "evaluation-metrics", "benchmarks", "stateful-tool-use", "tool-evaluation", "tool-sandboxing", "prompt-injection", "comparison-and-reproducibility"]
source_path: "raw/papers/2403.02691.md"
sources: ["https://arxiv.org/abs/2403.02691"]
ingested: "2026-11-19"
---

# InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents

**Paper:** [2403.02691](https://arxiv.org/abs/2403.02691) · [PDF](https://arxiv.org/pdf/2403.02691) · [HTML](https://arxiv.org/html/2403.02691)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** InjecAgent measures how well tool-using agents distinguish data from authorized instructions. Table 2 covers 1,054 simulated cases per variant. The authors report violation rates among valid responses and among all responses. [PDF, p. 4](https://arxiv.org/pdf/2403.02691v3#page=4) [PDF, p. 5](https://arxiv.org/pdf/2403.02691v3#page=5) [PDF, p. 6](https://arxiv.org/pdf/2403.02691v3#page=6)

**Key result.** For GPT-4 with ReAct in the basic setting, the violation rate was 23.6% among valid responses and 23.3% across all trials. Valid responses accounted for 98.8% of trials. [PDF, p. 5](https://arxiv.org/pdf/2403.02691v3#page=5) [PDF, p. 17](https://arxiv.org/pdf/2403.02691v3#page=17) [PDF, p. 19](https://arxiv.org/pdf/2403.02691v3#page=19)

**Limitations and scope.** Results depend on the simulated situations, model version and response-validity criterion. The use of one fixed variant and the limited diversity of external content restrict claims about robustness in practice. [PDF, p. 6](https://arxiv.org/pdf/2403.02691v3#page=6) [PDF, p. 10](https://arxiv.org/pdf/2403.02691v3#page=10) [PDF, p. 14](https://arxiv.org/pdf/2403.02691v3#page=14) [PDF, p. 15](https://arxiv.org/pdf/2403.02691v3#page=15)

## Overview

The work studies prompt injection via untrusted tool responses, documents and other external data. [PDF, p. 1](https://arxiv.org/pdf/2403.02691v3#page=1)

[Section and evidence audit](../reviews/audit-2026-11-19/2403.02691v3.md)

## Source files

arXiv version `2403.02691v3` · PDF pages: 36.

- [Original PDF](https://arxiv.org/pdf/2403.02691v3)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2403.02691.metadata.json)

PDF bookmarks — [Experiments (p. 5)](https://arxiv.org/pdf/2403.02691v3#page=5) · [Limitations (p. 10)](https://arxiv.org/pdf/2403.02691v3#page=10).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Prompt optimization](../concepts/prompt-optimization.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Stateful tool use](../concepts/stateful-tool-use.md)
- [Tool evaluation](../concepts/tool-evaluation.md)
- [Tool sandbox](../concepts/tool-sandboxing.md)
- [Prompt injection](../concepts/prompt-injection.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
