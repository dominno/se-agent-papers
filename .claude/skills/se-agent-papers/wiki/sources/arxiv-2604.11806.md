---
type: source
title: "Detecting Safety Violations Across Many Agent Traces"
created: 2026-11-19
arxiv_id: "2604.11806"
url: "https://arxiv.org/abs/2604.11806"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "observability", "tool-sandboxing"]
source_path: "raw/papers/2604.11806.md"
sources: ["https://arxiv.org/abs/2604.11806"]
ingested: "2026-11-19"
---

# Detecting Safety Violations Across Many Agent Traces

**Paper:** [2604.11806](https://arxiv.org/abs/2604.11806) · [PDF](https://arxiv.org/pdf/2604.11806) · [HTML](https://arxiv.org/html/2604.11806)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** The auditor searches groups of trajectories for evidence of a violation of a specified property. Detection is evaluated separately on annotated cases and on corpora without complete labels. [PDF, p. 3](https://arxiv.org/pdf/2604.11806v1#page=3) [PDF, p. 4](https://arxiv.org/pdf/2604.11806v1#page=4)

**Key result.** The CyBench audit confirmed violations in 16 of 464 passing runs (3.45%), spanning 13 tasks and four models. An earlier comparison reported four cases in a different dataset with two models. [PDF, p. 8](https://arxiv.org/pdf/2604.11806v1#page=8) [PDF, p. 29](https://arxiv.org/pdf/2604.11806v1#page=29)

**Limitations and scope.** The counts have different denominators, so their comparison cannot establish a fourfold change in incidence. The audit identifies violations from recorded traces. [PDF, p. 8](https://arxiv.org/pdf/2604.11806v1#page=8) [PDF, p. 17](https://arxiv.org/pdf/2604.11806v1#page=17) [PDF, p. 29](https://arxiv.org/pdf/2604.11806v1#page=29)

[Audit report for 2604.11806v1](../reviews/audit-2026-11-19/2604.11806v1.md)

## Overview

The study evaluates detection of rare safety violations across collections of agent execution traces. [PDF, p. 1](https://arxiv.org/pdf/2604.11806v1#page=1)

## Source files

arXiv version `2604.11806v1` · PDF pages: 35.

- [Original PDF](https://arxiv.org/pdf/2604.11806v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2604.11806.metadata.json)

PDF bookmarks — [Experiments (p. 4)](https://arxiv.org/pdf/2604.11806v1#page=4).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Agent observability](../concepts/observability.md)
- [Tool sandbox](../concepts/tool-sandboxing.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
