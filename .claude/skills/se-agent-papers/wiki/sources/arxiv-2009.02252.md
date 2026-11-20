---
type: source
title: "KILT: a Benchmark for Knowledge Intensive Language Tasks"
created: 2026-11-19
arxiv_id: "2009.02252"
url: "https://arxiv.org/abs/2009.02252"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["knowledge-graph", "entity-extraction", "citation-grounding", "grounded-generation", "evaluation-metrics", "benchmarks", "comparison-and-reproducibility"]
source_path: "raw/papers/2009.02252.md"
sources: ["https://arxiv.org/abs/2009.02252"]
ingested: "2026-11-19"
---

# KILT: a Benchmark for Knowledge Intensive Language Tasks

**Paper:** [2009.02252](https://arxiv.org/abs/2009.02252) · [PDF](https://arxiv.org/pdf/2009.02252) · [HTML](https://arxiv.org/html/2009.02252)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** KILT provides a common interface to 11 datasets covering five tasks and links them to the same Wikipedia snapshot, enabling evaluation of answer provenance. [PDF, p. 2](https://arxiv.org/pdf/2009.02252v4#page=2)

**Key result.** On FEVER, RAG assigned 86.31% of labels correctly and scored 53.45% on the metric requiring both the correct label and a complete evidence set. BERT+DPR scored 69.68% and 58.58%, respectively, reversing the ranking when evidence was required. [PDF, p. 8](https://arxiv.org/pdf/2009.02252v4#page=8) [PDF, p. 9](https://arxiv.org/pdf/2009.02252v4#page=9) [PDF, p. 17](https://arxiv.org/pdf/2009.02252v4#page=17)

**Limitations and scope.** All tasks use the 1 August 2019 Wikipedia snapshot. Results depend on its coverage. [PDF, p. 3](https://arxiv.org/pdf/2009.02252v4#page=3)

[Audit report for 2009.02252v4](../reviews/audit-2026-11-19/2009.02252v4.md)

## Overview

The benchmark standardizes knowledge-intensive tasks and evaluates both the answer and the provenance of supporting passages. [PDF, p. 1](https://arxiv.org/pdf/2009.02252v4#page=1)

## Source files

arXiv version `2009.02252v4` · PDF pages: 22.

- [Original PDF](https://arxiv.org/pdf/2009.02252v4)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2009.02252.metadata.json)

## Related concepts

- [Knowledge graph](../concepts/knowledge-graph.md)
- [Entity extraction](../concepts/entity-extraction.md)
- [Citations and supporting evidence](../concepts/citation-grounding.md)
- [Source-grounded generation](../concepts/grounded-generation.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
