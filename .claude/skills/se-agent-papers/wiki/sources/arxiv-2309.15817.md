---
type: source
title: "Identifying the Risks of LM Agents with an LM-Emulated Sandbox"
created: 2026-11-19
arxiv_id: "2309.15817"
url: "https://arxiv.org/abs/2309.15817"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "evaluation-metrics", "benchmarks", "stateful-tool-use", "tool-evaluation", "tool-sandboxing", "comparison-and-reproducibility"]
source_path: "raw/papers/2309.15817.md"
sources: ["https://arxiv.org/abs/2309.15817"]
ingested: "2026-11-19"
---

# Identifying the Risks of LM Agents with an LM-Emulated Sandbox

**Paper:** [2309.15817](https://arxiv.org/abs/2309.15817) · [PDF](https://arxiv.org/pdf/2309.15817) · [HTML](https://arxiv.org/html/2309.15817)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** Separate models emulate the tools and evaluate agent behavior. The authors ran the same agent twice on each of 100 validation scenarios, once with each emulator variant. [PDF, p. 5](https://arxiv.org/pdf/2309.15817v2#page=5) [PDF, p. 7](https://arxiv.org/pdf/2309.15817v2#page=7) [PDF, p. 9](https://arxiv.org/pdf/2309.15817v2#page=9)

**Key result.** In Table 3, 72.5% of the standard emulator's flagged failures were genuine, compared with 68.8% for the challenging-scenario emulator. Genuine identified failures as a share of all cases were 39.6% and 50.0%, respectively. [PDF, p. 10](https://arxiv.org/pdf/2309.15817v2#page=10)

**Limitations and scope.** External annotators judged 91.9% of standard simulations and 85.6% of challenging simulations free of critical issues. Table 3 reports one standard error. Only selected cases were directly reproduced. [PDF, p. 9](https://arxiv.org/pdf/2309.15817v2#page=9) [PDF, p. 10](https://arxiv.org/pdf/2309.15817v2#page=10) [PDF, p. 41](https://arxiv.org/pdf/2309.15817v2#page=41)

[Audit of sections, tables and appendices](../reviews/audit-2026-11-19/2309.15817v2.md)

## Overview

ToolEmu simulates tool calls and assesses risks without executing dangerous scenarios. [PDF, p. 1](https://arxiv.org/pdf/2309.15817v2#page=1)

## Source files

arXiv version `2309.15817v2` · PDF pages: 70.

- [Original PDF](https://arxiv.org/pdf/2309.15817v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2309.15817.metadata.json)

PDF bookmarks — [Limitations & Future Directions (p. 13)](https://arxiv.org/pdf/2309.15817v2#page=13).

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
