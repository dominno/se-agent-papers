---
type: source
title: "SquirrelFS: Using the Rust Compiler to Check File-System Crash Consistency"
created: 2026-11-19
arxiv_id: "2406.09649"
url: "https://arxiv.org/abs/2406.09649"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["parallelism", "workflow-optimization", "stateful-tool-use", "tool-evaluation", "fault-recovery", "file-system-durability"]
source_path: "raw/papers/2406.09649.md"
sources: ["https://arxiv.org/abs/2406.09649"]
ingested: "2026-11-19"
---

# SquirrelFS: Using the Rust Compiler to Check File-System Crash Consistency

**Paper:** [2406.09649](https://arxiv.org/abs/2406.09649) · [PDF](https://arxiv.org/pdf/2406.09649) · [HTML](https://arxiv.org/html/2406.09649)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** Synchronous Soft Updates uses Rust typestate to enforce the order in which metadata updates become persistent. An Alloy model and tests check additional implementation properties. [PDF, p. 5](https://arxiv.org/pdf/2406.09649v1#page=5) [PDF, p. 6](https://arxiv.org/pdf/2406.09649v1#page=6) [PDF, p. 8](https://arxiv.org/pdf/2406.09649v1#page=8) [PDF, p. 13](https://arxiv.org/pdf/2406.09649v1#page=13)

**Key result.** On Filebench, throughput was 8% higher for fileserver and 13% higher for varmail than with the fastest competitor. On RocksDB workload E range scans, ext4-DAX performed best. [PDF, p. 11](https://arxiv.org/pdf/2406.09649v1#page=11) [PDF, p. 12](https://arxiv.org/pdf/2406.09649v1#page=12)

**Limitations and scope.** The Alloy model covered up to two operations, ten persistent objects and 30 steps. Chipmunk found four bugs outside the ordering checks, including three in reconstruction of volatile structures. [PDF, p. 13](https://arxiv.org/pdf/2406.09649v1#page=13) [PDF, p. 14](https://arxiv.org/pdf/2406.09649v1#page=14)

[Section and table audit for 2406.09649v1](../reviews/audit-2026-11-19/2406.09649v1.md)

## Overview

The authors use Rust's type system to enforce safe ordering of file-system writes. [PDF, p. 1](https://arxiv.org/pdf/2406.09649v1#page=1)

## Source files

arXiv version `2406.09649v1` · PDF pages: 18.

- [Original PDF](https://arxiv.org/pdf/2406.09649v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2406.09649.metadata.json)

PDF bookmarks — [Evaluation (p. 11)](https://arxiv.org/pdf/2406.09649v1#page=11).

Title in the retrieved arXiv record: SquirrelFS: using the Rust compiler to check file-system crash consistency.

## Related concepts

- [Parallelism](../concepts/parallelism.md)
- [Workflow optimization](../concepts/workflow-optimization.md)
- [Stateful tool use](../concepts/stateful-tool-use.md)
- [Tool evaluation](../concepts/tool-evaluation.md)
- [Crash recovery](../concepts/fault-recovery.md)
- [File-system state durability](../concepts/file-system-durability.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
