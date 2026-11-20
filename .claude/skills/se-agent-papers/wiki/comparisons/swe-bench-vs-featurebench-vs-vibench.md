---
type: concept
title: "SWE-bench vs FeatureBench vs ViBench"
created: 2026-11-19
tags: ["comparison", "research-map"]
---

# SWE-bench vs FeatureBench vs ViBench

Resolving issues in existing repositories, adding features across multiple files and building applications in stages are distinct benchmark tasks.

**Note:** This comparison draws on sources at different stages of review. Its conclusions are a narrative synthesis without an A/B experiment or statistical meta-analysis.

## Publications

- [SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](../sources/arxiv-2310.06770.md) — The benchmark evaluates fixes for real GitHub issues against existing repositories and their tests.
- [FeatureBench: Benchmarking Agentic Coding for Complex Feature Development](../sources/arxiv-2602.10975.md) — The benchmark evaluates implementation of complex features spanning multiple files, modules and dependencies.
- [ViBench 2.0: A Benchmark for Long-Horizon Software Building](../sources/arxiv-2611.05620.md) — The benchmark evaluates complete applications developed across multiple feature requests, with final product behavior tested in the browser.

## Criteria for a fair comparison

- Use the same task class and data sources for each method.
- Record the costs of indexing, generation and evaluation.
- Check the limitations and versions of the papers.
- Scores from different benchmarks require a common evaluation before direct comparison.
