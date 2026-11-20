---
type: concept
title: "FActScore vs SAFE vs SciFact"
created: 2026-11-19
tags: ["comparison", "research-map"]
---

# FActScore vs SAFE vs SciFact

Atomic factuality checks, automated search-based fact-checking and verification of specialized scientific claims use different types of evidence.

**Note:** This comparison draws on sources at different stages of review. Its conclusions are a narrative synthesis without an A/B experiment or statistical meta-analysis.

## Publications

- [FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation](../sources/arxiv-2305.14251.md) — The method decomposes long answers into atomic facts and measures the proportion supported by a trusted source.
- [Long-form factuality in large language models](../sources/arxiv-2403.18802.md) — LongFact and SAFE support evaluation of long answers by splitting them into facts and checking those facts against retrieved sources.
- [Fact or Fiction: Verifying Scientific Claims](../sources/arxiv-2004.14974.md) — SciFact provides scientific claims and abstracts annotated for support, refutation and the passages that justify each label.

## Criteria for a fair comparison

- Use the same task class and data sources for each method.
- Record the costs of indexing, generation and evaluation.
- Check the limitations and versions of the papers.
- Scores from different benchmarks require a common evaluation before direct comparison.
