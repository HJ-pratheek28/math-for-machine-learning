<div align="center">

# Mathematics for Machine Learning — Mastery Track

**One textbook. One rigorous path. Derive it. Code it. Test it. Explain it.**

[Start Here](docs/MASTER_CURRICULUM.md) · [Mastery Protocol](docs/MASTERY_PROTOCOL.md) · [Implementation Labs](docs/IMPLEMENTATION_LABS.md) · [Progress Tracker](docs/PROGRESS.md)

</div>

## The mission

This is a long-form training system for building the mathematical foundations required to understand, implement, debug, and eventually research machine-learning methods. This is **not** a list of courses to collect or a 12-week speedrun. The objective is durable competence: explain assumptions, derive equations, implement the method, test its limits, and connect the mathematics to model behavior.

## The one-resource rule

Your primary spine is the free textbook **[Mathematics for Machine Learning (MML)](https://mml-book.github.io/)** by Marc Peter Deisenroth, A. Aldo Faisal, and Cheng Soon Ong.

Read the book in order, including its ML application chapters. Use the [master curriculum](docs/MASTER_CURRICULUM.md) to turn each chapter into a cycle of reading, derivation, exercises, implementation, and a mastery gate.

- Do not switch textbooks whenever a topic feels difficult.
- Do not mistake watching an explanation for learning the mathematics.
- Use this repository's notes, exercises, and code to make the book active.
- If a prerequisite gap blocks progress, repair that specific gap, then return to the book.
- Advanced specialist resources belong after the core spine, not beside it as competing primary courses.

## The learning loop

**LEARN → RECONSTRUCT → DERIVE → SOLVE → IMPLEMENT → TEST → EXPLAIN**

A chapter is complete only when you can do the work without copying a solution. See the [mastery protocol](docs/MASTERY_PROTOCOL.md) for pass criteria and review rules.

## Curriculum map

| Stage | MML chapters | Capability you must earn |
|---|---|---|
| 0. Readiness | Targeted prerequisite repair | Algebra, functions, logarithms, summation, and notation no longer block the main text |
| 1. Linear algebra | 2 | Reason about vectors, matrices, linear systems, rank, and linear transformations |
| 2. Analytic geometry | 3 | Interpret norms, distances, angles, projections, and similarity |
| 3. Matrix decompositions | 4 | Understand eigenvalues, eigendecomposition, and SVD |
| 4. Vector calculus | 5 | Derive partial derivatives, gradients, Jacobians, and chain-rule computations |
| 5. Probability | 6 | Reason about distributions, expectation, covariance, and conditional probability |
| 6. Optimization | 7 | Analyze objectives, gradients, curvature, and numerical optimization |
| 7. Models meet data | 8 | Connect data, assumptions, models, and inference |
| 8. Linear regression | 9 | Derive and implement regression and diagnose errors |
| 9. Dimensionality reduction | 10 | Derive PCA and explain its geometry and limitations |
| 10. Latent-variable models | 11 | Understand Gaussian mixture models and EM |
| 11. Margin-based learning | 12 | Explain and implement support vector machines |
| 12. Integration | All relevant chapters | Build a mathematical ML portfolio and defend your decisions |

## What makes this advanced

Every important topic is studied through four lenses:

1. **Mathematical:** definitions, assumptions, derivations, dimensions, proofs or proof sketches.
2. **Computational:** a from-scratch implementation, numerical checks, and comparison against a reference implementation.
3. **Experimental:** controlled tests, visualizations, edge cases, and explanations of observed behavior.
4. **Machine learning:** the model or training behavior the mathematics explains, including limitations.

The curriculum is mastery-based, not calendar-based. Expect a substantial long-term commitment; do not rush just to mark boxes complete.

## Start today

1. Open the [master curriculum](docs/MASTER_CURRICULUM.md).
2. Begin with Chapter 2 of the textbook if prerequisites are comfortable; otherwise repair only the specific gaps listed in Stage 0.
3. Solve exercises on paper before coding.
4. Keep a derivation log, an error log, and a small Python/NumPy lab for each chapter.
5. Use the mastery gate before moving on.

**Definition of success:** you can derive, implement, test, and clearly explain the core mathematics behind the methods in this book—and you know what you still do not understand.

Educational project. The textbook remains authoritative for its content; this repository provides a study system and implementation workflow.
