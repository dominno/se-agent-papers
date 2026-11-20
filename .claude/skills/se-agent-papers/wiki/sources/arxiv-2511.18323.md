---
type: source
title: "Crash-Consistent Checkpointing for AI Training on macOS/APFS"
created: 2026-11-19
arxiv_id: "2511.18323"
url: "https://arxiv.org/abs/2511.18323"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["stateful-tool-use", "tool-evaluation", "fault-recovery", "file-system-durability"]
source_path: "raw/papers/2511.18323.md"
sources: ["https://arxiv.org/abs/2511.18323"]
ingested: "2026-11-19"
---

# Crash-Consistent Checkpointing for AI Training on macOS/APFS

**Paper:** [2511.18323](https://arxiv.org/abs/2511.18323) · [PDF](https://arxiv.org/pdf/2511.18323) · [HTML](https://arxiv.org/html/2511.18323)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** The authors compare three checkpoint installation protocols on APFS and SHA-256 integrity checking with rollback of a corrupted write. [PDF, p. 1](https://arxiv.org/pdf/2511.18323v1#page=1)

**Key result.** After an atomic write, the checks detected 400/400 bit flips, 400/400 truncations and 399/400 zeroings, with 0/400 false positives. The experiment injected corruption after the write. [PDF, p. 7](https://arxiv.org/pdf/2511.18323v1#page=7) [PDF, p. 11](https://arxiv.org/pdf/2511.18323v1#page=11)

**Limitations and scope.** Process-interruption trials tested only unsynchronized writes (0/430 complete groups). The atomic control achieved 400/400 in runs without failures. The study used one APFS node and synthetic data and did not test power loss. [PDF, p. 9](https://arxiv.org/pdf/2511.18323v1#page=9) [PDF, p. 13](https://arxiv.org/pdf/2511.18323v1#page=13)

[Audit report for 2511.18323v1](../reviews/audit-2026-11-19/2511.18323v1.md)

## Overview

The study compares protocols for persisting checkpoints on macOS/APFS and detecting data corruption with checksums. [PDF, p. 1](https://arxiv.org/pdf/2511.18323v1#page=1)

## Source files

arXiv version `2511.18323v1` · PDF pages: 16.

- [Original PDF](https://arxiv.org/pdf/2511.18323v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2511.18323.metadata.json)

PDF bookmarks — [Experimental Methodology (p. 7)](https://arxiv.org/pdf/2511.18323v1#page=7).

## Related concepts

- [Stateful tool use](../concepts/stateful-tool-use.md)
- [Tool evaluation](../concepts/tool-evaluation.md)
- [Crash recovery](../concepts/fault-recovery.md)
- [File-system state durability](../concepts/file-system-durability.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
