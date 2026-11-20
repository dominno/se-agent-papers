---
type: source
title: "Fact or Fiction: Verifying Scientific Claims"
created: 2026-11-19
arxiv_id: "2004.14974"
url: "https://arxiv.org/abs/2004.14974"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["citation-grounding", "claim-verification", "grounded-generation", "rag-evaluation", "evaluation-metrics", "llm-as-judge", "benchmarks", "comparison-and-reproducibility"]
source_path: "raw/papers/2004.14974.md"
sources: ["https://arxiv.org/abs/2004.14974"]
ingested: "2026-11-19"
---

# Fact or Fiction: Verifying Scientific Claims

**Paper:** [2004.14974](https://arxiv.org/abs/2004.14974) · [PDF](https://arxiv.org/pdf/2004.14974) · [HTML](https://arxiv.org/html/2004.14974)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** SciFact contains 1,409 claims for verification against 5,183 abstracts. VeriSci retrieves three documents, selects rationale sentences and labels each claim–abstract pair. [PDF, p. 3](https://arxiv.org/pdf/2004.14974v6#page=3) [PDF, p. 5](https://arxiv.org/pdf/2004.14974v6#page=5) [PDF, p. 6](https://arxiv.org/pdf/2004.14974v6#page=6) [PDF, p. 7](https://arxiv.org/pdf/2004.14974v6#page=7)

**Key result.** On validation with gold evidence, label accuracy reached 81.9% after training on FEVER and SciFact, versus 67.6% after training on FEVER alone. In the full open-domain test, joint label-and-rationale F1 was 46.5 versus 36.4 for the zero-shot variant. [PDF, p. 6](https://arxiv.org/pdf/2004.14974v6#page=6) [PDF, p. 7](https://arxiv.org/pdf/2004.14974v6#page=7)

**Limitations and scope.** An abstract may support or refute a claim even when other sources contradict it. The dataset is predominantly biomedical. The counts in Figure 2 sum to 5,000, while the text and released corpus give 5,183. [PDF, p. 2](https://arxiv.org/pdf/2004.14974v6#page=2) [PDF, p. 3](https://arxiv.org/pdf/2004.14974v6#page=3) [PDF, p. 4](https://arxiv.org/pdf/2004.14974v6#page=4) [PDF, p. 14](https://arxiv.org/pdf/2004.14974v6#page=14)

## Overview

SciFact provides scientific claims and abstracts annotated for support, refutation and the passages that justify each label. [PDF, p. 1](https://arxiv.org/pdf/2004.14974v6#page=1)

[Section and evidence audit](../reviews/audit-2026-11-19/2004.14974v6.md)

## Source files

arXiv version `2004.14974v6` · PDF pages: 17.

- [Original PDF](https://arxiv.org/pdf/2004.14974v6)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2004.14974.metadata.json)

## Related concepts

- [Citations and supporting evidence](../concepts/citation-grounding.md)
- [Claim verification](../concepts/claim-verification.md)
- [Source-grounded generation](../concepts/grounded-generation.md)
- [RAG evaluation](../concepts/rag-evaluation.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [LLM-as-a-Judge](../concepts/llm-as-judge.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
