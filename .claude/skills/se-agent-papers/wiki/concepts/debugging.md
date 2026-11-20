---
type: concept
title: "Debugging"
created: 2026-11-19
tags: ["debugging", "research"]
sources: ["https://arxiv.org/abs/2312.13010", "https://arxiv.org/abs/2404.05427", "https://arxiv.org/abs/2405.15793", "https://arxiv.org/abs/2407.01489", "https://arxiv.org/abs/2410.20285", "https://arxiv.org/abs/2509.25370", "https://arxiv.org/abs/2511.03690", "https://arxiv.org/abs/2603.01327", "https://arxiv.org/abs/2604.03551", "https://arxiv.org/abs/2607.00990", "https://arxiv.org/abs/2607.27674", "https://arxiv.org/abs/2609.01481", "https://arxiv.org/abs/2605.08717", "https://arxiv.org/abs/2608.06346", "https://arxiv.org/abs/2504.14757"]
---

# Debugging

Diagnosing the causes of errors and testing proposed fixes.

**Status:** This page groups papers by topic. An entry in the list indicates **a topical relationship**. It does not imply that every claim is confirmed or that one paper cites another.

## Papers on this topic (22)

- [AgentCoder: Multi-Agent-based Code Generation with Iterative Testing and Optimisation](../sources/arxiv-2312.13010.md) — AgentCoder assigns code generation, test design and test execution to separate agents in an iterative repair loop.
- [AgenticFlict: A Large-Scale Dataset of Merge Conflicts in AI Coding Agent Pull Requests on GitHub](../sources/arxiv-2604.03551.md) — The study analyzes merge conflicts that arise when integrating changes made by coding agents.
- [Agentless: Demystifying LLM-based Software Engineering Agents](../sources/arxiv-2407.01489.md) — The method localizes the fault, generates a patch and validates it through a simple sequence of steps.
- [AutoCodeRover: Autonomous Program Improvement](../sources/arxiv-2404.05427.md) — The method combines structured code search with program analysis to localize faults and generate patches.
- [Can Large Language Models Resolve Real Java Merge Conflicts? An Evaluation with a Calibrated LLM-as-Judge](../sources/arxiv-2607.27674.md) — The study evaluates models' ability to resolve real Git conflicts in Java projects and the reliability of the evaluation itself.
- [Debugging the Debuggers: Failure-Anchored Structured Recovery for Software Engineering Agents](../sources/arxiv-2605.08717.md) — PROBE collects structured failure telemetry, diagnoses the problem and provides controlled guidance when the coding agent retries.
- [Finding and Analyzing Crash-Consistency Bugs in Persistent-Memory File Systems](../sources/arxiv-2204.06066.md) — The study examines metadata persistence and recovery failures in persistent-memory file systems.
- [Finding Crash-Consistency Bugs with Bounded Black-Box Crash Testing](../sources/arxiv-1810.02904.md) — The study tests file-system consistency by interrupting writes at controlled points.
- [From Failed Trajectories to Reliable LLM Agents: Diagnosing and Repairing Harness Flaws](../sources/arxiv-2606.06324.md) — The method analyzes failed trajectories, attributes failures to components of the agent harness and proposes targeted fixes.
- [Harness-of-Harness: Multi-Day Autonomous Software Development with Continual Improvement](../sources/arxiv-2609.01481.md) — Studies multiday software development by agents through cycles of planning, implementation, testing and improvement.
- [Observability and Fault Injection for LLM-Based Multi-Agent Systems in Software Engineering](../sources/arxiv-2608.24271.md) — The method combines distributed tracing of agents with controlled fault injection to diagnose reliability problems.
- [Phantom Guardrails: When Self-Improving Agent Harnesses Fix Failures That Never Happened](../sources/arxiv-2607.13083.md) — The study investigates apparent security improvements made in response to problems for which there is no observational evidence.
- [SWE-Adept: An LLM-Based Agentic Framework for Deep Codebase Analysis and Structured Issue Resolution](../sources/arxiv-2603.01327.md) — The method combines repository analysis, repair planning and checkpoints to support work on complex issues.
- [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](../sources/arxiv-2405.15793.md) — The paper shows how file access, terminal interaction and test execution affect coding-agent performance.
- [SWE-Doctor: Guiding Software Engineering Agents with Runtime Diagnosis from Multi-Faceted Bug Reproduction Tests](../sources/arxiv-2607.00990.md) — The method uses diverse bug-reproducing tests to improve fault diagnosis and code repair.
- [SWE-Search: Enhancing Software Agents with Monte Carlo Tree Search and Iterative Refinement](../sources/arxiv-2410.20285.md) — The study explores candidate patches using tree search and iterative verification.
- [SWE-Synth: Synthesizing Verifiable Bug-Fix Data to Enable Large Language Models in Resolving Real-World Bugs](../sources/arxiv-2504.14757.md) — The study describes synthetic generation of code-repair tasks, executable verification and data for model development.
- [The OpenHands Software Agent SDK: A Composable and Extensible Foundation for Production Agents](../sources/arxiv-2511.03690.md) — The paper describes a modular toolkit for building coding agents, including adapters, a runtime and lifecycle management.
- [TRAJDEBUG: Tracing Error Lifecycle to Identify Critical Failures in Long-Horizon Agent Trajectories](../sources/arxiv-2608.06346.md) — The study follows errors through long agent trajectories and attributes failures to critical steps.
- [Trial by Trace: Benchmarking AI Agent Harnesses for Reliability and Failure Attribution](../sources/arxiv-2610.32285.md) — The study evaluates agent infrastructure reliability and traces failures to their sources using execution traces.
- [When Agent Evaluation Becomes Unreliable: An Empirical Study of Oracle Failures and Configuration-Dependent Measurement in an LLM Agent Benchmark](../sources/arxiv-2610.16067.md) — The study examines evaluator defects that can inflate or distort reported agent performance.
- [Where LLM Agents Fail and How They can Learn From Failures](../sources/arxiv-2509.25370.md) — The paper classifies language-agent failures and examines how agents can improve by learning from earlier errors.

## Review questions

- How do the papers define the problem and the scope of their evaluation?
- Which conclusions have experimental support, and which are interpretations?
- When do these methods compete, and when do they complement each other?
- Which questions require consulting the full text?
