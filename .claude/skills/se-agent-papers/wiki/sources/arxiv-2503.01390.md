---
type: source
title: "Scalable and Accurate Application-Level Crash-Consistency Testing via Representative Testing"
created: 2026-11-19
arxiv_id: "2503.01390"
url: "https://arxiv.org/abs/2503.01390"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["benchmarks", "unit-testing", "fault-recovery", "file-system-durability"]
source_path: "raw/papers/2503.01390.md"
sources: ["https://arxiv.org/abs/2503.01390"]
ingested: "2026-11-19"
---

# Scalable and Accurate Application-Level Crash-Consistency Testing via Representative Testing

**Paper:** [2503.01390](https://arxiv.org/abs/2503.01390) · [PDF](https://arxiv.org/pdf/2503.01390) · [HTML](https://arxiv.org/html/2503.01390)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** Pathfinder constructs a persistence graph from a POSIX or MMIO trace, groups update patterns and tests the crash states of representative patterns. Its grouping rules differ between POSIX and MMIO. [PDF, p. 8](https://arxiv.org/pdf/2503.01390v1#page=8) [PDF, p. 12](https://arxiv.org/pdf/2503.01390v1#page=12) [PDF, p. 13](https://arxiv.org/pdf/2503.01390v1#page=13) [PDF, p. 16](https://arxiv.org/pdf/2503.01390v1#page=16)

**Key result.** The authors found 18 bugs, including seven previously unknown ones, across eight production variants. The 4× comparison with ALICE concerns POSIX applications, and the 8× comparison with Jaaru concerns separate MMIO microbenchmarks. Both use a two-hour limit. [PDF, p. 4](https://arxiv.org/pdf/2503.01390v1#page=4) [PDF, p. 18](https://arxiv.org/pdf/2503.01390v1#page=18) [PDF, p. 20](https://arxiv.org/pdf/2503.01390v1#page=20) [PDF, p. 21](https://arxiv.org/pdf/2503.01390v1#page=21)

**Limitations and scope.** Results depend on the trace. Incomplete observation of thread synchronization excludes some permissible crash states, so the approach cannot systematically detect bugs that require those interleavings. [PDF, p. 23](https://arxiv.org/pdf/2503.01390v1#page=23) [PDF, p. 24](https://arxiv.org/pdf/2503.01390v1#page=24)

[Section and table audit for 2503.01390v1](../reviews/audit-2026-11-19/2503.01390v1.md)

## Overview

The paper presents efficient methods for testing application crash consistency during disk operations. [PDF, p. 1](https://arxiv.org/pdf/2503.01390v1#page=1)

## Source files

arXiv version `2503.01390v1` · PDF pages: 30.

- [Original PDF](https://arxiv.org/pdf/2503.01390v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2503.01390.metadata.json)

PDF bookmarks — [6 Evaluation (p. 17)](https://arxiv.org/pdf/2503.01390v1#page=17).

## Related concepts

- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Unit tests](../concepts/unit-testing.md)
- [Crash recovery](../concepts/fault-recovery.md)
- [File-system state durability](../concepts/file-system-durability.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
