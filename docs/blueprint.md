# Research Lab — Product and Engineering Blueprint

## Goal
Build an open-source system for learning the mathematics behind ML. Each major concept should connect intuition, formal mathematics, derivation, implementation, visualization where useful, assessment, and an ML application.

## Architecture
- `curriculum/`: authoritative topic content and machine-readable metadata.
- `src/mathml/`: reusable implementations independent of notebooks and website code.
- `notebooks/`: executable demonstrations and experiments.
- `visualizations/`: interactive explanations where interaction adds learning value.
- `problem-sets/`: conceptual, derivation, and coding assessments.
- `projects/`: reproducible investigations with hypotheses, baselines, metrics, and limitations.
- `tests/`: unit, numerical, and reference-comparison tests.
- `website/`: static-first public learning interface.
- `.github/workflows/`: automated quality gates.

The curriculum is the source of truth. Avoid maintaining separate copies of lesson text in the website.

## Standard lesson contract
1. Objectives and prerequisites.
2. Intuition and geometry.
3. Definitions, assumptions, notation, and dimensions.
4. Step-by-step derivation and proof where appropriate.
5. Worked examples and counterexamples.
6. NumPy implementation from scratch.
7. Visualization or experiment where useful.
8. Reference-library verification and numerical discussion.
9. Exercises, hints, and mastery rubric.
10. Connection to an ML algorithm or research question.
11. Further reading and attribution.

Clearly distinguish fully derived results, theorems stated with assumptions, and proofs deferred to a cited source. Do not present empirical observations as proofs.

## Mastery model
States: `unstarted`, `learning`, `practiced`, `mastered`. Page views are not evidence of mastery. Suggested rubric: conceptual understanding 20%; derivation/proof 25%; problem solving 20%; implementation and numerical validation 25%; explanation and ML connection 10%. Suggested pass threshold: 80%, plus minimum performance on derivation and implementation. These are defaults to evaluate, not claims of psychometric validity.

Begin with local browser storage and JSON export if progress tracking is needed. Explain data-loss limitations and avoid collecting personal data by default.

## Quality and reproducibility
- Test expected behavior, dimensions, edge cases, and invalid inputs.
- Use justified numerical tolerances and include ill-conditioned cases.
- Check gradients with finite differences and, where appropriate, PyTorch autograd.
- Record versions, seeds, data provenance, commands, metrics, and limitations.
- Run link, curriculum metadata, Python test, and website build checks in CI.
- Do not claim an experiment is reproduced unless the procedure was actually run.

## 12-month mastery-based sequence
| Months | Focus | Evidence |
|---|---|---|
| 1–2 | Foundations and linear algebra | Least-squares derivation, projections, SVD/PCA experiments |
| 3–4 | Calculus and probability | Gradient checks, simulations, estimator derivations |
| 5–6 | Statistics and optimization | Estimation experiments and optimizer benchmarks |
| 7–8 | Information theory and numerical mathematics | Entropy/KL experiments and stability audit |
| 9–10 | Advanced topics | A selected research result reproduced and analyzed |
| 11–12 | Integration and research | Reproducible capstone and public release |

The timeline is a planning guide, not permission to skip a failed mastery gate.

## Release plan
- R0 Foundation: structure, curriculum schema, resource map, lesson standard, setup, first tested implementation.
- R1 Curriculum: diagnostic, domain maps, resource mapping, exemplar lessons across all domains.
- R2 Computational lab: implementations, notebooks, reference comparisons, numerical tests.
- R3 Website: navigation, math rendering, selected interactive visualizations, local progress and JSON export.
- R4 Research: problem sets, mastery rubrics, reproducible reports, benchmarks.
- R5 Public release: accessibility, link audit, contribution docs, deployment, release notes.

## Initial acceptance criteria
A new contributor can install the package and run tests; the roadmap and resources are actionable; at least one lesson demonstrates the theory-to-code workflow; mathematical functions have independent correctness tests; planned features are clearly distinguished from implemented features; sources are attributed.
