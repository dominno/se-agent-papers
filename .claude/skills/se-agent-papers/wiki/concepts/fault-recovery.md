---
type: concept
title: "Crash recovery"
created: 2026-11-19
tags: ["fault-recovery", "research"]
sources: ["https://arxiv.org/abs/2509.25370", "https://arxiv.org/abs/2605.08717", "https://arxiv.org/abs/2608.06346", "https://arxiv.org/abs/2610.16067", "https://arxiv.org/abs/2610.32285", "https://arxiv.org/abs/2608.24271", "https://arxiv.org/abs/2606.06324", "https://arxiv.org/abs/2607.13083", "https://arxiv.org/abs/1810.02904", "https://arxiv.org/abs/1811.00757", "https://arxiv.org/abs/2204.06066", "https://arxiv.org/abs/2211.07631", "https://arxiv.org/abs/2406.09649", "https://arxiv.org/abs/2503.01390", "https://arxiv.org/abs/2511.18323"]
---

# Crash recovery

Resuming operations and identifying failed steps.

**Status:** This page groups papers by topic. An entry in the list indicates **a topical relationship**. It does not imply that every claim is confirmed or that one paper cites another.

## Papers on this topic (15)

- [Crash-Consistent Checkpointing for AI Training on macOS/APFS](../sources/arxiv-2511.18323.md) — The study compares protocols for persisting checkpoints on macOS/APFS and detecting data corruption with checksums.
- [Debugging the Debuggers: Failure-Anchored Structured Recovery for Software Engineering Agents](../sources/arxiv-2605.08717.md) — PROBE collects structured failure telemetry, diagnoses the problem and provides controlled guidance when the coding agent retries.
- [DurableFS: A File System for Persistent Memory](../sources/arxiv-1811.00757.md) — The paper describes atomic, durable file-system operations based on logging and copy-on-write.
- [Finding and Analyzing Crash-Consistency Bugs in Persistent-Memory File Systems](../sources/arxiv-2204.06066.md) — The study examines metadata persistence and recovery failures in persistent-memory file systems.
- [Finding Crash-Consistency Bugs with Bounded Black-Box Crash Testing](../sources/arxiv-1810.02904.md) — The study tests file-system consistency by interrupting writes at controlled points.
- [From Failed Trajectories to Reliable LLM Agents: Diagnosing and Repairing Harness Flaws](../sources/arxiv-2606.06324.md) — The method analyzes failed trajectories, attributes failures to components of the agent harness and proposes targeted fixes.
- [Observability and Fault Injection for LLM-Based Multi-Agent Systems in Software Engineering](../sources/arxiv-2608.24271.md) — The method combines distributed tracing of agents with controlled fault injection to diagnose reliability problems.
- [Phantom Guardrails: When Self-Improving Agent Harnesses Fix Failures That Never Happened](../sources/arxiv-2607.13083.md) — The study investigates apparent security improvements made in response to problems for which there is no observational evidence.
- [Scalable and Accurate Application-Level Crash-Consistency Testing via Representative Testing](../sources/arxiv-2503.01390.md) — The paper presents efficient methods for testing application crash consistency during disk operations.
- [SquirrelFS: Using the Rust Compiler to Check File-System Crash Consistency](../sources/arxiv-2406.09649.md) — The authors use Rust's type system to enforce safe ordering of file-system writes.
- [The Path to Durable Linearizability](../sources/arxiv-2211.07631.md) — The authors formalize correctness for concurrent operations whose effects must remain consistent across crashes.
- [TRAJDEBUG: Tracing Error Lifecycle to Identify Critical Failures in Long-Horizon Agent Trajectories](../sources/arxiv-2608.06346.md) — The study follows errors through long agent trajectories and attributes failures to critical steps.
- [Trial by Trace: Benchmarking AI Agent Harnesses for Reliability and Failure Attribution](../sources/arxiv-2610.32285.md) — The study evaluates agent infrastructure reliability and traces failures to their sources using execution traces.
- [When Agent Evaluation Becomes Unreliable: An Empirical Study of Oracle Failures and Configuration-Dependent Measurement in an LLM Agent Benchmark](../sources/arxiv-2610.16067.md) — The study examines evaluator defects that can inflate or distort reported agent performance.
- [Where LLM Agents Fail and How They can Learn From Failures](../sources/arxiv-2509.25370.md) — The paper classifies language-agent failures and examines how agents can improve by learning from earlier errors.

## Review questions

- How do the papers define the problem and the scope of their evaluation?
- Which conclusions have experimental support, and which are interpretations?
- When do these methods compete, and when do they complement each other?
- Which questions require consulting the full text?
