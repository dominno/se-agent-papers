---
type: concept
title: "Agent and LLM benchmarks"
created: 2026-11-19
tags: ["benchmarks", "research"]
sources: ["https://arxiv.org/abs/2312.13010", "https://arxiv.org/abs/2405.15793", "https://arxiv.org/abs/2607.00990", "https://arxiv.org/abs/2607.27674", "https://arxiv.org/abs/2609.01481", "https://arxiv.org/abs/2307.16789", "https://arxiv.org/abs/2307.13854", "https://arxiv.org/abs/2309.15817", "https://arxiv.org/abs/2403.02691", "https://arxiv.org/abs/2404.07972", "https://arxiv.org/abs/2406.12045", "https://arxiv.org/abs/2408.04682", "https://arxiv.org/abs/2412.14161", "https://arxiv.org/abs/2306.03091", "https://arxiv.org/abs/2310.06770"]
---

# Agent and LLM benchmarks

Test suites that measure model and agent capabilities on repeatable tasks.

**Status:** This page groups papers by topic. An entry in the list indicates **a topical relationship**. It does not imply that every claim is confirmed or that one paper cites another.

## Papers on this topic (79)

- [$\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](../sources/arxiv-2406.12045.md) — The evaluation tests adherence to policy and the required final system state during multi-step interactions involving tools.
- [A Benchmark for Evaluating Repository-Level Code Agents with Intermediate Reasoning on Feature Addition Task](../sources/arxiv-2603.26337.md) — The evaluation covers task analysis, file localization and decomposition of the work alongside the final code.
- [AgentBench: Evaluating LLMs as Agents](../sources/arxiv-2308.03688.md) — The study compares agent reasoning and decisions across eight interactive environments and identifies recurring causes of failure.
- [AgentCoder: Multi-Agent-based Code Generation with Iterative Testing and Optimisation](../sources/arxiv-2312.13010.md) — AgentCoder assigns code generation, test design and test execution to separate agents in an iterative repair loop.
- [AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](../sources/arxiv-2406.13352.md) — The environment tests agents' resilience to prompt injection in external content and tool outputs.
- [AgentLens: Production-Assessed Trajectory Reviews for Coding Agent Evaluation](../sources/arxiv-2607.06624.md) — The study evaluates the quality of a coding agent's execution trace alongside its final result.
- [AgentLens: Revealing The Lucky Pass Problem in SWE-Agent Evaluation](../sources/arxiv-2605.12925.md) — The study examines apparent successes where tests pass despite problems in the agent's execution trace.
- [AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents](../sources/arxiv-2407.18901.md) — Simulated applications and APIs allow agents to be evaluated using state changes and side effects within the environment.
- [ARES: An Automated Evaluation Framework for Retrieval-Augmented Generation Systems](../sources/arxiv-2311.09476.md) — The method combines synthetic data and trained judges with a small set of human judgments to measure RAG relevance and faithfulness.
- [Automated structural testing of LLM-based agents: methods, framework, and case studies](../sources/arxiv-2601.18827.md) — The authors present methods for testing the structure and execution of agent actions, including calls and dependencies between steps.
- [Automated Unit Test Improvement using Large Language Models at Meta](../sources/arxiv-2402.09171.md) — Describes an industrial workflow that uses LLMs to improve existing tests and filters candidate changes for measurable quality gains.
- [Can Large Language Models Resolve Real Java Merge Conflicts? An Evaluation with a Calibrated LLM-as-Judge](../sources/arxiv-2607.27674.md) — The study evaluates models' ability to resolve real Git conflicts in Java projects and the reliability of the evaluation itself.
- [Chain-of-Verification Reduces Hallucination in Large Language Models](../sources/arxiv-2309.11495.md) — The model drafts an answer, devises verification questions and checks them independently before producing a final response.
- [Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering](../sources/arxiv-2401.08500.md) — The authors use a multi-stage, test-driven workflow to generate and revise code in place of a single prompt.
- [CodeT: Code Generation with Generated Tests](../sources/arxiv-2207.10397.md) — The method generates tests for alternative code solutions and uses agreement between outputs to select an implementation.
- [CRAG -- Comprehensive RAG Benchmark](../sources/arxiv-2406.04744.md) — The benchmark provides diverse questions, answers and simulated APIs for evaluating factual accuracy in RAG systems.
- [Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents](../sources/arxiv-2505.22954.md) — The agent edits its own code, tests variants and retains successful changes in an evolutionary archive.
- [DeepSWE: Measuring Frontier Coding Agents on Original, Long-Horizon Engineering Tasks](../sources/arxiv-2607.07946.md) — The authors introduce research tasks for evaluating agents on long-horizon engineering work.
- [Do Automatic Test Generation Tools Generate Flaky Tests?](../sources/arxiv-2310.05223.md) — The study examines flaky behavior in automatically generated tests, including sensitivity to the environment and test execution order.
- [DocPrompting: Generating Code by Retrieving the Docs](../sources/arxiv-2207.05987.md) — The study demonstrates code generation using retrieved library and API documentation, including APIs previously unseen by the model.
- [Does mutation testing improve testing practices?](../sources/arxiv-2103.07189.md) — The study tests whether introducing code mutations reveals gaps in test suites and improves testing practices.
- [Evaluating Very Long-Term Conversational Memory of LLM Agents](../sources/arxiv-2402.17753.md) — LoCoMo is a benchmark of multi-session conversations for evaluating memory and reasoning about events far apart in time.
- [Fact or Fiction: Verifying Scientific Claims](../sources/arxiv-2004.14974.md) — SciFact provides scientific claims and abstracts annotated for support, refutation and the passages that justify each label.
- [FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation](../sources/arxiv-2305.14251.md) — The method decomposes long answers into atomic facts and measures the proportion supported by a trusted source.
- [FeatureBench: Benchmarking Agentic Coding for Complex Feature Development](../sources/arxiv-2602.10975.md) — The benchmark evaluates implementation of complex features spanning multiple files, modules and dependencies.
- [Finding Crash-Consistency Bugs with Bounded Black-Box Crash Testing](../sources/arxiv-1810.02904.md) — The study tests file-system consistency by interrupting writes at controlled points.
- [Fine-Grained Assertion-Based Test Selection](../sources/arxiv-2403.16001.md) — The method selects regression tests at assertion granularity to reduce unnecessary test runs.
- [G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment](../sources/arxiv-2303.16634.md) — A judge model scores generated text against specified criteria. The study examines agreement with human judgments and potential bias.
- [Harness-of-Harness: Multi-Day Autonomous Software Development with Continual Improvement](../sources/arxiv-2609.01481.md) — Studies multiday software development by agents through cycles of planning, implementation, testing and improvement.
- [ICAE-Bench: Evaluating Coding Agents as Interactive Project Builders](../sources/arxiv-2607.21217.md) — The study examines project development through interactions with a user who initially supplies incomplete requirements.
- [Identifying the Risks of LM Agents with an LM-Emulated Sandbox](../sources/arxiv-2309.15817.md) — ToolEmu simulates tool calls and assesses risks without executing dangerous scenarios.
- [InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents](../sources/arxiv-2403.02691.md) — The work studies prompt injection via untrusted tool responses, documents and other external data.
- [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](../sources/arxiv-2306.05685.md) — The study evaluates language models as judges of other models' responses, identifying position bias, verbosity bias and other limitations.
- [KILT: a Benchmark for Knowledge Intensive Language Tasks](../sources/arxiv-2009.02252.md) — The benchmark standardizes knowledge-intensive tasks and evaluates both the answer and the provenance of supporting passages.
- [Large Language Models Are Human-Level Prompt Engineers](../sources/arxiv-2211.01910.md) — Automates instruction generation and selection by evaluating performance on test tasks.
- [LogicHunter: Testing LLM Agent Frameworks with an Agentic Oracle](../sources/arxiv-2607.06195.md) — The method detects semantic bugs in agent frameworks using automated testing and a specialized test oracle.
- [Long-form factuality in large language models](../sources/arxiv-2403.18802.md) — LongFact and SAFE support evaluation of long answers by splitting them into facts and checking those facts against retrieved sources.
- [LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](../sources/arxiv-2410.10813.md) — The benchmark tests long-term memory, temporal reasoning, knowledge updates and appropriate abstention when information is missing.
- [NL2Repo-Bench: Towards Long-Horizon Repository Generation Evaluation of Coding Agents](../sources/arxiv-2512.12730.md) — The benchmark evaluates whether agents can generate complete repositories from natural-language requirements.
- [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](../sources/arxiv-2404.07972.md) — The benchmark tests agents in real desktop environments and automatically evaluates task completion.
- [Practical Detectability for Persistent Lock-Free Data Structures](../sources/arxiv-2203.07621.md) — The study examines how to determine whether an operation completed before a crash and how to recover its result safely.
- [Predictive Test Selection](../sources/arxiv-1810.05286.md) — The study examines how selecting tests relevant to a code change can shorten regression testing.
- [Prometheus 2: An Open Source Language Model Specialized in Evaluating Other Language Models](../sources/arxiv-2405.01535.md) — The authors present an open judge model for absolute scoring and pairwise comparisons using user-defined criteria.
- [Ragas: Automated Evaluation of Retrieval Augmented Generation](../sources/arxiv-2309.15217.md) — The authors define metrics for retrieval, faithfulness to context and generation quality that do not require exhaustive human annotation.
- [RAGBench: Explainable Benchmark for Retrieval-Augmented Generation Systems](../sources/arxiv-2407.11005.md) — The dataset provides cases and interpretable labels for assessing whether retrieved evidence supports an answer.
- [RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems](../sources/arxiv-2306.03091.md) — The benchmark evaluates code completion that requires cross-file knowledge and retrieval of repository context.
- [RepoCoder: Repository-Level Code Completion Through Iterative Retrieval and Generation](../sources/arxiv-2303.12570.md) — The method iteratively retrieves related code and completes implementations across a repository.
- [Repoformer: Selective Retrieval for Repository-Level Code Completion](../sources/arxiv-2403.10059.md) — The method retrieves context selectively when it is expected to help code generation, reducing noise and unnecessary cost.
- [RepoZero: Can LLMs Generate a Code Repository from Scratch?](../sources/arxiv-2605.07122.md) — The study evaluates building a complete repository from scratch using a specification and executable tests.
- [Rethinking the Value of Agent-Generated Tests for LLM-Based Software Engineering Agents](../sources/arxiv-2602.07900.md) — The study examines the value of agent-generated tests and the limits of increasing test counts alone.
- [RoadmapBench: Evaluating Long-Horizon Agentic Software Development Across Version Upgrades](../sources/arxiv-2605.15846.md) — The study examines complex repository changes implemented in stages across successive product releases.
- [SaaSBench: Exploring the Boundaries of Coding Agents in Long-Horizon Enterprise SaaS Engineering](../sources/arxiv-2605.17526.md) — The study evaluates coding agents on long-running tasks that involve building and extending SaaS applications.
- [Scalable and Accurate Application-Level Crash-Consistency Testing via Representative Testing](../sources/arxiv-2503.01390.md) — The paper presents efficient methods for testing application crash consistency during disk operations.
- [SetupBench: Assessing Software Engineering Agents' Ability to Bootstrap Development Environments](../sources/arxiv-2507.09063.md) — The study tests whether agents can set up a development environment, install dependencies and run existing repositories.
- [SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks](../sources/arxiv-2603.24755.md) — The study tracks degradation in code quality and structure as agents repeatedly extend the same project.
- [SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents](../sources/arxiv-2605.21384.md) — Shows how agents can optimize code to pass visible tests while missing the underlying requirements.
- [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](../sources/arxiv-2405.15793.md) — The paper shows how file access, terminal interaction and test execution affect coding-agent performance.
- [SWE-Bench Pro V2: A Cleaner, Harder-to-Game Coding Benchmark](../sources/arxiv-2610.24206.md) — Presents a more difficult, more thoroughly audited set of tasks for evaluating coding agents.
- [SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](../sources/arxiv-2310.06770.md) — The benchmark evaluates fixes for real GitHub issues against existing repositories and their tests.
- [SWE-Chain: Benchmarking Coding Agents on Chained Release-Level Package Upgrades](../sources/arxiv-2605.14415.md) — The benchmark tests whether agents maintain quality across related software updates and successive releases.
- [SWE-Cycle: Benchmarking Code Agents across the Complete Issue Resolution Cycle](../sources/arxiv-2605.13139.md) — The evaluation covers the entire coding task, from setting up the environment to implementation and testing.
- [SWE-Doctor: Guiding Software Engineering Agents with Runtime Diagnosis from Multi-Faceted Bug Reproduction Tests](../sources/arxiv-2607.00990.md) — The method uses diverse bug-reproducing tests to improve fault diagnosis and code repair.
- [SWE-INTERACT: Reimagining SWE Benchmarks as User-Driven Long-Horizon Coding Sessions](../sources/arxiv-2606.30573.md) — The study evaluates coding agents working with a user over multiple turns as requirements change.
- [SWE-Lancer: Can Frontier LLMs Earn $1 Million from Real-World Freelance Software Engineering?](../sources/arxiv-2502.12115.md) — The evaluation measures models' ability to perform realistic, priced software-engineering tasks and make technical decisions.
- [SWE-NFI: Studying and Benchmarking Coding Agents for Non-Functional Improvements](../sources/arxiv-2607.27409.md) — The study evaluates refactoring and code-quality improvements that preserve required functionality.
- [SWE-PolyBench: A Multi-Language Benchmark for Repository-Level Evaluation of Coding Agents](../sources/arxiv-2504.08703.md) — The study compares coding agents on repository-level tasks in several programming languages.
- [SWE-Synth: Synthesizing Verifiable Bug-Fix Data to Enable Large Language Models in Resolving Real-World Bugs](../sources/arxiv-2504.14757.md) — The study describes synthetic generation of code-repair tasks, executable verification and data for model development.
- [Tangent: An Empirical Study of Testing Practices for LLM-Based Agent Applications](../sources/arxiv-2608.08413.md) — The study examines how developers test agent-based applications, including their use of mocks and integration tests.
- [Testing with AI Agents: An Empirical Study of Test Generation Frequency, Quality, and Coverage](../sources/arxiv-2603.13724.md) — The study compares how often agents write tests with the quality and code coverage of those tests.
- [TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks](../sources/arxiv-2412.14161.md) — The environment simulates digital work in a small company, including web browsing, programming and communicating with colleagues.
- [ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs](../sources/arxiv-2307.16789.md) — ToolBench provides methods for training and evaluating agents that call real APIs.
- [ToolSandbox: A Stateful, Conversational, Interactive Evaluation Benchmark for LLM Tool Use Capabilities](../sources/arxiv-2408.04682.md) — The evaluation covers state-dependent tool use, interactions and intermediate steps in addition to the outcome of an individual command.
- [TRACE: A Framework for Analyzing and Enhancing Stepwise Reasoning in Vision-Language Models](../sources/arxiv-2512.05943.md) — The study evaluates detection of incorrect reasoning steps and the consistency of intermediate outputs from vision-language models.
- [Training Software Engineering Agents and Verifiers with SWE-Gym](../sources/arxiv-2412.21139.md) — The authors provide executable tasks and environments for developing and evaluating coding agents and verifiers.
- [Trial by Trace: Benchmarking AI Agent Harnesses for Reliability and Failure Attribution](../sources/arxiv-2610.32285.md) — The study evaluates agent infrastructure reliability and traces failures to their sources using execution traces.
- [ViBench 2.0: A Benchmark for Long-Horizon Software Building](../sources/arxiv-2611.05620.md) — The benchmark evaluates complete applications developed across multiple feature requests, with final product behavior tested in the browser.
- [WebArena: A Realistic Web Environment for Building Autonomous Agents](../sources/arxiv-2307.13854.md) — The benchmark provides reproducible websites and realistic multi-step tasks for browser-based agents.
- [When Agent Evaluation Becomes Unreliable: An Empirical Study of Oracle Failures and Configuration-Dependent Measurement in an LLM Agent Benchmark](../sources/arxiv-2610.16067.md) — The study examines evaluator defects that can inflate or distort reported agent performance.
- [When the Specification Emerges: Benchmarking Faithfulness Loss in Long-Horizon Coding Agents](../sources/arxiv-2603.17104.md) — The evaluation tests whether agents satisfy requirements revealed incrementally during long coding sessions.

## Review questions

- How do the papers define the problem and the scope of their evaluation?
- Which conclusions have experimental support, and which are interpretations?
- When do these methods compete, and when do they complement each other?
- Which questions require consulting the full text?
