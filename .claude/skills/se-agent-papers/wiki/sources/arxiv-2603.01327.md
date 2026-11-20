---
type: source
title: "SWE-Adept: An LLM-Based Agentic Framework for Deep Codebase Analysis and Structured Issue Resolution"
created: 2026-11-19
arxiv_id: "2603.01327"
url: "https://arxiv.org/abs/2603.01327"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "task-planning", "coding-agents", "repository-context", "debugging"]
source_path: "raw/papers/2603.01327.md"
sources: ["https://arxiv.org/abs/2603.01327"]
ingested: "2026-11-19"
---

# SWE-Adept: An LLM-Based Agentic Framework for Deep Codebase Analysis and Structured Issue Resolution

**Paper:** [2603.01327](https://arxiv.org/abs/2603.01327) · [PDF](https://arxiv.org/pdf/2603.01327) · [HTML](https://arxiv.org/html/2603.01327)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** A localization agent searches a syntax-based repository index. A second agent works with hypotheses and checkpoints assigned to repair steps. [PDF, p. 4](https://arxiv.org/pdf/2603.01327v3#page=4) [PDF, p. 5](https://arxiv.org/pdf/2603.01327v3#page=5) [PDF, p. 6](https://arxiv.org/pdf/2603.01327v3#page=6)

**Key result.** With GPT-5.2 on Lite, SWE-Adept placed the correct function in the top five in 70.8% of cases, compared with 64.6% for LocAgent. On the Pro subset it resolved 37.8% of issues, compared with 33.5% for OrcaLoca. [PDF, p. 7](https://arxiv.org/pdf/2603.01327v3#page=7) [PDF, p. 8](https://arxiv.org/pdf/2603.01327v3#page=8) [PDF, p. 12](https://arxiv.org/pdf/2603.01327v3#page=12)

**Limitations and scope.** The Pro data comprise 200 tasks, including 20 in TypeScript. Results are means over two runs. The appendix also covers two open models, so the evaluation extends beyond commercial models. [PDF, p. 12](https://arxiv.org/pdf/2603.01327v3#page=12) [PDF, p. 13](https://arxiv.org/pdf/2603.01327v3#page=13) [PDF, p. 15](https://arxiv.org/pdf/2603.01327v3#page=15)

[Section and table audit for 2603.01327v3](../reviews/audit-2026-11-19/2603.01327v3.md)

## Overview

The method combines repository analysis, repair planning and checkpoints to support work on complex issues. [PDF, p. 1](https://arxiv.org/pdf/2603.01327v3#page=1)

## Source files

arXiv version `2603.01327v3` · PDF pages: 19.

- [Original PDF](https://arxiv.org/pdf/2603.01327v3)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2603.01327.metadata.json)

PDF bookmarks — [SWE-Adept Framework (p. 4)](https://arxiv.org/pdf/2603.01327v3#page=4) · [Experiments (p. 6)](https://arxiv.org/pdf/2603.01327v3#page=6).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Task planning](../concepts/task-planning.md)
- [Coding agents](../concepts/coding-agents.md)
- [Repository context](../concepts/repository-context.md)
- [Debugging](../concepts/debugging.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
