# Full-text review checklist

Document retrieval and verification of a paper's findings are separate steps.

## A. Bibliographic verification

- [ ] Verify the arXiv identifier, title, authors, year, version, and full-text availability.
- [ ] Check for withdrawal, material corrections, and newer versions.
- [ ] Identify the license and record the metadata in the register.

## B. Read the complete paper

- [ ] Read the introduction and related work. Identify the problem, motivation, and definitions.
- [ ] Read the full methodology, including assumptions, components, algorithms, and data.
- [ ] Check the experimental setup, including datasets, models, baselines, metrics, and budget.
- [ ] Read all results and key tables. Examine statistical differences and ablations.
- [ ] Read the limitations, negative results, and discussion.
- [ ] Inspect relevant appendices, pseudocode, and implementation availability.

## C. Record findings others can use

- [ ] Distinguish the authors' reported findings from the reviewer's interpretations and recommendations.
- [ ] Give each individual claim a section or page, the paper version, and the type of evidence.
- [ ] For numerical results, record the population, metric, baseline, interval, and experimental conditions.
- [ ] Document counterarguments, limits on generalization, and publications with conflicting results.
- [ ] Update relevant entities, method definitions, concept maps, and relationships.
- [ ] Check that any quotations and raw source files included in a shared ZIP are permitted for redistribution.

## D. Independent check

- [ ] Verify internal links and references to sources.
- [ ] Have an independent reviewer confirm selected individual claims against the cited evidence.
- [ ] Record the `fulltext_reviewed` status and review date in a version-specific report only after completing A–D.

## Review states

`catalog_import_only` → `abstract_verified` → `section_reviewed` → `fulltext_reviewed` → `claims_verified`.

`retrieved_not_reviewed` records the technical state of a download. It does not advance the review. A `model_draft_unverified` requires independent verification before it can support a review decision.
