---
type: source
title: "AgentCoder: Multi-Agent-based Code Generation with Iterative Testing and Optimisation"
created: 2026-11-19
arxiv_id: "2312.13010"
url: "https://arxiv.org/abs/2312.13010"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "coding-agents", "debugging", "workflow-optimization", "benchmarks", "unit-testing"]
source_path: "raw/papers/2312.13010.md"
sources: ["https://arxiv.org/abs/2312.13010"]
ingested: "2026-11-19"
---

# AgentCoder: Multi-Agent-based Code Generation with Iterative Testing and Optimisation

**Paper:** [2312.13010](https://arxiv.org/abs/2312.13010) · [PDF](https://arxiv.org/pdf/2312.13010) · [HTML](https://arxiv.org/html/2312.13010)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** The programmer and test designer generate their outputs independently from the task description. A local script runs the tests and reports failures to the programmer. [PDF, p. 4](https://arxiv.org/pdf/2312.13010v3#page=4) [PDF, p. 5](https://arxiv.org/pdf/2312.13010v3#page=5) [PDF, p. 22](https://arxiv.org/pdf/2312.13010v3#page=22)

**Key result.** With GPT-4, AgentCoder achieved 96.3% pass@1 on HumanEval and 91.8% on MBPP. Agent responses accounted for 56.9 thousand and 66.3 thousand tokens on these benchmarks, respectively. [PDF, p. 6](https://arxiv.org/pdf/2312.13010v3#page=6) [PDF, p. 14](https://arxiv.org/pdf/2312.13010v3#page=14)

**Limitations and scope.** When checked against the reference solution, 89.6% of the GPT-4-generated tests on HumanEval and 91.4% on MBPP were correct. Even the example implementation in Figure 2 accepts a distance equal to the threshold, although the task requires a strictly smaller distance. [PDF, p. 8](https://arxiv.org/pdf/2312.13010v3#page=8) [PDF, p. 15](https://arxiv.org/pdf/2312.13010v3#page=15)

[Section and table audit for 2312.13010v3](../reviews/audit-2026-11-19/2312.13010v3.md)

## Overview

AgentCoder assigns code generation, test design and test execution to separate agents in an iterative repair loop. [PDF, p. 1](https://arxiv.org/pdf/2312.13010v3#page=1)

## Source files

Downloaded version `2312.13010v3` dated 24 May 2024. The title on this record follows arXiv metadata. The title page of the PDF reads *AgentCoder: Multi-Agent Code Generation with Effective Testing and Self-optimisation*. The identifier on that page confirms the version. [arXiv v3 record](https://arxiv.org/abs/2312.13010v3)

- [Original PDF, 24 pages](https://arxiv.org/pdf/2312.13010v3)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2312.13010.metadata.json)

**Finding drawn from the description of the method.** In AgentCoder, a language model designs the tests. A local Python script runs them and reports errors to the programmer agent. Sections 3.2–3.3 on page 5 describe these roles. [PDF, p. 5](https://arxiv.org/pdf/2312.13010v3#page=5)

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Coding agents](../concepts/coding-agents.md)
- [Debugging](../concepts/debugging.md)
- [Workflow optimization](../concepts/workflow-optimization.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Unit tests](../concepts/unit-testing.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
