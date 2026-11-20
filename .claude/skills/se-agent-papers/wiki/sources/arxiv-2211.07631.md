---
type: source
title: "The Path to Durable Linearizability"
created: 2026-11-19
arxiv_id: "2211.07631"
url: "https://arxiv.org/abs/2211.07631"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["fault-recovery", "file-system-durability"]
source_path: "raw/papers/2211.07631.md"
sources: ["https://arxiv.org/abs/2211.07631"]
ingested: "2026-11-19"
---

# The Path to Durable Linearizability

**Paper:** [2211.07631](https://arxiv.org/abs/2211.07631) · [PDF](https://arxiv.org/pdf/2211.07631) · [HTML](https://arxiv.org/html/2211.07631)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** The authors separate the correctness of crash recovery, volatile linearizability and constraints on the order of persistence. Their theorem specifies when these parts imply durable linearizability. [PDF, p. 15](https://arxiv.org/pdf/2211.07631v1#page=15) [PDF, p. 16](https://arxiv.org/pdf/2211.07631v1#page=16) [PDF, p. 18](https://arxiv.org/pdf/2211.07631v1#page=18) [PDF, p. 19](https://arxiv.org/pdf/2211.07631v1#page=19)

**Key result.** Theorem C.60 establishes durable linearizability for the link-free implementation studied. The verification covers operations whose linearization points depend on the execution history, as well as correct link recovery. [PDF, p. 18](https://arxiv.org/pdf/2211.07631v1#page=18) [PDF, p. 56](https://arxiv.org/pdf/2211.07631v1#page=56) [PDF, p. 62](https://arxiv.org/pdf/2211.07631v1#page=62) [PDF, p. 63](https://arxiv.org/pdf/2211.07631v1#page=63)

**Limitations and scope.** The proof is conditional on the memory model and implementation. The authors assume synchronous flushes and study unbuffered durable linearizability. They do not measure hardware performance. [PDF, p. 5](https://arxiv.org/pdf/2211.07631v1#page=5) [PDF, p. 21](https://arxiv.org/pdf/2211.07631v1#page=21) [PDF, p. 28](https://arxiv.org/pdf/2211.07631v1#page=28) [PDF, p. 29](https://arxiv.org/pdf/2211.07631v1#page=29)

[Audit of sections, tables and appendices](../reviews/audit-2026-11-19/2211.07631v1.md)

## Overview

The authors formalize correctness for concurrent operations whose effects must remain consistent across crashes. [PDF, p. 1](https://arxiv.org/pdf/2211.07631v1#page=1)

## Source files

arXiv version `2211.07631v1` · PDF pages: 63.

- [Original PDF](https://arxiv.org/pdf/2211.07631v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2211.07631.metadata.json)

## Related concepts

- [Crash recovery](../concepts/fault-recovery.md)
- [File-system state durability](../concepts/file-system-durability.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
