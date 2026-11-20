---
type: concept
title: "DSPy vs AFlow vs TextGrad"
created: 2026-11-19
tags: ["comparison", "research-map"]
---

# DSPy vs AFlow vs TextGrad

Compiling a declarative LLM program, searching over workflows and using gradient-like textual feedback each optimize different parts of a system.

**Note:** This comparison draws on sources at different stages of review. Its conclusions are a narrative synthesis without an A/B experiment or statistical meta-analysis.

## Publications

- [DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines](../sources/arxiv-2310.03714.md) — The framework treats LLM programs as declarative modules whose demonstrations and instructions can be optimized against a measurable objective.
- [AFlow: Automating Agentic Workflow Generation](../sources/arxiv-2410.10762.md) — The method optimizes agent workflow graphs using search and feedback from executed tasks.
- [TextGrad: Automatic "Differentiation" via Text](../sources/arxiv-2406.07496.md) — The method uses textual feedback to iteratively improve components of complex AI systems.

## Criteria for a fair comparison

- Use the same task class and data sources for each method.
- Record the costs of indexing, generation and evaluation.
- Check the limitations and versions of the papers.
- Scores from different benchmarks require a common evaluation before direct comparison.
