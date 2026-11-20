---
type: source
title: "Tangent: An Empirical Study of Testing Practices for LLM-Based Agent Applications"
created: 2026-11-19
arxiv_id: "2608.08413"
url: "https://arxiv.org/abs/2608.08413"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "benchmarks", "unit-testing", "evaluation-metrics"]
source_path: "raw/papers/2608.08413.md"
sources: ["https://arxiv.org/abs/2608.08413"]
ingested: "2026-11-19"
---

# Tangent: An Empirical Study of Testing Practices for LLM-Based Agent Applications

**Paper:** [2608.08413](https://arxiv.org/abs/2608.08413) · [PDF](https://arxiv.org/pdf/2608.08413) · [HTML](https://arxiv.org/html/2608.08413)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** After multi-stage screening, two authors labeled 2,572 test methods from 240 modules in 12 Python projects. A separate part of the study involved interviews with ten IBM practitioners. [PDF, p. 3](https://arxiv.org/pdf/2608.08413v1#page=3) [PDF, p. 9](https://arxiv.org/pdf/2608.08413v1#page=9)

**Key result.** In the manually labeled sample, 61.8% of test methods tested an individual agent or tool and 34.6% tested interactions. Nonfunctional requirements accounted for 7.5% of methods. The counts in Table 2 yield state assertions in 1,317/2,572 methods (51.21%) and reasoning assertions in 225/2,572 (8.75%). [PDF, p. 5](https://arxiv.org/pdf/2608.08413v1#page=5) [PDF, p. 7](https://arxiv.org/pdf/2608.08413v1#page=7)

**Limitations and scope.** The code analysis covers selected public Python projects. Associations between test types and frameworks may also reflect project characteristics. Interviews at one organization provide a separate source of context. [PDF, p. 9](https://arxiv.org/pdf/2608.08413v1#page=9) [PDF, p. 11](https://arxiv.org/pdf/2608.08413v1#page=11)

[Audit of sections, tables and appendices](../reviews/audit-2026-11-19/2608.08413v1.md)

## Overview

The study examines how developers test agent-based applications, including their use of mocks and integration tests. [PDF, p. 1](https://arxiv.org/pdf/2608.08413v1#page=1)

## Source files

arXiv version `2608.08413v1` · PDF pages: 14.

- [Original PDF](https://arxiv.org/pdf/2608.08413v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2608.08413.metadata.json)

PDF bookmarks — [8 Threats to Validity (p. 11)](https://arxiv.org/pdf/2608.08413v1#page=11).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Unit tests](../concepts/unit-testing.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
