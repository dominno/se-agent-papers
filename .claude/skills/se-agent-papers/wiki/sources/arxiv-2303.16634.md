---
type: source
title: "G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment"
created: 2026-11-19
arxiv_id: "2303.16634"
url: "https://arxiv.org/abs/2303.16634"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["citation-grounding", "rag-evaluation", "evaluation-metrics", "llm-as-judge", "benchmarks", "comparison-and-reproducibility"]
source_path: "raw/papers/2303.16634.md"
sources: ["https://arxiv.org/abs/2303.16634"]
ingested: "2026-11-19"
---

# G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment

**Paper:** [2303.16634](https://arxiv.org/abs/2303.16634) · [PDF](https://arxiv.org/pdf/2303.16634) · [HTML](https://arxiv.org/html/2303.16634)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** G-EVAL generates evaluation steps, fills in a form and computes a weighted mean of scores. For GPT-4, probabilities were estimated from 20 samples at temperature 1. Agreement with humans was studied on SummEval, Topical-Chat and QAGS. [PDF, p. 2](https://arxiv.org/pdf/2303.16634v3#page=2) [PDF, p. 3](https://arxiv.org/pdf/2303.16634v3#page=3) [PDF, p. 4](https://arxiv.org/pdf/2303.16634v3#page=4)

**Key result.** On SummEval, the AVG column reports a Spearman correlation of 0.514 for G-EVAL-4 and 0.474 for UniEval. The simple mean of G-EVAL-4's four published values rounds to 0.523. [PDF, p. 1](https://arxiv.org/pdf/2303.16634v3#page=1) [PDF, p. 4](https://arxiv.org/pdf/2303.16634v3#page=4)

**Limitations and scope.** In all three groups of summaries defined by human preference, the GPT-4 judge gave GPT-3.5 text a higher mean score. Agreement among human raters in the cited dataset was low (α = 0.07), making the source of the difference difficult to identify. [PDF, p. 5](https://arxiv.org/pdf/2303.16634v3#page=5) [PDF, p. 6](https://arxiv.org/pdf/2303.16634v3#page=6)

## Overview

A judge model scores generated text against specified criteria. The study examines agreement with human judgments and potential bias. [PDF, p. 1](https://arxiv.org/pdf/2303.16634v3#page=1)

[Section and evidence audit](../reviews/audit-2026-11-19/2303.16634v3.md)

## Source files

arXiv version `2303.16634v3` · PDF pages: 11.

- [Original PDF](https://arxiv.org/pdf/2303.16634v3)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2303.16634.metadata.json)

## Related concepts

- [Citations and supporting evidence](../concepts/citation-grounding.md)
- [RAG evaluation](../concepts/rag-evaluation.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [LLM-as-a-Judge](../concepts/llm-as-judge.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
