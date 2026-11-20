---
type: concept
title: "Stateful tool use"
created: 2026-11-19
tags: ["stateful-tool-use", "research"]
sources: ["https://arxiv.org/abs/2307.16789", "https://arxiv.org/abs/2406.04692", "https://arxiv.org/abs/2309.15817", "https://arxiv.org/abs/2403.02691", "https://arxiv.org/abs/2406.12045", "https://arxiv.org/abs/2408.04682", "https://arxiv.org/abs/2407.18901", "https://arxiv.org/abs/2512.12730", "https://arxiv.org/abs/2112.01488", "https://arxiv.org/abs/2207.05987", "https://arxiv.org/abs/2602.02474", "https://arxiv.org/abs/2606.06448", "https://arxiv.org/abs/2406.04744", "https://arxiv.org/abs/2302.04761", "https://arxiv.org/abs/2310.05223"]
---

# Stateful tool use

Agent actions that make controlled changes to an environment’s state.

**Status:** This page groups papers by topic. An entry in the list indicates **a topical relationship**. It does not imply that every claim is confirmed or that one paper cites another.

## Papers on this topic (18)

- [$\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](../sources/arxiv-2406.12045.md) — The evaluation tests adherence to policy and the required final system state during multi-step interactions involving tools.
- [Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads](../sources/arxiv-2606.06448.md) — The study characterizes the cost and access patterns of memory reads and writes in long-running agent tasks.
- [AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents](../sources/arxiv-2407.18901.md) — Simulated applications and APIs allow agents to be evaluated using state changes and side effects within the environment.
- [ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction](../sources/arxiv-2112.01488.md) — The method combines multi-vector retrieval, late token interaction, representation compression and training with denoised supervision.
- [CRAG -- Comprehensive RAG Benchmark](../sources/arxiv-2406.04744.md) — The benchmark provides diverse questions, answers and simulated APIs for evaluating factual accuracy in RAG systems.
- [Crash-Consistent Checkpointing for AI Training on macOS/APFS](../sources/arxiv-2511.18323.md) — The study compares protocols for persisting checkpoints on macOS/APFS and detecting data corruption with checksums.
- [Do Automatic Test Generation Tools Generate Flaky Tests?](../sources/arxiv-2310.05223.md) — The study examines flaky behavior in automatically generated tests, including sensitivity to the environment and test execution order.
- [DocPrompting: Generating Code by Retrieving the Docs](../sources/arxiv-2207.05987.md) — The study demonstrates code generation using retrieved library and API documentation, including APIs previously unseen by the model.
- [Finding Crash-Consistency Bugs with Bounded Black-Box Crash Testing](../sources/arxiv-1810.02904.md) — The study tests file-system consistency by interrupting writes at controlled points.
- [Identifying the Risks of LM Agents with an LM-Emulated Sandbox](../sources/arxiv-2309.15817.md) — ToolEmu simulates tool calls and assesses risks without executing dangerous scenarios.
- [InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents](../sources/arxiv-2403.02691.md) — The work studies prompt injection via untrusted tool responses, documents and other external data.
- [MemSkill: Learning and Evolving Memory Skills for Self-Evolving Agents](../sources/arxiv-2602.02474.md) — The study investigates how agents learn policies for storing, updating and retrieving memories.
- [Mixture-of-Agents Enhances Large Language Model Capabilities](../sources/arxiv-2406.04692.md) — The method aggregates responses from multiple language models in successive layers as they solve a task.
- [NL2Repo-Bench: Towards Long-Horizon Repository Generation Evaluation of Coding Agents](../sources/arxiv-2512.12730.md) — The benchmark evaluates whether agents can generate complete repositories from natural-language requirements.
- [SquirrelFS: Using the Rust Compiler to Check File-System Crash Consistency](../sources/arxiv-2406.09649.md) — The authors use Rust's type system to enforce safe ordering of file-system writes.
- [Toolformer: Language Models Can Teach Themselves to Use Tools](../sources/arxiv-2302.04761.md) — The method uses self-supervised learning to choose API tools, specify arguments and use their results in subsequent generation.
- [ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs](../sources/arxiv-2307.16789.md) — ToolBench provides methods for training and evaluating agents that call real APIs.
- [ToolSandbox: A Stateful, Conversational, Interactive Evaluation Benchmark for LLM Tool Use Capabilities](../sources/arxiv-2408.04682.md) — The evaluation covers state-dependent tool use, interactions and intermediate steps in addition to the outcome of an individual command.

## Review questions

- How do the papers define the problem and the scope of their evaluation?
- Which conclusions have experimental support, and which are interpretations?
- When do these methods compete, and when do they complement each other?
- Which questions require consulting the full text?
