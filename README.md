# Math for Machine Learning — Research Lab

<div align="center">

**Understand the mathematics. Implement the algorithms. Investigate the evidence.**

A rigorous, open-source learning system for the mathematics behind machine learning.

[Curriculum](docs/curriculum/roadmap.md) · [Resource map](docs/curriculum/resource-map.md) · [Blueprint](docs/blueprint.md) · [First lesson](curriculum/linear-algebra/least-squares.md)

</div>

## The learning loop

**Intuition → derive → implement → visualize → verify → assess → connect to ML.**

This repository is being developed as a research-lab platform: a structured curriculum, tested Python implementations, executable notebooks, interactive visualizations, problem sets, and reproducible projects. Planned features are tracked honestly in the [blueprint](docs/blueprint.md).

## Seven mathematical domains

| Domain | Central question |
|---|---|
| Linear algebra and geometry | What do projections, eigenvectors, SVD, and low-rank approximations reveal about data? |
| Calculus and matrix calculus | How do derivatives and Jacobians describe changes in model outputs and losses? |
| Probability and statistics | How do we represent uncertainty and estimate parameters? |
| Optimization | Why do training algorithms converge, stall, or diverge? |
| Information theory | How do entropy, cross-entropy, and KL divergence relate to learning objectives? |
| Numerical mathematics | Why can mathematically valid computations fail on real hardware? |
| Advanced topics | How do stochastic processes, kernels, geometry, and high-dimensional statistics extend the toolkit? |

## Start here

1. Read the [curriculum roadmap](docs/curriculum/roadmap.md).
2. Follow the [resource map](docs/curriculum/resource-map.md) instead of resource-hopping.
3. Study the [lesson template](docs/curriculum/lesson-template.md) and the [least-squares lesson](curriculum/linear-algebra/least-squares.md).
4. Install the package and run its tests.
5. Record evidence of mastery, not just completed pages.

## Development

Python 3.10+ is targeted.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
pytest
```

## Current status

This is an incremental build. R0 introduces the product blueprint, curriculum, a first exemplar lesson, a tested mathematical function, CI, and an initial website shell. Not every domain, visualization, assessment, or research project is implemented yet.

## Attribution

External textbooks, courses, and papers remain the property of their authors. This project publishes original explanations, code, experiments, and attributed references—not copied textbook chapters or unlicensed solutions.
