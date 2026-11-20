---
type: source
title: "Enabling Large Language Models to Generate Text with Citations"
created: 2026-11-19
arxiv_id: "2305.14627"
url: "https://arxiv.org/abs/2305.14627"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["citation-grounding", "citation-precision", "citation-recall", "grounded-generation"]
source_path: "raw/papers/2305.14627.md"
sources: ["https://arxiv.org/abs/2305.14627"]
ingested: "2026-11-19"
---

# Enabling Large Language Models to Generate Text with Citations

**Paper:** [2305.14627](https://arxiv.org/abs/2305.14627) · [PDF](https://arxiv.org/pdf/2305.14627) · [HTML](https://arxiv.org/html/2305.14627)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** ALCE distinguishes fluency, answer correctness and citation quality. An entailment model checks whether the cited passages jointly support a claim and separately assesses the contribution of each citation. [PDF, p. 3](https://arxiv.org/pdf/2305.14627v2#page=3) [PDF, p. 4](https://arxiv.org/pdf/2305.14627v2#page=4) [PDF, p. 5](https://arxiv.org/pdf/2305.14627v2#page=5)

**Key result.** On ELI5, ChatGPT using five passages achieved 51.1% citation completeness. Selecting among four answers raised this to 69.3%. Coverage of reference claims was 12.0% and 11.4%, respectively. [PDF, p. 6](https://arxiv.org/pdf/2305.14627v2#page=6) [PDF, p. 7](https://arxiv.org/pdf/2305.14627v2#page=7) [PDF, p. 20](https://arxiv.org/pdf/2305.14627v2#page=20)

**Limitations and scope.** Automated evaluation may miss partial justifications and correct answers outside the reference. Against human labels, accuracy for judgments of completeness was 85.1%, and accuracy for judgments of citation precision was 77.6%. The ChatGPT variant that selects one of four answers was evaluated in a single series of runs. [PDF, p. 10](https://arxiv.org/pdf/2305.14627v2#page=10) [PDF, p. 15](https://arxiv.org/pdf/2305.14627v2#page=15) [PDF, p. 17](https://arxiv.org/pdf/2305.14627v2#page=17)

## Overview

ALCE evaluates the correctness, quality and completeness of citations in model-generated answers. [PDF, p. 1](https://arxiv.org/pdf/2305.14627v2#page=1)

## Section notes

**Mechanism:** ALCE evaluates answer correctness separately from attribution. It measures citation precision and citation recall by checking whether the cited material supports the response. [PDF, p. 3](https://arxiv.org/pdf/2305.14627v2#page=3) · [PDF, p. 4](https://arxiv.org/pdf/2305.14627v2#page=4)

**Evaluation and study settings:** The study compares retrieval followed by synthesis, post-editing and human evaluation for long-form answers with citations. [PDF, p. 2](https://arxiv.org/pdf/2305.14627v2#page=2) · [PDF, p. 7](https://arxiv.org/pdf/2305.14627v2#page=7)

**Scope and interpretation:** A link or citation alone does not establish support. Automated metrics require calibration against human judgments for the task at hand. [PDF, p. 10](https://arxiv.org/pdf/2305.14627v2#page=10)

**Sections checked:** 3 Automatic Evaluation, 4 Modeling, 5 Experiments, 6 Human Evaluation. [Read the paper](https://arxiv.org/html/2305.14627).


[Section and evidence audit](../reviews/audit-2026-11-19/2305.14627v2.md)

## Source files

arXiv version `2305.14627v2` · PDF pages: 24.

- [Original PDF](https://arxiv.org/pdf/2305.14627v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2305.14627.metadata.json)

## Related concepts

- [Citations and supporting evidence](../concepts/citation-grounding.md)
- [Citation precision](../concepts/citation-precision.md)
- [Citation completeness](../concepts/citation-recall.md)
- [Source-grounded generation](../concepts/grounded-generation.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.

## Findings and caveats

- [Finding 1 — method](../concepts/finding-2305-14627-1.md)
- [Finding 2 — evaluation](../concepts/finding-2305-14627-2.md)
- [Finding 3 — interpretive caveat](../concepts/finding-2305-14627-3.md)
