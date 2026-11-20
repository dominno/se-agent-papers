---
type: source
title: "DocPrompting: Generating Code by Retrieving the Docs"
created: 2026-11-19
arxiv_id: "2207.05987"
url: "https://arxiv.org/abs/2207.05987"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["coding-agents", "prompt-optimization", "retrieval-augmented-generation", "rag-evaluation", "benchmarks", "stateful-tool-use", "tool-evaluation", "unit-testing", "evaluation-metrics"]
source_path: "raw/papers/2207.05987.md"
sources: ["https://arxiv.org/abs/2207.05987"]
ingested: "2026-11-19"
---

# DocPrompting: Generating Code by Retrieving the Docs

**Paper:** [2207.05987](https://arxiv.org/abs/2207.05987) · [PDF](https://arxiv.org/pdf/2207.05987) · [HTML](https://arxiv.org/html/2207.05987)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** DocPrompting selects documentation from the task description and passes it to the generator. The tldr split separates command names between training and test, while CoNaLa holds out a subset of functions. [PDF, p. 3](https://arxiv.org/pdf/2207.05987v3#page=3) [PDF, p. 4](https://arxiv.org/pdf/2207.05987v3#page=4) [PDF, p. 5](https://arxiv.org/pdf/2207.05987v3#page=5)

**Key result.** On 100 CoNaLa tasks, CodeT5 pass@1 rose from 5.41% to 8.26% (+2.85 percentage points). Table 1 gives T5 a 6.49-point charBLEU gain on tldr, although the text reports more than 16. [PDF, p. 5](https://arxiv.org/pdf/2207.05987v3#page=5) [PDF, p. 6](https://arxiv.org/pdf/2207.05987v3#page=6) [PDF, p. 7](https://arxiv.org/pdf/2207.05987v3#page=7)

**Limitations and scope.** Execution tests covered 100 of 543 CoNaLa tasks. The best temperature was selected separately for each k and model. On tldr in Appendix H, code-davinci-002 with documentation achieved lower exact match. [PDF, p. 5](https://arxiv.org/pdf/2207.05987v3#page=5) [PDF, p. 14](https://arxiv.org/pdf/2207.05987v3#page=14) [PDF, p. 15](https://arxiv.org/pdf/2207.05987v3#page=15) [PDF, p. 18](https://arxiv.org/pdf/2207.05987v3#page=18)

[Audit of sections, tables and appendices](../reviews/audit-2026-11-19/2207.05987v3.md)

## Overview

The study demonstrates code generation using retrieved library and API documentation, including APIs previously unseen by the model. [PDF, p. 1](https://arxiv.org/pdf/2207.05987v3#page=1)

## Source files

arXiv version `2207.05987v3` · PDF pages: 19.

- [Original PDF](https://arxiv.org/pdf/2207.05987v3)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2207.05987.metadata.json)

PDF bookmarks — [5 Results (p. 5)](https://arxiv.org/pdf/2207.05987v3#page=5).

## Related concepts

- [Coding agents](../concepts/coding-agents.md)
- [Prompt optimization](../concepts/prompt-optimization.md)
- [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md)
- [RAG evaluation](../concepts/rag-evaluation.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Stateful tool use](../concepts/stateful-tool-use.md)
- [Tool evaluation](../concepts/tool-evaluation.md)
- [Unit tests](../concepts/unit-testing.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
