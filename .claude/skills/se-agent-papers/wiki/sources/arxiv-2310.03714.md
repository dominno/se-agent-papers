---
type: source
title: "DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines"
created: 2026-11-19
arxiv_id: "2310.03714"
url: "https://arxiv.org/abs/2310.03714"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["coding-agents", "self-evolution", "prompt-optimization", "workflow-optimization", "evaluation-metrics"]
source_path: "raw/papers/2310.03714.md"
sources: ["https://arxiv.org/abs/2310.03714"]
ingested: "2026-11-19"
---

# DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines

**Paper:** [2310.03714](https://arxiv.org/abs/2310.03714) · [PDF](https://arxiv.org/pdf/2310.03714) · [HTML](https://arxiv.org/html/2310.03714)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** DSPy compiles a modular program against a target metric. Its bootstrapping procedure uses successful traces to select demonstrations for individual modules. [PDF, p. 4](https://arxiv.org/pdf/2310.03714v1#page=4) [PDF, p. 5](https://arxiv.org/pdf/2310.03714v1#page=5) [PDF, p. 6](https://arxiv.org/pdf/2310.03714v1#page=6) [PDF, p. 28](https://arxiv.org/pdf/2310.03714v1#page=28)

**Key result.** On GSM8K, GPT-3.5 scored 81.6% on the test with CoT, bootstrapping and ensembling, compared with 72.4% with manual CoT demonstrations. On HotPotQA, multi-hop bootstrapping scored 39.6 exact match, compared with 31.2 for few-shot prompting. [PDF, p. 8](https://arxiv.org/pdf/2310.03714v1#page=8) [PDF, p. 11](https://arxiv.org/pdf/2310.03714v1#page=11)

**Limitations and scope.** Results depend on the validation metric, data and cost of trials. HotPotQA uses a sample of the official development set as the test set. The starred result of 45.6 exact match was evaluated on half of that sample. [PDF, p. 5](https://arxiv.org/pdf/2310.03714v1#page=5) [PDF, p. 10](https://arxiv.org/pdf/2310.03714v1#page=10) [PDF, p. 11](https://arxiv.org/pdf/2310.03714v1#page=11)

[Section and table audit for 2310.03714v1](../reviews/audit-2026-11-19/2310.03714v1.md)

## Overview

The framework treats LLM programs as declarative modules whose demonstrations and instructions can be optimized against a measurable objective. [PDF, p. 1](https://arxiv.org/pdf/2310.03714v1#page=1)

## Section notes

**Mechanism:** DSPy uses declarative signatures, composable modules and teleprompters or optimizers to tune multi-step model calls against a validation metric. [PDF, p. 3](https://arxiv.org/pdf/2310.03714v1#page=3) · [PDF, p. 5](https://arxiv.org/pdf/2310.03714v1#page=5)

**Evaluation and study settings:** The case studies cover mathematics and complex questions. Optimization tests alternatives against examples and metrics. [PDF, p. 1](https://arxiv.org/pdf/2310.03714v1#page=1) · [PDF, p. 2](https://arxiv.org/pdf/2310.03714v1#page=2)

**Scope and interpretation:** Optimization depends on the metric and the training and validation data. Improvement outside the evaluation distribution is not guaranteed. [PDF, p. 5](https://arxiv.org/pdf/2310.03714v1#page=5)

**Sections checked:** 3 The DSPy Programming Model, 4 The DSPy Compiler, 6 Case Study, 7 Case Study. [Read the paper](https://arxiv.org/html/2310.03714).


## Source files

arXiv version `2310.03714v1` · PDF pages: 32.

- [Original PDF](https://arxiv.org/pdf/2310.03714v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2310.03714.metadata.json)

## Related concepts

- [Coding agents](../concepts/coding-agents.md)
- [Agent self-improvement](../concepts/self-evolution.md)
- [Prompt optimization](../concepts/prompt-optimization.md)
- [Workflow optimization](../concepts/workflow-optimization.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.

## Findings and caveats

- [Finding 1 — method](../concepts/finding-2310-03714-1.md)
- [Finding 2 — evaluation](../concepts/finding-2310-03714-2.md)
- [Finding 3 — interpretive caveat](../concepts/finding-2310-03714-3.md)
