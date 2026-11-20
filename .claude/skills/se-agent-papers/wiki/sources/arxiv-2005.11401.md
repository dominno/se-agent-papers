---
type: source
title: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
created: 2026-11-19
arxiv_id: "2005.11401"
url: "https://arxiv.org/abs/2005.11401"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["retrieval-augmented-generation", "knowledge-graph", "entity-extraction", "grounded-generation", "rag-evaluation", "llm-as-judge"]
source_path: "raw/papers/2005.11401.md"
sources: ["https://arxiv.org/abs/2005.11401"]
ingested: "2026-11-19"
---

# Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

**Paper:** [2005.11401](https://arxiv.org/abs/2005.11401) · [PDF](https://arxiv.org/pdf/2005.11401) · [HTML](https://arxiv.org/html/2005.11401)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** DPR selects Wikipedia passages. BART marginalizes over them for the whole response in RAG-Sequence or at each token position in RAG-Token. The query encoder and generator are trained with a fixed index. [PDF, p. 2](https://arxiv.org/pdf/2005.11401v4#page=2) [PDF, p. 3](https://arxiv.org/pdf/2005.11401v4#page=3) [PDF, p. 4](https://arxiv.org/pdf/2005.11401v4#page=4)

**Key result.** In factuality ratings of 452 pairs of Jeopardy clues, raters preferred RAG-Token to BART in 42.7% of cases and BART to RAG-Token in 7.1%. Table 4 reports 11.7% in a separate “both good” category. [PDF, p. 6](https://arxiv.org/pdf/2005.11401v4#page=6) [PDF, p. 8](https://arxiv.org/pdf/2005.11401v4#page=8)

**Limitations and scope.** Preliminary story-generation experiments found retrieval collapse to a fixed set of documents and results comparable to BART. The Wikipedia index inherits errors and biases from its sources. [PDF, p. 10](https://arxiv.org/pdf/2005.11401v4#page=10) [PDF, p. 19](https://arxiv.org/pdf/2005.11401v4#page=19)

[Section and table audit for 2005.11401v4](../reviews/audit-2026-11-19/2005.11401v4.md)

## Overview

The architecture combines a generative model with retrieval over external documents. The paper evaluates RAG-Sequence and RAG-Token. [PDF, p. 1](https://arxiv.org/pdf/2005.11401v4#page=1)

## Source files

arXiv version `2005.11401v4` · PDF pages: 19.

- [Original PDF](https://arxiv.org/pdf/2005.11401v4)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2005.11401.metadata.json)

PDF bookmarks — [2 Methods (p. 2)](https://arxiv.org/pdf/2005.11401v4#page=2) · [3 Experiments (p. 4)](https://arxiv.org/pdf/2005.11401v4#page=4).

## Related concepts

- [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md)
- [Knowledge graph](../concepts/knowledge-graph.md)
- [Entity extraction](../concepts/entity-extraction.md)
- [Source-grounded generation](../concepts/grounded-generation.md)
- [RAG evaluation](../concepts/rag-evaluation.md)
- [LLM-as-a-Judge](../concepts/llm-as-judge.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
