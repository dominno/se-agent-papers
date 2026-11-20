---
type: source
title: "Finding and Analyzing Crash-Consistency Bugs in Persistent-Memory File Systems"
created: 2026-11-19
arxiv_id: "2204.06066"
url: "https://arxiv.org/abs/2204.06066"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["debugging", "long-term-memory", "memory-evaluation", "fault-recovery", "file-system-durability"]
source_path: "raw/papers/2204.06066.md"
sources: ["https://arxiv.org/abs/2204.06066"]
ingested: "2026-11-19"
---

# Finding and Analyzing Crash-Consistency Bugs in Persistent-Memory File Systems

**Paper:** [2204.06066](https://arxiv.org/abs/2204.06066) · [PDF](https://arxiv.org/pdf/2204.06066) · [HTML](https://arxiv.org/html/2204.06066)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** FlyTrap tests persistent-memory file systems and checks their state after a simulated crash. The authors also investigate the causes of the inconsistencies it finds. [PDF, p. 1](https://arxiv.org/pdf/2204.06066v1#page=1)

**Key result.** The authors report 18 distinct crash-consistency bugs in four file systems. All were reported to maintainers, who confirmed 16. Twelve had been fixed. [PDF, p. 1](https://arxiv.org/pdf/2204.06066v1#page=1) Two bugs occurred in both PMFS and WineFS. Fourteen of the 18 were classified as logic errors. For reconstruction of DRAM structures, Table 3 lists seven bugs, while the results text reports eight. [PDF, p. 9](https://arxiv.org/pdf/2204.06066v1#page=9) [PDF, p. 10](https://arxiv.org/pdf/2204.06066v1#page=10) [PDF, p. 11](https://arxiv.org/pdf/2204.06066v1#page=11)

**Limitations and scope.** The tool covers a subset of workloads and crash states. It assumes cache-line flushes are atomic with respect to crashes, so it can miss bugs. [PDF, p. 7](https://arxiv.org/pdf/2204.06066v1#page=7)

[Audit report for 2204.06066v1](../reviews/audit-2026-11-19/2204.06066v1.md)

## Overview

The study examines metadata persistence and recovery failures in persistent-memory file systems. [PDF, p. 1](https://arxiv.org/pdf/2204.06066v1#page=1)

## Source files

arXiv version `2204.06066v1` · PDF pages: 16.

- [Original PDF](https://arxiv.org/pdf/2204.06066v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2204.06066.metadata.json)

## Related concepts

- [Debugging](../concepts/debugging.md)
- [Long-term memory](../concepts/long-term-memory.md)
- [Memory evaluation](../concepts/memory-evaluation.md)
- [Crash recovery](../concepts/fault-recovery.md)
- [File-system state durability](../concepts/file-system-durability.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
