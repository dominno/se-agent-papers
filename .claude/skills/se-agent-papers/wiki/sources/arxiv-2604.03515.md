---
type: source
title: "Inside the Scaffold: A Source-Code Taxonomy of Coding Agent Architectures"
created: 2026-11-19
arxiv_id: "2604.03515"
url: "https://arxiv.org/abs/2604.03515"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "task-planning", "coding-agents", "architecture-design", "citation-grounding"]
source_path: "raw/papers/2604.03515.md"
sources: ["https://arxiv.org/abs/2604.03515"]
ingested: "2026-11-19"
---

# Inside the Scaffold: A Source-Code Taxonomy of Coding Agent Architectures

**Paper:** [2604.03515](https://arxiv.org/abs/2604.03515) · [PDF](https://arxiv.org/pdf/2604.03515) · [HTML](https://arxiv.org/html/2604.03515)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** The author examined the code of 13 open-source harnesses at fixed commits. After piloting two systems, the author identified 12 dimensions covering control flow, the tool interface and resource management. [PDF, p. 7](https://arxiv.org/pdf/2604.03515v2#page=7) [PDF, p. 8](https://arxiv.org/pdf/2604.03515v2#page=8) [PDF, p. 9](https://arxiv.org/pdf/2604.03515v2#page=9) [PDF, p. 11](https://arxiv.org/pdf/2604.03515v2#page=11) [PDF, p. 42](https://arxiv.org/pdf/2604.03515v2#page=42)

**Key result.** The author found coexisting control mechanisms in 11 of 13 harnesses. For example, Aider's outer loop accepts user input, while its inner loop can repeat code revision autonomously. [PDF, p. 1](https://arxiv.org/pdf/2604.03515v2#page=1) [PDF, p. 11](https://arxiv.org/pdf/2604.03515v2#page=11) [PDF, p. 12](https://arxiv.org/pdf/2604.03515v2#page=12)

**Limitations and scope.** Static analysis identifies which constructs are available. It does not measure how often they are used or how they affect task outcomes. Table 1 lists 9 Python, 3 TypeScript and 1 Rust/TypeScript implementation, while the limitations section lists 10 in Python. [PDF, p. 6](https://arxiv.org/pdf/2604.03515v2#page=6) [PDF, p. 7](https://arxiv.org/pdf/2604.03515v2#page=7) [PDF, p. 34](https://arxiv.org/pdf/2604.03515v2#page=34) [PDF, p. 35](https://arxiv.org/pdf/2604.03515v2#page=35)

## Overview

The paper analyzes coding-agent frameworks and identifies common elements in their execution loops. [PDF, p. 1](https://arxiv.org/pdf/2604.03515v2#page=1)

[Section and evidence audit](../reviews/audit-2026-11-19/2604.03515v2.md)

## Source files

arXiv version `2604.03515v2` · PDF pages: 42.

- [Original PDF](https://arxiv.org/pdf/2604.03515v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2604.03515.metadata.json)

PDF bookmarks — [Methodology (p. 6)](https://arxiv.org/pdf/2604.03515v2#page=6) · [Results (p. 10)](https://arxiv.org/pdf/2604.03515v2#page=10) · [Threats to Validity (p. 33)](https://arxiv.org/pdf/2604.03515v2#page=33).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Task planning](../concepts/task-planning.md)
- [Coding agents](../concepts/coding-agents.md)
- [Software architecture](../concepts/architecture-design.md)
- [Citations and supporting evidence](../concepts/citation-grounding.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
