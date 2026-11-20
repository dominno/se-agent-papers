---
type: concept
title: "ToolSandbox vs AppWorld vs AgentDojo"
created: 2026-11-19
tags: ["comparison", "research-map"]
---

# ToolSandbox vs AppWorld vs AgentDojo

Stateful tool use, verification of action effects in applications and resistance to prompt injection measure different aspects of agent behavior.

**Note:** This comparison draws on sources at different stages of review. Its conclusions are a narrative synthesis without an A/B experiment or statistical meta-analysis.

## Publications

- [ToolSandbox: A Stateful, Conversational, Interactive Evaluation Benchmark for LLM Tool Use Capabilities](../sources/arxiv-2408.04682.md) — The evaluation covers state-dependent tool use, interactions and intermediate steps in addition to the outcome of an individual command.
- [AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents](../sources/arxiv-2407.18901.md) — Simulated applications and APIs allow agents to be evaluated using state changes and side effects within the environment.
- [AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](../sources/arxiv-2406.13352.md) — The environment tests agents' resilience to prompt injection in external content and tool outputs.

## Criteria for a fair comparison

- Use the same task class and data sources for each method.
- Record the costs of indexing, generation and evaluation.
- Check the limitations and versions of the papers.
- Scores from different benchmarks require a common evaluation before direct comparison.
