---
type: source
title: "Harness-of-Harness: Multi-Day Autonomous Software Development with Continual Improvement"
created: 2026-11-19
arxiv_id: "2609.01481"
url: "https://arxiv.org/abs/2609.01481"
review_status: "section_reviewed"
full_text_reviewed: false
tags: ["agent-orchestration", "task-planning", "coding-agents", "debugging", "self-evolution", "benchmarks", "long-horizon-development"]
source_path: "raw/papers/2609.01481.md"
sources: ["https://arxiv.org/abs/2609.01481"]
ingested: "2026-11-19"
---

# Harness-of-Harness: Multi-Day Autonomous Software Development with Continual Improvement

**Paper** [2609.01481](https://arxiv.org/abs/2609.01481) · [PDF](https://arxiv.org/pdf/2609.01481) · [HTML](https://arxiv.org/html/2609.01481)  
**Review status** `section_reviewed` · **Full-text review passed** No

## Research findings

**Method.** HoH repeatedly plans, modifies, and tests a software artifact. Each iteration passes the project state, planning document, and test evidence to the next. Final benchmark scores are kept separate from development. [PDF, p. 5](https://arxiv.org/pdf/2609.01481v1#page=5) · [PDF, p. 9](https://arxiv.org/pdf/2609.01481v1#page=9) · [PDF, p. 29](https://arxiv.org/pdf/2609.01481v1#page=29)

**Main result.** The nine comparisons in Table 1 give an average relative gain of 52.25% after three iterations. They cover the GameCraft Overall score, FrontierSWE Dominance, and mean ProgramBench test pass rate. The GameCraft Overall score for Codex/GPT-5.5 rises from 49.58 to 71.52. [PDF, p. 11](https://arxiv.org/pdf/2609.01481v1#page=11)

**Limitations.** The supplement lists 45 GameCraft tasks and 15 FrontierSWE tasks, with one valid run per condition and task. The announced ProgramBench sample could not be located. The available materials report only aggregate results for this third benchmark. [PDF, p. 10](https://arxiv.org/pdf/2609.01481v1#page=10) · [PDF, p. 11](https://arxiv.org/pdf/2609.01481v1#page=11) · [PDF, p. 30](https://arxiv.org/pdf/2609.01481v1#page=30) · [PDF, p. 31](https://arxiv.org/pdf/2609.01481v1#page=31) · [PDF, p. 38](https://arxiv.org/pdf/2609.01481v1#page=38)

[Version 2609.01481v1 audit of sections and tables](../reviews/audit-2026-11-19/2609.01481v1.md)

## Scope

Studies multi-day agent-driven software development through cycles of planning, implementation, testing, and improvement. [PDF, p. 1](https://arxiv.org/pdf/2609.01481v1#page=1)

## Source files

arXiv version `2609.01481v1` · PDF pages: 53.

- [Versioned PDF](https://arxiv.org/pdf/2609.01481v1)
- [Retrieval metadata, authors, license, and SHA-256 checksums (local file)](../raw/metadata/2609.01481.metadata.json)

PDF bookmarks — [Experiments: Benchmark Evaluation (p. 9)](https://arxiv.org/pdf/2609.01481v1#page=9).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Task planning](../concepts/task-planning.md)
- [Coding agents](../concepts/coding-agents.md)
- [Debugging](../concepts/debugging.md)
- [Agent self-improvement](../concepts/self-evolution.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Long-horizon software development](../concepts/long-horizon-development.md)

## Review notes

- This card was part of the original 100-paper index.
- **Reason for withholding full-text status.** The nine aggregate comparisons reproduce the 52.25% mean. The composition of the ProgramBench sample and its task-level results remain unknown. [Decision and evidence](../reviews/audit-2026-11-19/2609.01481v1.md)
