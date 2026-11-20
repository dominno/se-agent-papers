---
type: source
title: "AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents"
created: 2026-11-19
arxiv_id: "2407.18901"
url: "https://arxiv.org/abs/2407.18901"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "coding-agents", "evaluation-metrics", "benchmarks", "acceptance-testing", "stateful-tool-use", "tool-evaluation", "comparison-and-reproducibility"]
source_path: "raw/papers/2407.18901.md"
sources: ["https://arxiv.org/abs/2407.18901"]
ingested: "2026-11-19"
---

# AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents

**Paper:** [2407.18901](https://arxiv.org/abs/2407.18901) · [PDF](https://arxiv.org/pdf/2407.18901) · [HTML](https://arxiv.org/html/2407.18901)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** Nine applications and their APIs form an environment for 250 scenarios with three tasks each. Tests check the final state against the requirements and detect unintended changes. [PDF, p. 3](https://arxiv.org/pdf/2407.18901v1#page=3) [PDF, p. 4](https://arxiv.org/pdf/2407.18901v1#page=4) [PDF, p. 5](https://arxiv.org/pdf/2407.18901v1#page=5) [PDF, p. 6](https://arxiv.org/pdf/2407.18901v1#page=6)

**Key result.** GPT-4o with ReAct solved 48.8% of Test-N tasks and 30.2% of Test-C tasks. Requiring all three variants of a scenario to pass reduced these rates to 32.1% and 13.0%. [PDF, p. 8](https://arxiv.org/pdf/2407.18901v1#page=8)

**Limitations and scope.** Test-C includes tasks requiring applications unseen during training. The agent interacts through APIs, so the evaluation does not measure GUI operation. [PDF, p. 6](https://arxiv.org/pdf/2407.18901v1#page=6) [PDF, p. 7](https://arxiv.org/pdf/2407.18901v1#page=7) [PDF, p. 10](https://arxiv.org/pdf/2407.18901v1#page=10)

[Audit of sections, tables and appendices](../reviews/audit-2026-11-19/2407.18901v1.md)

## Overview

Simulated applications and APIs allow agents to be evaluated using state changes and side effects within the environment. [PDF, p. 1](https://arxiv.org/pdf/2407.18901v1#page=1)

## Source files

arXiv version `2407.18901v1` · PDF pages: 55.

- [Original PDF](https://arxiv.org/pdf/2407.18901v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2407.18901.metadata.json)

PDF bookmarks — [Benchmarking Experiments (p. 7)](https://arxiv.org/pdf/2407.18901v1#page=7) · [Limitations (p. 10)](https://arxiv.org/pdf/2407.18901v1#page=10).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Coding agents](../concepts/coding-agents.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Acceptance tests](../concepts/acceptance-testing.md)
- [Stateful tool use](../concepts/stateful-tool-use.md)
- [Tool evaluation](../concepts/tool-evaluation.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
