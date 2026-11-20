---
type: source
title: "LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory"
created: 2026-11-19
arxiv_id: "2410.10813"
url: "https://arxiv.org/abs/2410.10813"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["long-term-memory", "memory-evaluation", "temporal-reasoning", "retrieval-augmented-generation", "grounded-generation", "evaluation-metrics", "llm-as-judge", "benchmarks", "comparison-and-reproducibility"]
source_path: "raw/papers/2410.10813.md"
sources: ["https://arxiv.org/abs/2410.10813"]
ingested: "2026-11-19"
---

# LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory

**Paper:** [2410.10813](https://arxiv.org/abs/2410.10813) · [PDF](https://arxiv.org/pdf/2410.10813) · [HTML](https://arxiv.org/html/2410.10813)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** LongMemEval contains 500 questions over multi-session histories and distinguishes five memory abilities. The authors analyze architectures in terms of indexing, retrieval and reading. [PDF, p. 3](https://arxiv.org/pdf/2410.10813v2#page=3) [PDF, p. 4](https://arxiv.org/pdf/2410.10813v2#page=4) [PDF, p. 7](https://arxiv.org/pdf/2410.10813v2#page=7)

**Key result.** Without Chain-of-Note, GPT-4o scored 87.0% with oracle retrieval and 60.6% on full S histories, a drop of 26.4 percentage points or 30.3% relative to the oracle score. [PDF, p. 6](https://arxiv.org/pdf/2410.10813v2#page=6)

**Limitations and scope.** The comparison with the oracle also reflects the difficulty of reading long, noisy context. Commercial services were evaluated on a separate sample of 97 questions with shorter histories of three to six sessions. [PDF, p. 6](https://arxiv.org/pdf/2410.10813v2#page=6) [PDF, p. 21](https://arxiv.org/pdf/2410.10813v2#page=21) [PDF, p. 28](https://arxiv.org/pdf/2410.10813v2#page=28)

[Section and table audit for 2410.10813v2](../reviews/audit-2026-11-19/2410.10813v2.md)

## Overview

The benchmark tests long-term memory, temporal reasoning, knowledge updates and appropriate abstention when information is missing. [PDF, p. 1](https://arxiv.org/pdf/2410.10813v2#page=1)

## Section notes

**Mechanism:** LongMemEval distinguishes memory, temporal reasoning, knowledge updates and abstention when facts are missing. Its memory-system model separates the value, key, query and reading strategy. [PDF, p. 4](https://arxiv.org/pdf/2410.10813v2#page=4) · [PDF, p. 7](https://arxiv.org/pdf/2410.10813v2#page=7)

**Evaluation and study settings:** The study evaluated memory over long conversation histories, comparing fact indexing, multiple keys, time-aware query expansion and reading strategies. [PDF, p. 7](https://arxiv.org/pdf/2410.10813v2#page=7) · [PDF, p. 9](https://arxiv.org/pdf/2410.10813v2#page=9)

**Scope and interpretation:** The evaluation uses simulated or collected long conversation histories. Performance depends on the model and indexing method. [PDF, p. 4](https://arxiv.org/pdf/2410.10813v2#page=4) · [PDF, p. 6](https://arxiv.org/pdf/2410.10813v2#page=6)

**Sections checked:** 3 LongMemEval, 4 A Unified View, 5 Experiment Results. [Read the paper](https://arxiv.org/html/2410.10813).


## Source files

arXiv version `2410.10813v2` · PDF pages: 28.

- [Original PDF](https://arxiv.org/pdf/2410.10813v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2410.10813.metadata.json)

PDF bookmarks — [Experiment Results (p. 8)](https://arxiv.org/pdf/2410.10813v2#page=8).

## Related concepts

- [Long-term memory](../concepts/long-term-memory.md)
- [Memory evaluation](../concepts/memory-evaluation.md)
- [Temporal reasoning](../concepts/temporal-reasoning.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md)
- [Source-grounded generation](../concepts/grounded-generation.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [LLM-as-a-Judge](../concepts/llm-as-judge.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.

## Findings and caveats

- [Finding 1 — method](../concepts/finding-2410-10813-1.md)
- [Finding 2 — evaluation](../concepts/finding-2410-10813-2.md)
- [Finding 3 — interpretive caveat](../concepts/finding-2410-10813-3.md)
