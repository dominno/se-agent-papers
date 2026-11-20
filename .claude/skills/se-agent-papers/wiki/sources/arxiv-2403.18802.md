---
type: source
title: "Long-form factuality in large language models"
created: 2026-11-19
arxiv_id: "2403.18802"
url: "https://arxiv.org/abs/2403.18802"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["citation-grounding", "claim-verification", "rag-evaluation", "evaluation-metrics", "llm-as-judge", "benchmarks", "comparison-and-reproducibility"]
source_path: "raw/papers/2403.18802.md"
sources: ["https://arxiv.org/abs/2403.18802"]
ingested: "2026-11-19"
---

# Long-form factuality in large language models

**Paper:** [2403.18802](https://arxiv.org/abs/2403.18802) · [PDF](https://arxiv.org/pdf/2403.18802) · [HTML](https://arxiv.org/html/2403.18802)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** SAFE verifies atomic facts with the help of a search engine. Validation against human judgments uses 496 answers with manually extracted facts. Separately, 13 models were compared on 250 LongFact-Objects questions at different preferred answer lengths. [PDF, p. 4](https://arxiv.org/pdf/2403.18802v4#page=4) [PDF, p. 5](https://arxiv.org/pdf/2403.18802v4#page=5) [PDF, p. 6](https://arxiv.org/pdf/2403.18802v4#page=6) [PDF, p. 7](https://arxiv.org/pdf/2403.18802v4#page=7)

**Key result.** SAFE and the original annotators agreed on 11,528 of 16,011 facts (72.0%). In a separate sample of 100 disagreements, reassessment favored SAFE in 76 cases and the original human judgment in 19. [PDF, p. 5](https://arxiv.org/pdf/2403.18802v4#page=5)

**Limitations and scope.** The reassessment covers disagreements only and allows a broader range of sources. Manual decomposition in the validation omits errors made by automatic fact splitting. F1@K also depends on the preferred number of facts. [PDF, p. 5](https://arxiv.org/pdf/2403.18802v4#page=5) [PDF, p. 6](https://arxiv.org/pdf/2403.18802v4#page=6) [PDF, p. 40](https://arxiv.org/pdf/2403.18802v4#page=40) [PDF, p. 44](https://arxiv.org/pdf/2403.18802v4#page=44)

[Audit of sections, tables and appendices](../reviews/audit-2026-11-19/2403.18802v4.md)

## Overview

LongFact and SAFE support evaluation of long answers by splitting them into facts and checking those facts against retrieved sources. [PDF, p. 1](https://arxiv.org/pdf/2403.18802v4#page=1)

## Source files

arXiv version `2403.18802v4` · PDF pages: 72.

- [Original PDF](https://arxiv.org/pdf/2403.18802v4)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2403.18802.metadata.json)

PDF bookmarks — [Limitations (p. 9)](https://arxiv.org/pdf/2403.18802v4#page=9).

## Related concepts

- [Citations and supporting evidence](../concepts/citation-grounding.md)
- [Claim verification](../concepts/claim-verification.md)
- [RAG evaluation](../concepts/rag-evaluation.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [LLM-as-a-Judge](../concepts/llm-as-judge.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
