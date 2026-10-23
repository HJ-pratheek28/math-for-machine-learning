# Master Curriculum: One Spine, Deep Mastery

Primary source: [Mathematics for Machine Learning (free official book)](https://mml-book.github.io/).

This is the canonical route through the book. Read it in order. The topic lists below are checkpoints, not substitutes for the text.

## The chapter cycle

For every chapter: (1) read actively, (2) reconstruct definitions from memory, (3) derive key equations and state assumptions, (4) solve exercises without looking at solutions, (5) implement with Python/NumPy, (6) test edge cases and compare against independent checks, (7) explain uses and limitations, and (8) pass the gate in [MASTERY_PROTOCOL.md](MASTERY_PROTOCOL.md).

Do not move on just because a certain number of days passed. A slow, correct pass beats a fast, fragile one.

## Stage 0 — Readiness check

Verify you can manipulate equations and inequalities; work with functions, composition, inverses, exponentials, logarithms and trigonometry; use summation and set notation; rearrange formulas; and track dimensions. Create a diagnostic page with 15 self-generated examples. Repair only the gaps that actually block you; do not postpone the book for months.

## Stage 1 — Chapter 2: Linear Algebra

**Focus:** vectors, matrices, linear systems, vector spaces, and linear maps.

You must explain matrix-vector multiplication as a transformation; check dimensions; solve small systems; reason about span, independence, basis, rank, and null space; and understand what NumPy's linear algebra operations compute.

**Derivation:** show why composition of linear maps becomes matrix multiplication.

**Lab:** transform a 2D grid using identity, scaling, rotation, shear, and a rank-deficient matrix. Predict the result before running code.

**Gate:** explain a matrix as a map and predict a transformation's qualitative effect before verifying it numerically.

## Stage 2 — Chapter 3: Analytic Geometry

**Focus:** inner products, norms, distances, angles, orthogonality, and projections.

You must interpret norms and dot products; derive projection onto a line; explain residual orthogonality in least squares; and distinguish geometric intuition from assumptions specific to Euclidean space.

**Derivation:** minimize squared distance to derive a projection coefficient.

**Lab:** compare Euclidean distance and cosine similarity; visualize projections and residuals.

**Gate:** derive and implement a projection, then explain why the residual is orthogonal.

## Stage 3 — Chapter 4: Matrix Decompositions

**Focus:** eigenvalues/eigenvectors, diagonalization, and SVD.

You must explain invariant directions and scaling; state when diagonalization is valid; understand the role of symmetry; use SVD to reveal directions and scales; and connect rank, low-rank approximation, and PCA.

**Derivation:** work through one small eigendecomposition and one SVD, explaining each factor.

**Lab:** reconstruct a matrix with truncated SVD and plot reconstruction error against rank.

**Gate:** choose between eigendecomposition and SVD for a task, justify the choice, and validate reconstruction numerically.

## Stage 4 — Chapter 5: Vector Calculus

**Focus:** derivatives, partial derivatives, gradients, Jacobians, and the multivariable chain rule.

You must interpret local sensitivity; calculate gradients; understand Jacobian shapes; derive a chain rule for a composition; and validate analytical gradients using finite differences while knowing their limitations.

**Derivation:** derive gradients for a quadratic and a simple composition, annotating dimensions.

**Lab:** plot a 2D loss surface and compare analytical gradients with numerical approximations.

**Gate:** derive a new gradient without a template and pass a finite-difference check.

## Stage 5 — Chapter 6: Probability and Distributions

**Focus:** random variables, distributions, expectation, variance, covariance, conditional probability, and multivariate Gaussian distributions.

You must distinguish PMFs, PDFs, and CDFs; compute simple moments; interpret covariance and correlation; apply conditional probability and Bayes' rule; and distinguish population quantities from sample estimates.

**Derivation:** calculate theoretical moments for a simple discrete random variable and interpret a 2D Gaussian covariance matrix.

**Lab:** simulate random variables and compare empirical and theoretical moments; visualize multivariate Gaussian samples.

**Gate:** solve a new probability problem on paper, simulate it, and explain sampling variability.

## Stage 6 — Chapter 7: Continuous Optimization

**Focus:** objectives, gradients, curvature, stationary points, and iterative optimization.

You must derive gradient-descent updates; explain learning rate, curvature, conditioning, and initialization; interpret the Hessian at the level of the text; and distinguish a stationary point from a proven global minimum.

**Derivation:** derive gradient descent for a quadratic objective and analyze the step size.

**Lab:** implement gradient descent without an optimizer library; compare well- and poorly-conditioned objectives and multiple learning rates.

**Gate:** diagnose a diverging or slow run mathematically and justify a correction.

## Stage 7 — Chapter 8: When Models Meet Data

Create a concept map connecting previous chapters to a learning problem. Describe the data, model, objective, assumptions, and uncertainty. Distinguish mathematical assumptions from assumptions about how data were generated.

**Gate:** explain what can go wrong when assumptions are violated.

## Stage 8 — Chapter 9: Linear Regression

You must write the model, residual vector, and squared-error objective with correct dimensions; derive the normal equations; explain projection onto the column space; implement regression without a high-level estimator; and investigate scaling, collinearity, residuals, and outliers.

**Derivation:** derive least squares and explain residual orthogonality to the design matrix's column space.

**Lab:** compare a direct linear-algebra solution with gradient descent on synthetic data.

**Gate:** validate your implementation independently and explain assumptions and failure cases.

## Stage 9 — Chapter 10: Principal Component Analysis

You must explain centering; connect variance maximization to an eigenvector problem; connect covariance eigendecomposition with SVD; interpret explained variance and reconstruction error; and explain why high variance does not guarantee predictive value.

**Derivation:** derive the first principal-component objective under a unit-norm constraint.

**Lab:** implement PCA with SVD, compare with a library, and plot reconstruction error against retained dimensions.

**Gate:** explain what PCA preserves, what it discards, and why dimensionality is a modeling decision.

## Stage 10 — Chapter 11: Gaussian Mixture Models

You must explain mixture distributions and latent assignments; distinguish the E-step from the M-step; track likelihood; investigate initialization sensitivity; and explain why EM can converge to a local solution.

**Derivation:** annotate the EM cycle and state what is held fixed in each step.

**Lab:** implement a small 1D or 2D Gaussian mixture EM algorithm and visualize responsibilities and likelihood.

**Gate:** diagnose poor initialization or misleading cluster interpretations.

## Stage 11 — Chapter 12: Support Vector Machines

You must explain separating hyperplanes, margins, support vectors, constraints, and regularization; understand the optimization objective in the text; and recognize why an optimal boundary is not necessarily a calibrated probability model.

**Derivation:** interpret the margin objective and constraints symbol by symbol.

**Lab:** implement a simple linear margin classifier or its core optimization and compare against a trusted SVM.

**Gate:** explain the boundary geometrically and the effect of regularization.

## Stage 12 — Synthesis capstone

Build a **Mathematical Model Laboratory** using at least three methods from the book. Include a clear question, assumptions, derivations, from-scratch implementations, numerical tests, controlled experiments, failure cases, and comparison against trusted libraries. Write a report with equations and plots so another reader can reproduce the experiment.

## After the core book: advanced specialization

The book is a foundation, not the endpoint of research mathematics. After every chapter passes its gate, choose a specialization and extend only where the work requires it:

- **Deep learning:** matrix calculus, computational graphs, initialization, normalization, backpropagation, and optimization dynamics.
- **Probabilistic ML:** Bayesian inference, statistical estimation, graphical models, and approximate inference.
- **Theory:** concentration, generalization, statistical learning theory, and optimization theory.
- **Research:** proof-writing, counterexamples, assumptions, and reproducing paper derivations.

Do not add a second main resource before completing this spine. Later, choose one deeper resource for the specialization you actually pursue.
