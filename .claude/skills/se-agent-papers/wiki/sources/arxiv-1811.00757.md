---
type: source
title: "DurableFS: A File System for Persistent Memory"
created: 2026-11-19
arxiv_id: "1811.00757"
url: "https://arxiv.org/abs/1811.00757"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["long-term-memory", "memory-evaluation", "fault-recovery", "file-system-durability"]
source_path: "raw/papers/1811.00757.md"
sources: ["https://arxiv.org/abs/1811.00757"]
ingested: "2026-11-19"
---

# DurableFS: A File System for Persistent Memory

**Paper:** [1811.00757](https://arxiv.org/abs/1811.00757) · [PDF](https://arxiv.org/pdf/1811.00757) · [Read the article online](https://arxiv.org/pdf/1811.00757v1)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** DurableFS uses copy-on-write for data and a redo log to recover metadata changes. The single-file guarantee covers operations from opening the file to a successful close. [PDF, p. 1](https://arxiv.org/pdf/1811.00757v1#page=1) [PDF, p. 4](https://arxiv.org/pdf/1811.00757v1#page=4) [PDF, p. 5](https://arxiv.org/pdf/1811.00757v1#page=5)

**Key result.** In Figure 3, throughput relative to DurableFS without data-cache flushing falls by 9.56% for Fio, 7.29% for the Filebench fileserver and 3.32% for the webserver. The unweighted mean is 6.72%, consistent with the authors’ estimate of about 7%. [PDF, p. 5](https://arxiv.org/pdf/1811.00757v1#page=5)

**Limitations and scope.** The experiment used 4 GB of DRAM to emulate persistent memory. The chart reports means over ten repetitions without a measure of dispersion. It does not test durability after physical power loss. [PDF, p. 5](https://arxiv.org/pdf/1811.00757v1#page=5)

[Section and table audit for 1811.00757v1](../reviews/audit-2026-11-19/1811.00757v1.md)

## Overview

The paper describes atomic, durable file-system operations based on logging and copy-on-write. [PDF, p. 1](https://arxiv.org/pdf/1811.00757v1#page=1)

## Source files

arXiv version `1811.00757v1` · PDF pages: 6.

- [Original PDF](https://arxiv.org/pdf/1811.00757v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/1811.00757.metadata.json)

## Related concepts

- [Long-term memory](../concepts/long-term-memory.md)
- [Memory evaluation](../concepts/memory-evaluation.md)
- [Crash recovery](../concepts/fault-recovery.md)
- [File-system state durability](../concepts/file-system-durability.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
