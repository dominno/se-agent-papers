---
type: source
title: "TextGrad: Automatic \"Differentiation\" via Text"
created: 2026-11-19
arxiv_id: "2406.07496"
url: "https://arxiv.org/abs/2406.07496"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["prompt-optimization", "workflow-optimization"]
source_path: "raw/papers/2406.07496.md"
sources: ["https://arxiv.org/abs/2406.07496"]
ingested: "2026-11-19"
---

# TextGrad: Automatic "Differentiation" via Text

**Paper:** [2406.07496](https://arxiv.org/abs/2406.07496) · [PDF](https://arxiv.org/pdf/2406.07496) · [HTML](https://arxiv.org/html/2406.07496)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** TextGrad propagates textual feedback backward through a computation graph and proposes changes to its components. The authors separately evaluate optimizing an individual answer at inference time and learning a reusable instruction. [PDF, p. 4](https://arxiv.org/pdf/2406.07496v1#page=4) [PDF, p. 5](https://arxiv.org/pdf/2406.07496v1#page=5) [PDF, p. 6](https://arxiv.org/pdf/2406.07496v1#page=6) [PDF, p. 9](https://arxiv.org/pdf/2406.07496v1#page=9) [PDF, p. 10](https://arxiv.org/pdf/2406.07496v1#page=10)

**Key result.** On 198 GPQA Diamond questions, TextGrad with GPT-4o reached 55.0%, compared with 51.0% for zero-shot CoT. On 39 LeetCode Hard tasks, the mean full-pass rate was 36%, compared with 31% for Reflexion. [PDF, p. 8](https://arxiv.org/pdf/2406.07496v1#page=8) [PDF, p. 10](https://arxiv.org/pdf/2406.07496v1#page=10) [PDF, p. 31](https://arxiv.org/pdf/2406.07496v1#page=31) [PDF, p. 32](https://arxiv.org/pdf/2406.07496v1#page=32)

**Limitations and scope.** Answer optimization requires additional iterations. The LeetCode data were retrieved again and may differ from the dataset in the earlier Reflexion paper. In prompt experiments, results matched DSPy on two of the three datasets. [PDF, p. 8](https://arxiv.org/pdf/2406.07496v1#page=8) [PDF, p. 9](https://arxiv.org/pdf/2406.07496v1#page=9) [PDF, p. 11](https://arxiv.org/pdf/2406.07496v1#page=11) [PDF, p. 31](https://arxiv.org/pdf/2406.07496v1#page=31)

## Overview

The method uses textual feedback to iteratively improve components of complex AI systems. [PDF, p. 1](https://arxiv.org/pdf/2406.07496v1#page=1)

[Section and evidence audit](../reviews/audit-2026-11-19/2406.07496v1.md)

## Source files

arXiv version `2406.07496v1` · PDF pages: 41.

- [Original PDF](https://arxiv.org/pdf/2406.07496v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2406.07496.metadata.json)

MuPDF reported a color-space problem in some figures while reading the PDF. The text extraction includes every page.

PDF bookmarks — [Results (p. 7)](https://arxiv.org/pdf/2406.07496v1#page=7).

## Related concepts

- [Prompt optimization](../concepts/prompt-optimization.md)
- [Workflow optimization](../concepts/workflow-optimization.md)

## Provenance and review

- This entry was added from the expanded catalog or from metadata verified against arXiv.
