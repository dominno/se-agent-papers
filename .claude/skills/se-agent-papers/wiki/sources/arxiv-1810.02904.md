---
type: source
title: "Finding Crash-Consistency Bugs with Bounded Black-Box Crash Testing"
created: 2026-11-19
arxiv_id: "1810.02904"
url: "https://arxiv.org/abs/1810.02904"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["debugging", "benchmarks", "unit-testing", "stateful-tool-use", "tool-evaluation", "fault-recovery", "file-system-durability"]
source_path: "raw/papers/1810.02904.md"
sources: ["https://arxiv.org/abs/1810.02904"]
ingested: "2026-11-19"
---

# Finding Crash-Consistency Bugs with Bounded Black-Box Crash Testing

**Paper:** [1810.02904](https://arxiv.org/abs/1810.02904) · [PDF](https://arxiv.org/pdf/1810.02904) · [HTML](https://arxiv.org/html/1810.02904)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** ACE generates small workloads within specified bounds. After a simulated power loss, CrashMonkey compares recovered file-system data and metadata with the expected state of explicitly persisted objects. [PDF, p. 6](https://arxiv.org/pdf/1810.02904v1#page=6) [PDF, p. 7](https://arxiv.org/pdf/1810.02904v1#page=7)

**Key result.** The study reproduced 24 of 26 historical bug families (26 of 28 occurrences). Across 3.37 million workloads it found ten new bugs in btrfs and F2FS combined, plus one in an unverified part of FSCQ. [PDF, p. 4](https://arxiv.org/pdf/1810.02904v1#page=4) [PDF, p. 12](https://arxiv.org/pdf/1810.02904v1#page=12) [PDF, p. 13](https://arxiv.org/pdf/1810.02904v1#page=13) [PDF, p. 15](https://arxiv.org/pdf/1810.02904v1#page=15)

**Limitations and scope.** The bounds were chosen using known bug reports. The evaluation used small, freshly created file systems and crashes after specific persistence points. Its results apply to that state space. [PDF, p. 5](https://arxiv.org/pdf/1810.02904v1#page=5) [PDF, p. 6](https://arxiv.org/pdf/1810.02904v1#page=6) [PDF, p. 11](https://arxiv.org/pdf/1810.02904v1#page=11)

[Audit of sections, tables and appendices](../reviews/audit-2026-11-19/1810.02904v1.md)

## Overview

The study tests file-system consistency by interrupting writes at controlled points. [PDF, p. 1](https://arxiv.org/pdf/1810.02904v1#page=1)

## Source files

arXiv version `1810.02904v1` · PDF pages: 23.

- [Original PDF](https://arxiv.org/pdf/1810.02904v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/1810.02904.metadata.json)

PDF bookmarks — [6 Evaluation (p. 11)](https://arxiv.org/pdf/1810.02904v1#page=11).

## Related concepts

- [Debugging](../concepts/debugging.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Unit tests](../concepts/unit-testing.md)
- [Stateful tool use](../concepts/stateful-tool-use.md)
- [Tool evaluation](../concepts/tool-evaluation.md)
- [Crash recovery](../concepts/fault-recovery.md)
- [File-system state durability](../concepts/file-system-durability.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
