---
type: concept
title: "File-system state durability"
created: 2026-11-19
tags: ["file-system-durability", "research"]
sources: ["https://arxiv.org/abs/1810.02904", "https://arxiv.org/abs/1811.00757", "https://arxiv.org/abs/2204.06066", "https://arxiv.org/abs/2211.07631", "https://arxiv.org/abs/2406.09649", "https://arxiv.org/abs/2503.01390", "https://arxiv.org/abs/2511.18323"]
---

# File-system state durability

Atomic writes, crash resilience and preservation of invariants.

**Status:** This page groups papers by topic. An entry in the list indicates **a topical relationship**. It does not imply that every claim is confirmed or that one paper cites another.

## Papers on this topic (8)

- [Crash-Consistent Checkpointing for AI Training on macOS/APFS](../sources/arxiv-2511.18323.md) — The study compares protocols for persisting checkpoints on macOS/APFS and detecting data corruption with checksums.
- [DurableFS: A File System for Persistent Memory](../sources/arxiv-1811.00757.md) — The paper describes atomic, durable file-system operations based on logging and copy-on-write.
- [Finding and Analyzing Crash-Consistency Bugs in Persistent-Memory File Systems](../sources/arxiv-2204.06066.md) — The study examines metadata persistence and recovery failures in persistent-memory file systems.
- [Finding Crash-Consistency Bugs with Bounded Black-Box Crash Testing](../sources/arxiv-1810.02904.md) — The study tests file-system consistency by interrupting writes at controlled points.
- [Scalable and Accurate Application-Level Crash-Consistency Testing via Representative Testing](../sources/arxiv-2503.01390.md) — The paper presents efficient methods for testing application crash consistency during disk operations.
- [SquirrelFS: Using the Rust Compiler to Check File-System Crash Consistency](../sources/arxiv-2406.09649.md) — The authors use Rust's type system to enforce safe ordering of file-system writes.
- [The Path to Durable Linearizability](../sources/arxiv-2211.07631.md) — The authors formalize correctness for concurrent operations whose effects must remain consistent across crashes.

## Review questions

- How do the papers define the problem and the scope of their evaluation?
- Which conclusions have experimental support, and which are interpretations?
- When do these methods compete, and when do they complement each other?
- Which questions require consulting the full text?
