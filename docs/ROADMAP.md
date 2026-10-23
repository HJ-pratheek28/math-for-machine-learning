# Complete Roadmap: Mathematics for Machine Learning

This is a mastery curriculum, not a calendar challenge. Follow the primary book in order, prove that you understand each idea, implement it, and only then advance. A stage may take days or weeks depending on your background.

## The governing rule

**Primary spine:** [Mathematics for Machine Learning](https://mml-book.github.io/) by Marc Peter Deisenroth, A. Aldo Faisal, and Cheng Soon Ong.

Read the relevant chapter carefully, work through derivations with the book closed, solve exercises, implement the core ideas in NumPy, and explain the result in plain language. Supplementary resources are for clarification or advanced extension; they do not replace the spine.

## How to use each stage

For every chapter:

1. **Preview:** list unfamiliar terms and write what problem the chapter is trying to solve.
2. **Read actively:** derive equations by hand; do not merely highlight them.
3. **Reconstruct:** close the book and reproduce the central derivations from memory.
4. **Exercise:** solve representative end-of-chapter problems without looking at solutions first.
5. **Implement:** build a small NumPy experiment that demonstrates the mathematics.
6. **Explain:** write a short note connecting assumptions, equations, geometry, and ML use.
7. **Pass the gate:** score yourself using [MASTERY_PROTOCOL.md](MASTERY_PROTOCOL.md). Revisit weak dimensions before moving on.

## Stage 0 — Readiness and mathematical fluency

**Goal:** remove basic algebra and notation friction before the main text.

Study:
- Fractions, powers, roots, logarithms, exponent rules, rearranging equations.
- Functions, graphs, composition, inverse functions, exponentials and logarithms.
- Summation notation, products, indices, absolute values, inequalities.
- Systems of linear equations and elementary matrix notation.
- Derivatives of basic functions and the chain rule.
- Basic probability: events, conditional probability, expectation, variance.

Use only the sections you need:
- [Khan Academy — Algebra](https://www.khanacademy.org/math/algebra)
- [Khan Academy — Calculus 1](https://www.khanacademy.org/math/calculus-1)
- [Khan Academy — Statistics and probability](https://www.khanacademy.org/math/statistics-probability)

**Gate:** manipulate equations, interpret summations, differentiate simple functions, and calculate elementary probabilities without repeatedly searching for basic rules.

## Stage 1 — Chapter 1: Introduction and the ML viewpoint

**Goal:** understand why the mathematics is organized around data, models, and learning.

Tasks:
- Identify the mathematical objects in a simple ML problem: data, parameters, objective, constraints, and predictions.
- Explain the difference between a model assumption, an optimization procedure, and an evaluation metric.
- Keep a glossary of notation used throughout the book.

**Deliverable:** one page explaining how linear regression turns data into a fitted model.

**Gate:** describe an ML problem as a mathematical mapping from assumptions and data to a model, without confusing the model with the algorithm used to fit it.

## Stage 2 — Chapter 2: Linear Algebra

**Goal:** treat vectors and matrices as mathematical objects, not just arrays of numbers.

Master:
- Scalars, vectors, matrices, tensors and their shapes.
- Linear combinations, span, linear independence, bases and dimension.
- Matrix-vector and matrix-matrix multiplication as composition of linear maps.
- Identity, inverse, transpose, rank, null space, column space and row space.
- Systems of linear equations and the geometry of their solution sets.
- Orthogonality, inner products, norms, distances and projections.
- Gram-Schmidt and orthonormal bases where covered.

Derive:
- Why matrix multiplication represents composition.
- Why a projection onto a unit vector has the familiar inner-product form.
- How rank, null space, and the number of independent directions relate.

Implement:
- Vector operations and matrix multiplication with loops, then verify against NumPy.
- Projection onto a line and onto a subspace.
- Least-squares solution for an overdetermined system.

**Gate:** given a matrix, explain its dimensions, rank, null space, column space, and geometric action; solve a small least-squares problem and interpret the residual.

## Stage 3 — Chapter 3: Analytic Geometry

**Goal:** connect algebraic formulas to geometry and distance.

Master:
- Inner products, norms, angles and orthogonality.
- Distances and geometric interpretations of vectors.
- Hyperplanes and affine sets.
- Projections and geometric relationships between points, vectors and subspaces.

Derive:
- The relationship between dot product and angle.
- Why projection minimizes squared distance to a subspace.
- How a hyperplane can be represented by a normal vector and offset.

Implement:
- Plot vectors, projections, distances and hyperplanes in 2D.
- Compare a point's distance to a line with the residual after projection.

**Gate:** turn a geometric statement into an equation and explain the geometric meaning of the equation.

## Stage 4 — Chapter 4: Matrix Decompositions

**Goal:** understand the structure hidden inside matrices.

Master:
- Determinant and trace as useful matrix properties.
- Eigenvalues, eigenvectors and diagonalization.
- Symmetric matrices and orthogonal eigenvectors.
- Singular value decomposition (SVD).
- Positive definite and positive semidefinite matrices.
- How decompositions expose dominant directions and numerical structure.

Derive:
- The eigenvector equation and its geometric interpretation.
- Why SVD works for rectangular matrices.
- The relationship between singular values and rank.
- Why positive semidefinite matrices produce nonnegative quadratic forms.

Implement:
- Compare eigendecomposition and SVD on suitable matrices.
- Reconstruct a matrix from its SVD.
- Plot low-rank approximations and reconstruction error.

**Gate:** choose a suitable decomposition for a problem, interpret its components, and explain why an arbitrary rectangular matrix does not necessarily have an ordinary eigendecomposition.

## Stage 5 — Chapter 5: Vector Calculus

**Goal:** calculate how multivariable functions change.

Master:
- Scalar-valued and vector-valued functions.
- Partial derivatives and directional derivatives.
- Gradient and its geometric meaning.
- Jacobian and Hessian.
- Chain rule for composed functions.
- Taylor approximation and local behavior.
- Derivatives of common scalar, vector and matrix expressions used in ML.

Derive:
- Why the gradient points in the direction of steepest local increase under the Euclidean norm.
- The multivariable chain rule.
- Gradients for squared error and a simple linear model.

Implement:
- Compare analytical gradients with finite-difference approximations.
- Plot a 2D function and its gradient field.
- Record gradient-check errors for several parameter values.

**Gate:** derive the gradient of a small differentiable model and verify it numerically; explain the roles of gradient, Jacobian and Hessian.

## Stage 6 — Chapter 6: Probability and Distributions

**Goal:** model uncertainty and reason from data.

Master:
- Sample spaces, events, random variables and distributions.
- Discrete and continuous probability distributions.
- Conditional probability, independence and Bayes' rule.
- Expectation, variance and covariance.
- Joint, marginal and conditional distributions.
- Gaussian and multivariate Gaussian distributions.
- Covariance matrices and correlation.
- Common distributional assumptions and their limits.

Derive:
- Expectation and variance for simple distributions.
- Bayes' rule from conditional probability.
- Mean and covariance interpretations for multivariate data.
- The role of covariance in the shape of a Gaussian.

Implement:
- Simulate random variables and compare empirical and theoretical moments.
- Visualize univariate and bivariate Gaussian samples.
- Demonstrate correlation without confusing it with causation.

**Gate:** calculate conditional probabilities, expectations and covariance for small examples; explain what a multivariate Gaussian's mean and covariance encode.

## Stage 7 — Chapter 7: Continuous Optimization

**Goal:** understand how learning algorithms choose parameters.

Master:
- Objective functions, constraints and feasible regions.
- Local and global optima.
- Convex sets and convex functions.
- First- and second-order conditions.
- Gradient descent and step-size effects.
- Lagrange multipliers and constrained optimization where covered.
- Conditioning, curvature and the role of Hessians.

Derive:
- The gradient-descent update from a local first-order approximation.
- The first-order optimality condition for an unconstrained differentiable objective.
- Why convexity matters for global optimality.

Implement:
- Gradient descent on a one-dimensional and a two-dimensional function.
- Compare learning rates and plot convergence.
- Compare gradient descent with a numerical optimizer on a convex objective.

**Gate:** explain when a stationary point is not necessarily a minimum, diagnose divergence from a poor learning rate, and state what convexity does and does not guarantee.

## Stage 8 — Chapter 8: When Models Meet Data

**Goal:** connect the preceding mathematics into a learning workflow.

Tasks:
- Distinguish model family, parameters, loss/objective, fitting algorithm and generalization.
- Identify where linear algebra, probability and optimization enter a real pipeline.
- Write down assumptions before choosing an algorithm.
- Separate training performance from performance on unseen data.

**Deliverable:** a short mathematical specification of one prediction problem: data representation, model, objective, fitting method, assumptions and evaluation plan.

**Gate:** justify each mathematical component rather than listing techniques by name.

## Stage 9 — Chapter 9: Linear Regression

**Goal:** understand regression from geometry through optimization.

Master:
- Linear model and design matrix.
- Squared-error objective and residuals.
- Least squares and normal equations.
- Geometric projection interpretation.
- Conditions for uniqueness and the role of rank.
- Gradient-based fitting and feature scaling.
- Training error, validation error and limitations of the model.

Derive:
- The least-squares objective in vector form.
- The normal equations.
- The gradient of squared error.
- Why the least-squares solution is a projection when the relevant conditions hold.

Implement:
- Fit a line using a closed-form method and gradient descent.
- Compare predictions, residuals and objective curves.
- Test the effect of collinear features and feature scaling.

**Gate:** derive and implement linear regression, explain its assumptions, and compare a closed-form solution with iterative optimization.

## Stage 10 — Chapter 10: Dimensionality Reduction with PCA

**Goal:** understand dimensionality reduction as a variance and reconstruction problem.

Master:
- Centering and scaling.
- Covariance matrix.
- Principal directions and eigenvectors.
- Explained variance.
- Projection to a lower-dimensional space.
- Reconstruction and information loss.
- Relationship between PCA, SVD and low-rank approximation.

Derive:
- Why maximizing projected variance leads to an eigenvector problem.
- Why the leading principal components capture the greatest variance among orthogonal directions.
- How reconstruction error changes with the number of components.

Implement:
- PCA from covariance eigendecomposition and from SVD.
- Plot a 2D dataset before and after projection.
- Plot explained variance and reconstruction error versus component count.

**Gate:** explain what PCA preserves, what it discards, why centering matters, and why high variance is not automatically equivalent to predictive usefulness.

## Stage 11 — Chapter 11: Density Estimation with Gaussian Mixture Models

**Goal:** model data as a mixture of latent subpopulations.

Master:
- Density estimation and mixture distributions.
- Latent component assignments.
- Gaussian mixture model parameters.
- Likelihood and log-likelihood.
- Expectation-Maximization (EM): E-step and M-step.
- Initialization, convergence and local optima.
- Difference between clustering and density estimation.

Derive:
- The mixture likelihood.
- The responsibility formula conceptually and algebraically.
- Why EM alternates between estimating latent assignments and updating parameters.

Implement:
- Generate synthetic data from a mixture of Gaussians.
- Implement a small EM algorithm and plot log-likelihood per iteration.
- Explore initialization sensitivity and compare with a library implementation.

**Gate:** explain the latent-variable problem, describe each EM step, and identify why EM may converge to a poor local solution.

## Stage 12 — Chapter 12: Classification with Support Vector Machines

**Goal:** connect geometry, margins and constrained optimization to classification.

Master:
- Linear decision boundaries.
- Separating hyperplanes and margins.
- Hard-margin versus soft-margin intuition.
- Hinge loss and regularization.
- Support vectors.
- Constrained optimization and the role of the penalty parameter.
- Kernel idea at a conceptual level, if included in the edition you use.

Derive:
- How the signed distance to a hyperplane relates to its normal vector.
- Why maximizing the margin leads to a norm-minimization objective under suitable constraints.
- The effect of regularization and margin violations.

Implement:
- Visualize a separating hyperplane and margin.
- Fit a linear SVM to a toy dataset.
- Change the regularization parameter and inspect the decision boundary.

**Gate:** explain the margin geometrically, interpret support vectors, and describe the trade-off between a wider margin and training violations.

## Stage 13 — Integration project

Build a compact, reproducible mathematical ML notebook. Choose a real or synthetic dataset and:

1. State the problem and assumptions.
2. Inspect and represent the data using vectors and matrices.
3. Analyze summary statistics and covariance.
4. Fit a baseline linear model.
5. implement gradient descent and check its gradient numerically.
6. Apply PCA if dimensionality or visualization warrants it.
7. Compare against one appropriate probabilistic or margin-based model.
8. Evaluate with a clearly justified metric and a held-out split.
9. Discuss failure modes, numerical issues, and what the mathematics cannot establish.
10. Write a report that a peer can reproduce.

**Final gate:** you can defend the assumptions, derive the core equations, reproduce the implementation, interpret the results, and explain failure cases without relying on a tutorial.

## Stage 14 — Advanced extensions (after the primary book)

Do these only after completing the relevant core chapters:
- **Numerical linear algebra:** conditioning, stability, iterative solvers and floating-point error.
- **Convex optimization:** KKT conditions, duality and constrained optimization.
- **Statistical learning:** bias-variance, regularization, generalization, empirical risk minimization.
- **Information theory:** entropy, cross-entropy, KL divergence and mutual information.
- **Deep learning mathematics:** computational graphs, backpropagation, initialization, normalization and optimization dynamics.
- **Bayesian methods:** priors, posteriors, MAP estimation and uncertainty.
- **Probabilistic graphical models:** factorization, conditional independence and inference.
- **Advanced matrix methods:** low-rank methods, randomized SVD and matrix calculus.

Suggested next texts are listed in [RESOURCES.md](RESOURCES.md). Do not jump between all of them at once.

## Weekly operating rhythm (flexible)

Use this cycle rather than a rigid deadline:
- 3 sessions: reading and hand derivations.
- 2 sessions: exercises and proof reconstruction.
- 1 session: NumPy implementation and plots.
- 1 session: closed-book review, error log and explanation.

Short on time? Reduce the number of exercises, not the standard of understanding. Never advance solely because a week has ended.

## Completion definition

You have completed this roadmap when:
- Every core chapter has passed its mastery gate.
- Every implementation lab is reproducible.
- You can explain the main ideas without copying the book.
- The integration project contains derivations, experiments, evaluation and limitations.
- Your progress tracker records evidence, not just time spent.
