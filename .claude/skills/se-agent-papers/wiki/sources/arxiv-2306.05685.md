---
type: source
title: "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena"
created: 2026-11-19
arxiv_id: "2306.05685"
url: "https://arxiv.org/abs/2306.05685"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["evaluation-metrics", "llm-as-judge", "benchmarks"]
source_path: "raw/papers/2306.05685.md"
sources: ["https://arxiv.org/abs/2306.05685"]
ingested: "2026-11-19"
---

# Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena

**Paper:** [2306.05685](https://arxiv.org/abs/2306.05685) · [PDF](https://arxiv.org/pdf/2306.05685) · [HTML](https://arxiv.org/html/2306.05685)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** The study compares GPT-4 judgments with expert preferences on 80 two-turn MT-Bench questions and with Chatbot Arena user votes. Tables 5–6 report results both with ties and after excluding them. [PDF, p. 3](https://arxiv.org/pdf/2306.05685v4#page=3) [PDF, p. 4](https://arxiv.org/pdf/2306.05685v4#page=4) [PDF, p. 7](https://arxiv.org/pdf/2306.05685v4#page=7) [PDF, p. 8](https://arxiv.org/pdf/2306.05685v4#page=8)

**Key result.** GPT-4's pairwise judgments agreed with humans on 85% of first-turn MT-Bench comparisons when ties were excluded and on 66% when ties were included. The corresponding Arena figures were 87% and 64%. [PDF, p. 8](https://arxiv.org/pdf/2306.05685v4#page=8)

**Limitations and scope.** Excluding ties changes the number and difficulty of comparisons. Presentation order, answer length and judge reasoning errors can affect results, including on simple mathematics problems. [PDF, p. 5](https://arxiv.org/pdf/2306.05685v4#page=5) [PDF, p. 6](https://arxiv.org/pdf/2306.05685v4#page=6) [PDF, p. 8](https://arxiv.org/pdf/2306.05685v4#page=8)

[Audit of sections, tables and appendices](../reviews/audit-2026-11-19/2306.05685v4.md)

## Overview

The study evaluates language models as judges of other models' responses, identifying position bias, verbosity bias and other limitations. [PDF, p. 1](https://arxiv.org/pdf/2306.05685v4#page=1)

## Source files

arXiv version `2306.05685v4` · PDF pages: 29.

- [Original PDF](https://arxiv.org/pdf/2306.05685v4)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2306.05685.metadata.json)

PDF bookmarks — [Agreement Evaluation (p. 7)](https://arxiv.org/pdf/2306.05685v4#page=7).

## Related concepts

- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [LLM-as-a-Judge](../concepts/llm-as-judge.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
