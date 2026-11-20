---
type: source
title: "Practical Detectability for Persistent Lock-Free Data Structures"
created: 2026-11-19
arxiv_id: "2203.07621"
url: "https://arxiv.org/abs/2203.07621"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["benchmarks"]
source_path: "raw/papers/2203.07621.md"
sources: ["https://arxiv.org/abs/2203.07621"]
ingested: "2026-11-19"
---

# Practical Detectability for Persistent Lock-Free Data Structures

**Paper:** [2203.07621](https://arxiv.org/abs/2203.07621) · [PDF](https://arxiv.org/pdf/2203.07621) · [HTML](https://arxiv.org/html/2203.07621)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** A thread records progress and operation results in persistent memento objects. After a restart, it can replay completed suboperations and execute the remaining ones. Composing suboperations requires stable branch conditions and loop state, among other conditions. [PDF, p. 3](https://arxiv.org/pdf/2203.07621v1#page=3) [PDF, p. 4](https://arxiv.org/pdf/2203.07621v1#page=4)

**Key result.** MSQ-mmt-vol generally achieved higher throughput than the durable Michael–Scott queues tested. The authors note an exception for LogQ at 80% insertions with few threads. Hash-table lookups had similar throughput, while updates generally incurred overhead. [PDF, p. 11](https://arxiv.org/pdf/2203.07621v1#page=11) [PDF, p. 12](https://arxiv.org/pdf/2203.07621v1#page=12)

**Limitations and scope.** The system assumes a single Optane module and statically known root objects, among other conditions. Measurements pinned to one socket cover specific implementations, operation types and key distributions. Source data show 10 million initial elements in three randomized queue workloads and zero for the alternating enqueue–dequeue pair. Hash-table logs report Linux 5.4.0-91, while the text gives 5.11. Figure 8 uses the skewed distribution and Figure 9 the uniform distribution. [Original measurements](https://drive.google.com/file/d/1CC5rrLHcynNWTrZKcJcN9azoasqbOSQv/view) [PDF, p. 5](https://arxiv.org/pdf/2203.07621v1#page=5) [PDF, p. 11](https://arxiv.org/pdf/2203.07621v1#page=11) [PDF, p. 12](https://arxiv.org/pdf/2203.07621v1#page=12)

[Section and table audit for 2203.07621v1](../reviews/audit-2026-11-19/2203.07621v1.md)

## Overview

The study examines how to determine whether an operation completed before a crash and how to recover its result safely. [PDF, p. 1](https://arxiv.org/pdf/2203.07621v1#page=1)

## Source files

**Paper license notice.** The arXiv record lists CC BY 4.0. The PDF states CC BY-NC-ND 4.0. This wiki links to the reviewed version. [PDF, p. 1](https://arxiv.org/pdf/2203.07621v1#page=1)

arXiv version `2203.07621v1` · PDF pages: 15.

- [Original PDF](https://arxiv.org/pdf/2203.07621v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2203.07621.metadata.json)

PDF bookmarks — [7 Evaluation (p. 11)](https://arxiv.org/pdf/2203.07621v1#page=11).

## Related concepts

- [Agent and LLM benchmarks](../concepts/benchmarks.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
- The review examined the main text, LaTeX source, historical repository and 162 measurement files from the original supplement. The report documents discrepancies in the description of the environment, initial queue states and ordering of distributions. [Authors' supplement, March 2022](https://web.archive.org/web/20220325152549/https://cp.kaist.ac.kr/memento)
