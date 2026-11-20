---
type: source
title: "Active Retrieval Augmented Generation"
created: 2026-11-19
arxiv_id: "2305.06983"
url: "https://arxiv.org/abs/2305.06983"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["retrieval-augmented-generation", "selective-retrieval", "knowledge-graph", "entity-extraction", "grounded-generation", "rag-evaluation", "llm-as-judge"]
source_path: "raw/papers/2305.06983.md"
sources: ["https://arxiv.org/abs/2305.06983"]
ingested: "2026-11-19"
---

# Active Retrieval Augmented Generation

**Paper:** [2305.06983](https://arxiv.org/abs/2305.06983) · [PDF](https://arxiv.org/pdf/2305.06983) · [HTML](https://arxiv.org/html/2305.06983)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** FLARE-direct predicts the next sentence, identifies low-probability tokens, retrieves information and regenerates the sentence. A separate FLARE-instruct variant uses an explicit retrieval request. [PDF, p. 3](https://arxiv.org/pdf/2305.06983v2#page=3) [PDF, p. 4](https://arxiv.org/pdf/2305.06983v2#page=4)

**Key result.** On 500 questions from 2WikiMultihopQA, FLARE-direct scored 51.0 exact match, compared with 47.8 for question decomposition and 39.4 for one-time retrieval. FLARE-instruct scored 42.4. [PDF, p. 7](https://arxiv.org/pdf/2305.06983v2#page=7) [PDF, p. 16](https://arxiv.org/pdf/2305.06983v2#page=16)

**Limitations and scope.** The authors found no significant gain on Wizard of Wikipedia or ELI5. Across the tested masking thresholds, exact match on 2Wiki ranged from 48.8 to 51.0. [PDF, p. 9](https://arxiv.org/pdf/2305.06983v2#page=9)

[Section and table audit for 2305.06983v2](../reviews/audit-2026-11-19/2305.06983v2.md)

## Overview

FLARE investigates when to retrieve additional information during long-form generation. [PDF, p. 1](https://arxiv.org/pdf/2305.06983v2#page=1)

## Source files

arXiv version `2305.06983v2` · PDF pages: 24.

- [Original PDF](https://arxiv.org/pdf/2305.06983v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2305.06983.metadata.json)

## Related concepts

- [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md)
- [Selective retrieval](../concepts/selective-retrieval.md)
- [Knowledge graph](../concepts/knowledge-graph.md)
- [Entity extraction](../concepts/entity-extraction.md)
- [Source-grounded generation](../concepts/grounded-generation.md)
- [RAG evaluation](../concepts/rag-evaluation.md)
- [LLM-as-a-Judge](../concepts/llm-as-judge.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
