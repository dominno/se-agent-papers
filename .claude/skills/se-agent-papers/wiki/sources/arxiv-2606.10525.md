---
type: source
title: "Assessing Automated Prompt Injection Attacks in Agentic Environments"
created: 2026-11-19
arxiv_id: "2606.10525"
url: "https://arxiv.org/abs/2606.10525"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "prompt-optimization", "tool-sandboxing", "prompt-injection", "observability"]
source_path: "raw/papers/2606.10525.md"
sources: ["https://arxiv.org/abs/2606.10525"]
ingested: "2026-11-19"
---

# Assessing Automated Prompt Injection Attacks in Agentic Environments

**Paper:** [2606.10525](https://arxiv.org/abs/2606.10525) · [PDF](https://arxiv.org/pdf/2606.10525) · [HTML](https://arxiv.org/html/2606.10525)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** The authors evaluate robustness to untrusted content in AgentDojo using 80 task pairs across four domains. Deterministic rules verify the final effect in the environment. An LLM judge plays a separate, supporting role. [PDF, p. 5](https://arxiv.org/pdf/2606.10525v1#page=5) [PDF, p. 6](https://arxiv.org/pdf/2606.10525v1#page=6) [PDF, p. 9](https://arxiv.org/pdf/2606.10525v1#page=9)

**Key result.** Against environment state, the auxiliary judge achieved 100% sensitivity but only 47.8% precision in the pooled confusion matrix. Of 642 predicted successes, 335 were false positives. [PDF, p. 8](https://arxiv.org/pdf/2606.10525v1#page=8) [PDF, p. 9](https://arxiv.org/pdf/2606.10525v1#page=9)

**Limitations and scope.** The results cover selected tasks and models in AgentDojo. Large differences in target-event prevalence between models affect judge accuracy within each group. [PDF, p. 8](https://arxiv.org/pdf/2606.10525v1#page=8) [PDF, p. 9](https://arxiv.org/pdf/2606.10525v1#page=9) [PDF, p. 11](https://arxiv.org/pdf/2606.10525v1#page=11)

## Overview

The study evaluates automatically generated prompt-injection attacks against tool-using agents. [PDF, p. 1](https://arxiv.org/pdf/2606.10525v1#page=1)

[Section and evidence audit](../reviews/audit-2026-11-19/2606.10525v1.md)

## Source files

arXiv version `2606.10525v1` · PDF pages: 17.

- [Original PDF](https://arxiv.org/pdf/2606.10525v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2606.10525.metadata.json)

PDF bookmarks — [5 Methodology (p. 4)](https://arxiv.org/pdf/2606.10525v1#page=4) · [6 Experiments (p. 5)](https://arxiv.org/pdf/2606.10525v1#page=5).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Prompt optimization](../concepts/prompt-optimization.md)
- [Tool sandbox](../concepts/tool-sandboxing.md)
- [Prompt injection](../concepts/prompt-injection.md)
- [Agent observability](../concepts/observability.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
