# Publication review status

The catalog contains 173 papers. The audit completed on 20 November 2026 covers 165 of them. [Current catalog counts](../catalog/review_progress.json)

| Review status | Papers | Evidence checked |
|---|---:|---|
| `section_reviewed` | 5 | Reviewers checked the cited method, result, and limitation in the recorded PDF version. A specific issue remains open. |
| `abstract_verified` | 0 | Abstract and metadata checked. |
| `catalog_import_only` | 8 | Bibliographic record imported from arXiv. Findings await review. |
| `fulltext_reviewed` | 160 | Complete paper read and checked section by section. |

[Decisions and reports by paper version](audit-2026-11-19/README.md)

## Follow-up on the five open decisions

The repository and archive checks clarified the CAID version mismatch, the number of tasks plotted by SpecBench, the name of the missing ProgramBench CSV, the mathematical bound in SEAL and how agreement was averaged in How Agent Skills Evolve. All five reports identify the evidence still needed. [Open decisions](audit-2026-11-19/README.md#papers-awaiting-resolution)

## Full audit, 19–20 November 2026

All 165 paper versions have individual reports. Of these, 160 passed full review. The other five cards explain the outstanding issue and link to the evidence. The audit checked each card against its source. Individual reports identify any additional checks of underlying data, calculations, and the authors' artifacts.

Reviewers checked 495 entries on methods, results, and limitations. They verified the SHA-256 checksums of all 165 PDFs and 165 extracts and the page numbering across 4,317 pages in the local texts. In the wiki, reports, and navigation documents at the time of the audit, 10,765 local link occurrences were checked. Of these, 6,227 pointed to a specific PDF page, covering 3,560 distinct pages across the corpus. All local targets existed, all page numbers were in range, and 735 distinct active external addresses responded successfully. The wiki structure validator checked 314 pages without errors. The reports identify sources that could not be accessed.

## English edition and public links, 20 November 2026

The English edition covers all 165 publication cards and all 165 version-specific reports, along with the catalog and navigation. Translation used a local Polish–English model and independent agent editing. The checks compared figures, units, denominators, scientific notation and conclusions with the Polish records. The original papers and page-indexed extracts retain their original text.

The public file tree passed checks for 4,210 internal Markdown links and 6,250 versioned PDF page citations. These citations cover 3,561 distinct version–page pairs. Across the 19–20 November checks, all 936 distinct external destinations linked in the release responded. The SpecBench submission page is accessible, but downloading its supplementary attachment returned HTTP 403. All 165 local PDFs and 165 page-indexed extracts matched their recorded SHA-256 digests. Their page sequences cover 4,317 pages.

## What the publication cards cover

Each of the 165 cards describes the method, main result, and a limitation or boundary on the conclusion. Each part cites a physical PDF page in the reviewed arXiv version. Empirical results refer to the stated sample and protocol. Reviews describe the synthesis of earlier research, and formal papers describe what was proved. Limitations include both the authors' observations and limits implied by their choice of data, metrics, or comparisons.

The `section_reviewed` status records verification of these specific findings. Full review also requires checking all sections, tables, and appendices and completing an independent check. [Full-text review checklist](FULLTEXT_REVIEW_CHECKLIST.md)

**Local collection at audit time.** All 165 papers had a PDF accessible from the [wiki index](../index.md). Each card linked the versioned original, page-numbered text, and provenance metadata with authors, license, and two SHA-256 checksums. The PDFs had 4,317 pages in total. For 126 papers, selected section links were derived from PDF bookmarks. The [AgentCoder card](../sources/arxiv-2312.13010.md) illustrates the record.

**Earlier section review.** The 495 substantive entries included 512 page citations. Including earlier notes, descriptions, and bookmarks, reviewers checked 926 links on publication cards against 584 distinct PDF pages. They checked the local file versions by SHA-256 and compared the text on the cited pages with the local extracts. The structure validator checked 314 wiki pages without errors.

**Import checks.** The earlier import also checked 493 distinct external addresses. During extraction, MuPDF reported a color-space issue affecting some images in SWE-Search and TextGrad. Both papers retained their original PDFs and text extracts covering every page.

`scripts/fetch_fulltext.py` retrieves source material. `scripts/draft_review.py` helps draft a review. Reviewers must independently verify claims before changing the review status.

## Limits on interpretation

- `about_topic` edges classify papers by subject. Evidence of a citation requires checking the source.
- Applying a cataloged algorithm to a new project requires evidence for that setting.
- Numerical results, charts, and page locations require source verification. Leave missing information open.
- Full-text review requires reading and verification beyond downloading a file or summarizing its abstract.
