---
type: source
title: "Can Large Language Models Resolve Real Java Merge Conflicts? An Evaluation with a Calibrated LLM-as-Judge"
created: 2026-11-19
arxiv_id: "2607.27674"
url: "https://arxiv.org/abs/2607.27674"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["coding-agents", "debugging", "rag-evaluation", "evaluation-metrics", "llm-as-judge", "benchmarks", "comparison-and-reproducibility"]
source_path: "raw/papers/2607.27674.md"
sources: ["https://arxiv.org/abs/2607.27674"]
ingested: "2026-11-19"
---

# Can Large Language Models Resolve Real Java Merge Conflicts? An Evaluation with a Calibrated LLM-as-Judge

**Paper:** [2607.27674](https://arxiv.org/abs/2607.27674) · [PDF](https://arxiv.org/pdf/2607.27674) · [HTML](https://arxiv.org/html/2607.27674)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** ConflictAgent separates solution generation, deterministic structural checks and assessment of agreement with the developer’s decision. On 292 human-labeled pairs, its judge recorded 117 true acceptances, 0 false acceptances and 64 false rejections. [PDF, p. 7](https://arxiv.org/pdf/2607.27674v1#page=7) [PDF, p. 8](https://arxiv.org/pdf/2607.27674v1#page=8) [PDF, p. 9](https://arxiv.org/pdf/2607.27674v1#page=9) [PDF, p. 11](https://arxiv.org/pdf/2607.27674v1#page=11)

**Key result.** Across the same 49 real conflicts, OpenAI matched the developer’s decision in 27/49 (55.1%), Gemini in 29/49 (59.2%) and AutoMerge in 18/49 (36.7%). Among Gemini’s 47 evaluable responses, its match rate was 61.7%. [PDF, p. 11](https://arxiv.org/pdf/2607.27674v1#page=11) [PDF, p. 12](https://arxiv.org/pdf/2607.27674v1#page=12)

**Limitations and scope.** The judge accepted four of five answers that failed structural checks. Calibration on tool outputs does not directly measure judge precision on LLM-generated answers, and structural validity does not establish that a full compilation would succeed. [PDF, p. 11](https://arxiv.org/pdf/2607.27674v1#page=11) [PDF, p. 13](https://arxiv.org/pdf/2607.27674v1#page=13) [PDF, p. 16](https://arxiv.org/pdf/2607.27674v1#page=16)

## Overview

The study evaluates models' ability to resolve real Git conflicts in Java projects and the reliability of the evaluation itself. [PDF, p. 2](https://arxiv.org/pdf/2607.27674v1#page=2)

[Section and evidence audit](../reviews/audit-2026-11-19/2607.27674v1.md)

## Source files

arXiv version `2607.27674v1` · PDF pages: 18.

- [Original PDF](https://arxiv.org/pdf/2607.27674v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2607.27674.metadata.json)

PDF bookmarks — [Results (p. 11)](https://arxiv.org/pdf/2607.27674v1#page=11) · [Threats to Validity (p. 16)](https://arxiv.org/pdf/2607.27674v1#page=16).

## Related concepts

- [Coding agents](../concepts/coding-agents.md)
- [Debugging](../concepts/debugging.md)
- [RAG evaluation](../concepts/rag-evaluation.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [LLM-as-a-Judge](../concepts/llm-as-judge.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
