---
type: source
title: "SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents"
created: 2026-11-19
arxiv_id: "2605.21384"
url: "https://arxiv.org/abs/2605.21384"
review_status: "section_reviewed"
full_text_reviewed: false
tags: ["agent-orchestration", "coding-agents", "context-window", "evaluation-metrics", "benchmarks", "long-horizon-development", "comparison-and-reproducibility"]
source_path: "raw/papers/2605.21384.md"
sources: ["https://arxiv.org/abs/2605.21384"]
ingested: "2026-11-19"
---

# SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents

**Paper** [2605.21384](https://arxiv.org/abs/2605.21384) · [PDF](https://arxiv.org/pdf/2605.21384) · [HTML](https://arxiv.org/html/2605.21384)  
**Review status** `section_reviewed` · **Full-text review passed** No

## Research findings

**Method.** SpecBench compares pass rates on public tests of features in isolation with pass rates on hidden tests of feature interactions for the same implementation. The study compares models, agent environments, and strategies for selecting the next revision. [PDF, p. 2](https://arxiv.org/pdf/2605.21384v2#page=2) · [PDF, p. 3](https://arxiv.org/pdf/2605.21384v2#page=3) · [PDF, p. 5](https://arxiv.org/pdf/2605.21384v2#page=5)

**Main result.** The mean gap in Figure 2 increases by 23 percentage points per tenfold increase in reference code size. For P90 the plot gives +28 points (R² = 0.25), while the text gives +27 points (R² = 0.21). Measuring the vector lines yields 22.72 and 28.42 points for the mean and P90, respectively. [PDF, p. 3](https://arxiv.org/pdf/2605.21384v2#page=3) · [PDF, p. 5](https://arxiv.org/pdf/2605.21384v2#page=5)

**Limitations.** The gap captures both failures of interacting features and fitting specific examples. The summary reports 30 tasks, while Table 5 and Figure 2 name 31. Figure 2 shows 1,329 data markers. Its plot cannot establish which observations entered the regression. Test counts in Table 5 and resource totals in Table 3 also disagree with their printed totals. [PDF, p. 3](https://arxiv.org/pdf/2605.21384v2#page=3) · [PDF, p. 10](https://arxiv.org/pdf/2605.21384v2#page=10) · [PDF, p. 15](https://arxiv.org/pdf/2605.21384v2#page=15) · [PDF, p. 17](https://arxiv.org/pdf/2605.21384v2#page=17)

[Audit of sections, tables, and appendices](../reviews/audit-2026-11-19/2605.21384v2.md)

## Scope

Studies how coding agents can optimize for visible tests while missing requirements those tests do not cover. [PDF, p. 1](https://arxiv.org/pdf/2605.21384v2#page=1)

## Source files

arXiv version `2605.21384v2` · PDF pages: 22.

- [Versioned PDF](https://arxiv.org/pdf/2605.21384v2)
- [Retrieval metadata, authors, license, and SHA-256 checksums (local file)](../raw/metadata/2605.21384.metadata.json)

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Coding agents](../concepts/coding-agents.md)
- [Context window](../concepts/context-window.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Long-horizon software development](../concepts/long-horizon-development.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)

## Review notes

- This card was part of the original 100-paper index.
- **Reason for withholding full-text status.** Figure 2 and the task list name 31 tasks, while Table 1 gives 30. The audit confirmed the plotted slopes. Resolving the regression, test counts, and resource totals requires the original run records or an erratum. [Decision and evidence](../reviews/audit-2026-11-19/2605.21384v2.md)
