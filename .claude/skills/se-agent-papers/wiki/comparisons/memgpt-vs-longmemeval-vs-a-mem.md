---
type: concept
title: "MemGPT vs LongMemEval vs A-MEM"
created: 2026-11-19
tags: ["comparison", "research-map"]
---

# MemGPT vs LongMemEval vs A-MEM

MemGPT is a memory architecture, LongMemEval evaluates memory quality, and A-MEM describes linked notes. Each addresses a different question.

**Note:** This comparison draws on sources at different stages of review. Its conclusions are a narrative synthesis without an A/B experiment or statistical meta-analysis.

## Publications

- [MemGPT: Towards LLMs as Operating Systems](../sources/arxiv-2310.08560.md) — The method manages memory hierarchically and moves information between memory levels when the context window is limited.
- [LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](../sources/arxiv-2410.10813.md) — The benchmark tests long-term memory, temporal reasoning, knowledge updates and appropriate abstention when information is missing.
- [A-MEM: Agentic Memory for LLM Agents](../sources/arxiv-2502.12110.md) — The memory system organizes information into a network of linked notes that it updates dynamically.

## Criteria for a fair comparison

- Use the same task class and data sources for each method.
- Record the costs of indexing, generation and evaluation.
- Check the limitations and versions of the papers.
- Scores from different benchmarks require a common evaluation before direct comparison.
