---
type: source
title: "Testing with AI Agents: An Empirical Study of Test Generation Frequency, Quality, and Coverage"
created: 2026-11-19
arxiv_id: "2603.13724"
url: "https://arxiv.org/abs/2603.13724"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "claim-verification", "grounded-generation", "benchmarks", "unit-testing", "evaluation-metrics"]
source_path: "raw/papers/2603.13724.md"
sources: ["https://arxiv.org/abs/2603.13724"]
ingested: "2026-11-19"
---

# Testing with AI Agents: An Empirical Study of Test Generation Frequency, Quality, and Coverage

**Paper:** [2603.13724](https://arxiv.org/abs/2603.13724) · [PDF](https://arxiv.org/pdf/2603.13724) · [HTML](https://arxiv.org/html/2603.13724)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** The authors selected the ten TypeScript/Vitest repositories with the most AI activity in adding tests. They identified test additions in pull-request patches, compared method structure in nine projects and measured coverage before and after changes in three. [PDF, p. 2](https://arxiv.org/pdf/2603.13724v1#page=2) [PDF, p. 3](https://arxiv.org/pdf/2603.13724v1#page=3) [PDF, p. 4](https://arxiv.org/pdf/2603.13724v1#page=4)

**Key result.** Table 1 attributes 366/2,232 observations to AI (16.4%). An independent count after deduplicating by project and SHA yields 351/1,977 unique commits (17.75%). [PDF, p. 2](https://arxiv.org/pdf/2603.13724v1#page=2) [Authors' data](https://github.com/suu-y/AI-human-test-comparison/blob/9abc31fd2fa053bcf3bd68209f37ecd30a1b3460/results/test_commits_from_github_api_detail.csv)

**Limitations and scope.** Coverage was measured in three projects across 531 observations. Branch coverage gains in helper were larger for human changes, while AI changes gained more in appkit. The authors leave fault detection to a separate study. [PDF, p. 4](https://arxiv.org/pdf/2603.13724v1#page=4)

[Audit of sections, tables and appendices](../reviews/audit-2026-11-19/2603.13724v1.md)

## Overview

The study compares how often agents write tests with the quality and code coverage of those tests. [PDF, p. 1](https://arxiv.org/pdf/2603.13724v1#page=1)

## Source files

arXiv version `2603.13724v1` · PDF pages: 5.

- [Original PDF](https://arxiv.org/pdf/2603.13724v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2603.13724.metadata.json)

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Claim verification](../concepts/claim-verification.md)
- [Source-grounded generation](../concepts/grounded-generation.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Unit tests](../concepts/unit-testing.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
