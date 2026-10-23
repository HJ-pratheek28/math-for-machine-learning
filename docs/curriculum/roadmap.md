# Curriculum Roadmap

This is a 12-month target with mastery gates. Extend the schedule when prerequisites or assessments require it.

## Stage 0 — Readiness diagnostic
Review algebra, functions, logarithms, exponentials, trigonometry, single-variable derivatives and integrals, summation notation, basic proof language, Python functions, NumPy arrays/shapes, plotting, and tests.

**Gate:** solve representative algebra/calculus problems and write a small NumPy function with tests. Route gaps to targeted remediation.

## Stage 1 — Linear algebra and geometry (months 1–2)
Vectors and linear maps; span, independence, basis, dimension, rank and null space; orthogonality, projections and least squares; determinants and eigenvectors; symmetric and positive-definite matrices; eigendecomposition, SVD, low-rank approximation, conditioning and PCA.

**Lab:** compare normal equations, QR, and SVD on well- and ill-conditioned systems. **Gate:** derive least squares, explain projection geometry, and interpret an SVD/PCA experiment.

## Stage 2 — Calculus and matrix calculus (months 3–4)
Limits and Taylor approximations; partial derivatives, gradients and directional derivatives; Jacobians, Hessians and chain rule; derivatives of linear/quadratic forms; vector-Jacobian and Jacobian-vector products; finite differences and automatic differentiation.

**Lab:** compare analytical gradients with finite differences and PyTorch.

## Stage 3 — Probability and statistics (months 3–5)
Conditional probability and Bayes' rule; random variables and distributions; expectation, variance and covariance; transformations and multivariate Gaussian; LLN and CLT; likelihood, MLE, MAP, bias, variance, MSE, confidence intervals, hypothesis tests and Bayesian inference.

**Lab:** simulate estimators and compare empirical bias/variance with theory.

## Stage 4 — Optimization (months 5–6)
Convex sets/functions; smoothness and strong convexity; gradient descent, SGD and momentum; Newton and quasi-Newton methods; constraints, Lagrange multipliers, KKT conditions and duality; regularization, conditioning and convergence diagnostics.

**Lab:** compare optimizers across objectives with different curvature and conditioning.

## Stage 5 — Information theory (month 7)
Self-information, entropy, conditional entropy, cross-entropy, KL divergence, mutual information, and connections to classification losses and probabilistic modeling.

## Stage 6 — Numerical mathematics (month 8)
Floating-point representation; rounding, cancellation, overflow and underflow; conditioning versus stability; stable least squares and iterative methods; finite-difference error; tolerances and reproducible computation.

## Stage 7 — Advanced tools (months 9–10)
Select according to ML goals: stochastic processes and Markov chains; measure-theoretic probability foundations; concentration inequalities and high-dimensional statistics; kernels and Gaussian processes; geometry of data; causal inference fundamentals; deeper matrix calculus and gradient flow.

**Lab:** reproduce a selected result and state assumptions, baselines, and limitations.

## Stage 8 — Integration and research (months 11–12)
Complete a project combining at least three domains; compare implementations to reference libraries; run ablations and sensitivity analysis; document reproducibility and limitations; publish a report.

**Final gate:** another learner can reproduce the main result and explain the mathematics.

For every topic, record prerequisite status, primary reading, derivation evidence, problem-set result, implementation/test link, ML connection, and review date. A watched video or executed notebook alone is not mastery.
