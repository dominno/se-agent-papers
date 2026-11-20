---
type: source
title: "Chain-of-Verification Reduces Hallucination in Large Language Models"
created: 2026-11-19
arxiv_id: "2309.11495"
url: "https://arxiv.org/abs/2309.11495"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["task-planning", "citation-grounding", "grounded-generation", "rag-evaluation", "evaluation-metrics", "llm-as-judge", "benchmarks", "comparison-and-reproducibility"]
source_path: "raw/papers/2309.11495.md"
sources: ["https://arxiv.org/abs/2309.11495"]
ingested: "2026-11-19"
---

# Chain-of-Verification Reduces Hallucination in Large Language Models

**Paper:** [2309.11495](https://arxiv.org/abs/2309.11495) · [PDF](https://arxiv.org/pdf/2309.11495) · [HTML](https://arxiv.org/html/2309.11495)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** Chain-of-Verification generates a draft, verification questions and fresh answers used to revise the draft. In the factored variant, the model answers each question separately. The factor+revise variant also compares each answer with the original claim. [PDF, p. 3](https://arxiv.org/pdf/2309.11495v2#page=3) [PDF, p. 4](https://arxiv.org/pdf/2309.11495v2#page=4) [PDF, p. 5](https://arxiv.org/pdf/2309.11495v2#page=5) [PDF, p. 13](https://arxiv.org/pdf/2309.11495v2#page=13)

**Key result.** On closed-book MultiSpanQA, the factored variant raised Llama 65B F1 from 0.39 to 0.48. For biographies, factor+revise raised FACTSCORE from 55.9 to 71.4 while reducing the mean number of facts from 16.6 to 12.3. [PDF, p. 7](https://arxiv.org/pdf/2309.11495v2#page=7)

**Limitations and scope.** Verification without an external source depends on the model’s knowledge and increases the number of generated tokens. For Wiki-Category/two-step, the 0.21 precision in Table 1 cannot be reproduced from the reported means of 0.50 correct items and 0.52 incorrect items. [PDF, p. 5](https://arxiv.org/pdf/2309.11495v2#page=5) [PDF, p. 6](https://arxiv.org/pdf/2309.11495v2#page=6) [PDF, p. 9](https://arxiv.org/pdf/2309.11495v2#page=9)

## Overview

The model drafts an answer, devises verification questions and checks them independently before producing a final response. [PDF, p. 1](https://arxiv.org/pdf/2309.11495v2#page=1)

[Section and evidence audit](../reviews/audit-2026-11-19/2309.11495v2.md)

## Source files

arXiv version `2309.11495v2` · PDF pages: 19.

- [Original PDF](https://arxiv.org/pdf/2309.11495v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2309.11495.metadata.json)

PDF bookmarks — [Experiments (p. 5)](https://arxiv.org/pdf/2309.11495v2#page=5) · [Limitations (p. 9)](https://arxiv.org/pdf/2309.11495v2#page=9).

## Related concepts

- [Task planning](../concepts/task-planning.md)
- [Citations and supporting evidence](../concepts/citation-grounding.md)
- [Source-grounded generation](../concepts/grounded-generation.md)
- [RAG evaluation](../concepts/rag-evaluation.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [LLM-as-a-Judge](../concepts/llm-as-judge.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
