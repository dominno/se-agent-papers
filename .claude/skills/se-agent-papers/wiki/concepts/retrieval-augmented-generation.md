---
type: concept
title: "Retrieval-Augmented Generation (RAG)"
created: 2026-11-19
tags: ["retrieval-augmented-generation", "research"]
sources: ["https://arxiv.org/abs/1908.10084", "https://arxiv.org/abs/2004.04906", "https://arxiv.org/abs/2005.11401", "https://arxiv.org/abs/2112.01488", "https://arxiv.org/abs/2212.10496", "https://arxiv.org/abs/2305.06983", "https://arxiv.org/abs/2312.10997", "https://arxiv.org/abs/2401.15884", "https://arxiv.org/abs/2407.01449", "https://arxiv.org/abs/2207.05987", "https://arxiv.org/abs/2303.12570", "https://arxiv.org/abs/2403.10059", "https://arxiv.org/abs/2309.15217", "https://arxiv.org/abs/2311.09476", "https://arxiv.org/abs/2407.11005"]
---

# Retrieval-Augmented Generation (RAG)

Combining a language model with information retrieved from indexed sources.

**Status:** This page groups papers by topic. An entry in the list indicates **a topical relationship**. It does not imply that every claim is confirmed or that one paper cites another.

## Papers on this topic (26)

- [Active Retrieval Augmented Generation](../sources/arxiv-2305.06983.md) — FLARE investigates when to retrieve additional information during long-form generation.
- [ARES: An Automated Evaluation Framework for Retrieval-Augmented Generation Systems](../sources/arxiv-2311.09476.md) — The method combines synthetic data and trained judges with a small set of human judgments to measure RAG relevance and faithfulness.
- [ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction](../sources/arxiv-2112.01488.md) — The method combines multi-vector retrieval, late token interaction, representation compression and training with denoised supervision.
- [ColPali: Efficient Document Retrieval with Vision Language Models](../sources/arxiv-2407.01449.md) — The method retrieves visually complex documents using multi-vector embeddings of page images and evaluates retrieval on ViDoRe.
- [Corrective Retrieval Augmented Generation](../sources/arxiv-2401.15884.md) — CRAG assesses retrieved documents and takes corrective action when the retrieved evidence is of poor quality.
- [CRAG -- Comprehensive RAG Benchmark](../sources/arxiv-2406.04744.md) — The benchmark provides diverse questions, answers and simulated APIs for evaluating factual accuracy in RAG systems.
- [Dense Passage Retrieval for Open-Domain Question Answering](../sources/arxiv-2004.04906.md) — A dual encoder produces dense representations of questions and passages for retrieval over open-domain document collections.
- [DocPrompting: Generating Code by Retrieving the Docs](../sources/arxiv-2207.05987.md) — The study demonstrates code generation using retrieved library and API documentation, including APIs previously unseen by the model.
- [Evaluating Very Long-Term Conversational Memory of LLM Agents](../sources/arxiv-2402.17753.md) — LoCoMo is a benchmark of multi-session conversations for evaluating memory and reasoning about events far apart in time.
- [From Local to Global: A Graph RAG Approach to Query-Focused Summarization](../sources/arxiv-2404.16130.md) — The method builds an entity graph and summarizes graph communities to answer questions that span a large text collection.
- [HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models](../sources/arxiv-2405.14831.md) — Knowledge graphs and Personalized PageRank support associations between facts and multi-hop retrieval.
- [LightRAG: Simple and Fast Retrieval-Augmented Generation](../sources/arxiv-2410.05779.md) — The method combines a relationship graph and vector representations with two-level retrieval and incremental index updates.
- [LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](../sources/arxiv-2410.10813.md) — The benchmark tests long-term memory, temporal reasoning, knowledge updates and appropriate abstention when information is missing.
- [Lost in the Middle: How Language Models Use Long Contexts](../sources/arxiv-2307.03172.md) — The authors find that models can make less effective use of information placed in the middle of a long context.
- [MemGPT: Towards LLMs as Operating Systems](../sources/arxiv-2310.08560.md) — The method manages memory hierarchically and moves information between memory levels when the context window is limited.
- [Precise Zero-Shot Dense Retrieval without Relevance Labels](../sources/arxiv-2212.10496.md) — HyDE generates a hypothetical document, embeds it and retrieves real documents without using relevance labels.
- [Ragas: Automated Evaluation of Retrieval Augmented Generation](../sources/arxiv-2309.15217.md) — The authors define metrics for retrieval, faithfulness to context and generation quality that do not require exhaustive human annotation.
- [RAGBench: Explainable Benchmark for Retrieval-Augmented Generation Systems](../sources/arxiv-2407.11005.md) — The dataset provides cases and interpretable labels for assessing whether retrieved evidence supports an answer.
- [RAGChecker: A Fine-grained Framework for Diagnosing Retrieval-Augmented Generation](../sources/arxiv-2408.08067.md) — The authors propose metrics that distinguish context-retrieval errors from answer-generation errors.
- [RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval](../sources/arxiv-2401.18059.md) — The method builds a hierarchy of summaries and passages to support retrieval at multiple levels of detail.
- [RepoCoder: Repository-Level Code Completion Through Iterative Retrieval and Generation](../sources/arxiv-2303.12570.md) — The method iteratively retrieves related code and completes implementations across a repository.
- [Repoformer: Selective Retrieval for Repository-Level Code Completion](../sources/arxiv-2403.10059.md) — The method retrieves context selectively when it is expected to help code generation, reducing noise and unnecessary cost.
- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](../sources/arxiv-2005.11401.md) — The architecture combines a generative model with retrieval over external documents. The paper evaluates RAG-Sequence and RAG-Token.
- [Retrieval-Augmented Generation for Large Language Models: A Survey](../sources/arxiv-2312.10997.md) — The survey covers basic, advanced and modular RAG, including retrieval, augmentation, generation and evaluation.
- [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](../sources/arxiv-2310.11511.md) — The method trains a model to retrieve evidence adaptively and evaluate its own responses using reflection tokens.
- [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](../sources/arxiv-1908.10084.md) — BERT trained with a Siamese or triplet architecture produces sentence embeddings that can be compared by cosine similarity for semantic search.

## Review questions

- How do the papers define the problem and the scope of their evaluation?
- Which conclusions have experimental support, and which are interpretations?
- When do these methods compete, and when do they complement each other?
- Which questions require consulting the full text?
