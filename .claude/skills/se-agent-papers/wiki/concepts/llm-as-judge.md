---
type: concept
title: "LLM-as-a-Judge"
created: 2026-11-19
tags: ["llm-as-judge", "research"]
sources: ["https://arxiv.org/abs/2607.27674", "https://arxiv.org/abs/2408.04682", "https://arxiv.org/abs/2504.08703", "https://arxiv.org/abs/2512.12730", "https://arxiv.org/abs/2605.12925", "https://arxiv.org/abs/2605.15846", "https://arxiv.org/abs/2607.06624", "https://arxiv.org/abs/2607.21217", "https://arxiv.org/abs/2610.16067", "https://arxiv.org/abs/1908.10084", "https://arxiv.org/abs/2004.04906", "https://arxiv.org/abs/2005.11401", "https://arxiv.org/abs/2112.01488", "https://arxiv.org/abs/2212.10496", "https://arxiv.org/abs/2305.06983"]
---

# LLM-as-a-Judge

Evaluating answers with models and examining the biases of those evaluators.

**Status:** This page groups papers by topic. An entry in the list indicates **a topical relationship**. It does not imply that every claim is confirmed or that one paper cites another.

## Papers on this topic (38)

- [A Benchmark for Evaluating Repository-Level Code Agents with Intermediate Reasoning on Feature Addition Task](../sources/arxiv-2603.26337.md) — The evaluation covers task analysis, file localization and decomposition of the work alongside the final code.
- [Active Retrieval Augmented Generation](../sources/arxiv-2305.06983.md) — FLARE investigates when to retrieve additional information during long-form generation.
- [AgentBench: Evaluating LLMs as Agents](../sources/arxiv-2308.03688.md) — The study compares agent reasoning and decisions across eight interactive environments and identifies recurring causes of failure.
- [AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](../sources/arxiv-2406.13352.md) — The environment tests agents' resilience to prompt injection in external content and tool outputs.
- [AgentLens: Production-Assessed Trajectory Reviews for Coding Agent Evaluation](../sources/arxiv-2607.06624.md) — The study evaluates the quality of a coding agent's execution trace alongside its final result.
- [AgentLens: Revealing The Lucky Pass Problem in SWE-Agent Evaluation](../sources/arxiv-2605.12925.md) — The study examines apparent successes where tests pass despite problems in the agent's execution trace.
- [ARES: An Automated Evaluation Framework for Retrieval-Augmented Generation Systems](../sources/arxiv-2311.09476.md) — The method combines synthetic data and trained judges with a small set of human judgments to measure RAG relevance and faithfulness.
- [Can Large Language Models Resolve Real Java Merge Conflicts? An Evaluation with a Calibrated LLM-as-Judge](../sources/arxiv-2607.27674.md) — The study evaluates models' ability to resolve real Git conflicts in Java projects and the reliability of the evaluation itself.
- [Chain-of-Verification Reduces Hallucination in Large Language Models](../sources/arxiv-2309.11495.md) — The model drafts an answer, devises verification questions and checks them independently before producing a final response.
- [ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction](../sources/arxiv-2112.01488.md) — The method combines multi-vector retrieval, late token interaction, representation compression and training with denoised supervision.
- [ColPali: Efficient Document Retrieval with Vision Language Models](../sources/arxiv-2407.01449.md) — The method retrieves visually complex documents using multi-vector embeddings of page images and evaluates retrieval on ViDoRe.
- [Corrective Retrieval Augmented Generation](../sources/arxiv-2401.15884.md) — CRAG assesses retrieved documents and takes corrective action when the retrieved evidence is of poor quality.
- [Dense Passage Retrieval for Open-Domain Question Answering](../sources/arxiv-2004.04906.md) — A dual encoder produces dense representations of questions and passages for retrieval over open-domain document collections.
- [Evaluating Very Long-Term Conversational Memory of LLM Agents](../sources/arxiv-2402.17753.md) — LoCoMo is a benchmark of multi-session conversations for evaluating memory and reasoning about events far apart in time.
- [Fact or Fiction: Verifying Scientific Claims](../sources/arxiv-2004.14974.md) — SciFact provides scientific claims and abstracts annotated for support, refutation and the passages that justify each label.
- [FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation](../sources/arxiv-2305.14251.md) — The method decomposes long answers into atomic facts and measures the proportion supported by a trusted source.
- [G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment](../sources/arxiv-2303.16634.md) — A judge model scores generated text against specified criteria. The study examines agreement with human judgments and potential bias.
- [ICAE-Bench: Evaluating Coding Agents as Interactive Project Builders](../sources/arxiv-2607.21217.md) — The study examines project development through interactions with a user who initially supplies incomplete requirements.
- [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](../sources/arxiv-2306.05685.md) — The study evaluates language models as judges of other models' responses, identifying position bias, verbosity bias and other limitations.
- [LightRAG: Simple and Fast Retrieval-Augmented Generation](../sources/arxiv-2410.05779.md) — The method combines a relationship graph and vector representations with two-level retrieval and incremental index updates.
- [Long-form factuality in large language models](../sources/arxiv-2403.18802.md) — LongFact and SAFE support evaluation of long answers by splitting them into facts and checking those facts against retrieved sources.
- [LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](../sources/arxiv-2410.10813.md) — The benchmark tests long-term memory, temporal reasoning, knowledge updates and appropriate abstention when information is missing.
- [NL2Repo-Bench: Towards Long-Horizon Repository Generation Evaluation of Coding Agents](../sources/arxiv-2512.12730.md) — The benchmark evaluates whether agents can generate complete repositories from natural-language requirements.
- [Precise Zero-Shot Dense Retrieval without Relevance Labels](../sources/arxiv-2212.10496.md) — HyDE generates a hypothetical document, embeds it and retrieves real documents without using relevance labels.
- [Prometheus 2: An Open Source Language Model Specialized in Evaluating Other Language Models](../sources/arxiv-2405.01535.md) — The authors present an open judge model for absolute scoring and pairwise comparisons using user-defined criteria.
- [Ragas: Automated Evaluation of Retrieval Augmented Generation](../sources/arxiv-2309.15217.md) — The authors define metrics for retrieval, faithfulness to context and generation quality that do not require exhaustive human annotation.
- [RAGBench: Explainable Benchmark for Retrieval-Augmented Generation Systems](../sources/arxiv-2407.11005.md) — The dataset provides cases and interpretable labels for assessing whether retrieved evidence supports an answer.
- [RAGChecker: A Fine-grained Framework for Diagnosing Retrieval-Augmented Generation](../sources/arxiv-2408.08067.md) — The authors propose metrics that distinguish context-retrieval errors from answer-generation errors.
- [RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval](../sources/arxiv-2401.18059.md) — The method builds a hierarchy of summaries and passages to support retrieval at multiple levels of detail.
- [RepoCoder: Repository-Level Code Completion Through Iterative Retrieval and Generation](../sources/arxiv-2303.12570.md) — The method iteratively retrieves related code and completes implementations across a repository.
- [Repoformer: Selective Retrieval for Repository-Level Code Completion](../sources/arxiv-2403.10059.md) — The method retrieves context selectively when it is expected to help code generation, reducing noise and unnecessary cost.
- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](../sources/arxiv-2005.11401.md) — The architecture combines a generative model with retrieval over external documents. The paper evaluates RAG-Sequence and RAG-Token.
- [Retrieval-Augmented Generation for Large Language Models: A Survey](../sources/arxiv-2312.10997.md) — The survey covers basic, advanced and modular RAG, including retrieval, augmentation, generation and evaluation.
- [RoadmapBench: Evaluating Long-Horizon Agentic Software Development Across Version Upgrades](../sources/arxiv-2605.15846.md) — The study examines complex repository changes implemented in stages across successive product releases.
- [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](../sources/arxiv-1908.10084.md) — BERT trained with a Siamese or triplet architecture produces sentence embeddings that can be compared by cosine similarity for semantic search.
- [SWE-PolyBench: A Multi-Language Benchmark for Repository-Level Evaluation of Coding Agents](../sources/arxiv-2504.08703.md) — The study compares coding agents on repository-level tasks in several programming languages.
- [ToolSandbox: A Stateful, Conversational, Interactive Evaluation Benchmark for LLM Tool Use Capabilities](../sources/arxiv-2408.04682.md) — The evaluation covers state-dependent tool use, interactions and intermediate steps in addition to the outcome of an individual command.
- [When Agent Evaluation Becomes Unreliable: An Empirical Study of Oracle Failures and Configuration-Dependent Measurement in an LLM Agent Benchmark](../sources/arxiv-2610.16067.md) — The study examines evaluator defects that can inflate or distort reported agent performance.

## Review questions

- How do the papers define the problem and the scope of their evaluation?
- Which conclusions have experimental support, and which are interpretations?
- When do these methods compete, and when do they complement each other?
- Which questions require consulting the full text?
