---
type: source
title: "How Agent Skills Evolve: A Large-Scale Empirical Study of Skills on GitHub"
created: 2026-11-19
arxiv_id: "2611.04456"
url: "https://arxiv.org/abs/2611.04456"
review_status: "section_reviewed"
full_text_reviewed: false
tags: ["agent-orchestration", "repository-context", "self-evolution", "agent-skills"]
source_path: "raw/papers/2611.04456.md"
sources: ["https://arxiv.org/abs/2611.04456"]
ingested: "2026-11-19"
---

# How Agent Skills Evolve: A Large-Scale Empirical Study of Skills on GitHub

**Paper** [2611.04456](https://arxiv.org/abs/2611.04456) · [PDF](https://arxiv.org/pdf/2611.04456) · [HTML](https://arxiv.org/html/2611.04456)  
**Review status** `section_reviewed` · **Full-text review passed** No

## Research findings

**Method.** The authors collected 84,200 agent skills and 750,898 associated commits from GitHub. They developed a taxonomy through manual annotation and used it to label changes automatically. [PDF, p. 1](https://arxiv.org/pdf/2611.04456v1#page=1)

**Main result.** Of 84,200 skills with usable histories, 58.5% changed fewer than five times after creation. In the detailed analysis of 5,628 active skills, the most common change types were knowledge enrichment (9.00%) and procedural refinement (8.50%). [PDF, p. 7](https://arxiv.org/pdf/2611.04456v1#page=7) · [PDF, p. 8](https://arxiv.org/pdf/2611.04456v1#page=8)

**Limitations.** The detailed labels primarily describe visible, actively maintained repositories. Agreement with manual annotations was 0.816 for change type and 0.840 for motivation. The external supplement documenting annotation was unavailable on the audit date. [PDF, p. 9](https://arxiv.org/pdf/2611.04456v1#page=9) · [PDF, p. 10](https://arxiv.org/pdf/2611.04456v1#page=10) · [PDF, p. 11](https://arxiv.org/pdf/2611.04456v1#page=11)

[Audit report for 2611.04456v1](../reviews/audit-2026-11-19/2611.04456v1.md)

## Scope

Examines changes to agent skill files in real repositories and how maintainers manage those changes. [PDF, p. 1](https://arxiv.org/pdf/2611.04456v1#page=1)

## Source files

arXiv version `2611.04456v1` · PDF pages: 12.

- [Versioned PDF](https://arxiv.org/pdf/2611.04456v1)
- [Retrieval metadata, authors, license, and SHA-256 checksums (local file)](../raw/metadata/2611.04456.metadata.json)

PDF bookmarks — [Methodology (p. 3)](https://arxiv.org/pdf/2611.04456v1#page=3) · [Results (p. 6)](https://arxiv.org/pdf/2611.04456v1#page=6) · [Threats to Validity (p. 10)](https://arxiv.org/pdf/2611.04456v1#page=10).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Repository context](../concepts/repository-context.md)
- [Agent self-improvement](../concepts/self-evolution.md)
- [Agent skills](../concepts/agent-skills.md)

## Review notes

- This card was part of the original 100-paper index.
- The main text and all four tables were checked. The external supplement documenting annotation remains outstanding.
- The 404 commits in Table IV identify the sample. Accuracy is averaged over commits after aligning changed components, so multiplying the accuracy by 404 does not recover a count of correctly labeled components. [Section V-A, p. 9](https://arxiv.org/pdf/2611.04456v1#page=9)
- **Reason for withholding full-text status.** The unavailable supplement includes annotation instructions and detailed agreement results. [Decision and evidence](../reviews/audit-2026-11-19/2611.04456v1.md)
