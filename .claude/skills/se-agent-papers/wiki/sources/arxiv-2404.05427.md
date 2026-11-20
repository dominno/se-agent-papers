---
type: source
title: "AutoCodeRover: Autonomous Program Improvement"
created: 2026-11-19
arxiv_id: "2404.05427"
url: "https://arxiv.org/abs/2404.05427"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["coding-agents", "debugging"]
source_path: "raw/papers/2404.05427.md"
sources: ["https://arxiv.org/abs/2404.05427"]
ingested: "2026-11-19"
---

# AutoCodeRover: Autonomous Program Improvement

**Paper:** [2404.05427](https://arxiv.org/abs/2404.05427) · [PDF](https://arxiv.org/pdf/2404.05427) · [HTML](https://arxiv.org/html/2404.05427)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** AutoCodeRover searches for classes, methods and code snippets, iteratively narrows the context for GPT-4, and generates a patch. A separate variant uses the full test suite and execution-based fault localization to identify suspicious methods. [PDF, p. 5](https://arxiv.org/pdf/2404.05427v3#page=5) [PDF, p. 6](https://arxiv.org/pdf/2404.05427v3#page=6) [PDF, p. 7](https://arxiv.org/pdf/2404.05427v3#page=7) [PDF, p. 9](https://arxiv.org/pdf/2404.05427v3#page=9)

**Key result.** On SWE-bench Lite, Table 2 reports 57/300 tasks passing with one attempt and 78/300 with three, compared with 54/300 for SWE-agent. The authors judged 51 of the 78 passing patches semantically correct (65.4%). [PDF, p. 8](https://arxiv.org/pdf/2404.05427v3#page=8) [PDF, p. 9](https://arxiv.org/pdf/2404.05427v3#page=9)

**Limitations and scope.** Passing the tests does not establish equivalence to the developer's patch. The pass@3 row for full SWE-bench in Table 2 also gives inconsistent values, 17.96% and 422/2,294 (18.40%). [PDF, p. 8](https://arxiv.org/pdf/2404.05427v3#page=8) [PDF, p. 9](https://arxiv.org/pdf/2404.05427v3#page=9) [PDF, p. 11](https://arxiv.org/pdf/2404.05427v3#page=11)

## Overview

The method combines structured code search with program analysis to localize faults and generate patches. [PDF, p. 1](https://arxiv.org/pdf/2404.05427v3#page=1)

[Section and evidence audit](../reviews/audit-2026-11-19/2404.05427v3.md)

## Source files

**Paper license notice.** The arXiv record lists CC BY 4.0. The first page also carries an ACM notice on personal and classroom copying and other uses. [PDF, p. 1](https://arxiv.org/pdf/2404.05427v3#page=1)

arXiv version `2404.05427v3` · PDF pages: 13.

- [Original PDF](https://arxiv.org/pdf/2404.05427v3)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2404.05427.metadata.json)

PDF bookmarks — [4 AI Program Improvement Framework (p. 4)](https://arxiv.org/pdf/2404.05427v3#page=4) · [5 Experiment Setup (p. 7)](https://arxiv.org/pdf/2404.05427v3#page=7) · [8 Threats to Validity (p. 11)](https://arxiv.org/pdf/2404.05427v3#page=11).

## Related concepts

- [Coding agents](../concepts/coding-agents.md)
- [Debugging](../concepts/debugging.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
