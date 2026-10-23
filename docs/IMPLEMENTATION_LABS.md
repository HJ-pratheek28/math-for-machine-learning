# Implementation Labs: Mathematics You Can Run

These are specifications, not prewritten solutions. Implement each one yourself before looking for a reference implementation. Use Python and NumPy; Matplotlib is useful for visualization. Keep dependencies minimal.

## Lab 1 — Linear transformations
Apply identity, scaling, rotation, shear, and a rank-deficient matrix to a 2D grid. Plot original and transformed points. Predict results before running code. Compare sequential transformations with multiplication by the product matrix. Explain information loss under a rank-deficient map.

**Tests:** identity preserves points; applying identity twice changes nothing; composed transformations agree within tolerance.

## Lab 2 — Projections and geometry
Project vectors onto a line and a column space. Calculate a case by hand, check residual orthogonality, and compare Euclidean distance with cosine similarity.

**Tests:** unit vector, zero vector, parallel and orthogonal vectors, nearly dependent basis vectors.

## Lab 3 — Eigenvalues and SVD
Choose interpretable small matrices. Compute an eigendecomposition where its conditions hold, compute SVD, reconstruct the matrix, and truncate singular values to plot reconstruction error. Explain why eigenvectors and singular vectors are not interchangeable for arbitrary matrices.

**Tests:** reconstruction residual, sorted singular values, rank-deficient matrix, non-symmetric matrix.

## Lab 4 — Gradients and finite differences
Define a smooth scalar-valued function, derive its gradient, approximate partial derivatives with finite differences, and compare at multiple points. Plot contours and gradient arrows.

**Tests:** multiple step sizes, flat regions, stationary point. Explain rounding and approximation error.

## Lab 5 — Probability simulation
Choose tractable random variables. Derive theoretical mean and variance, simulate increasing sample sizes, compare empirical moments with theory, and visualize correlated two-dimensional data.

**Tests:** fixed random seed, small versus large samples, explanation of sampling fluctuations.

## Lab 6 — Gradient descent
Implement gradient descent for a quadratic objective without an optimizer library. Log objective and gradient norm. Compare learning rates and well- versus poorly-conditioned objectives.

**Tests:** known minimizer, stopping criterion, too-small step, too-large step. Explain convergence, oscillation, and divergence.

## Lab 7 — Linear regression from first principles
Generate data with known parameters and controlled noise. Implement least squares using a numerically appropriate solver; avoid explicitly computing a matrix inverse. Implement gradient descent separately and compare coefficients, predictions, residuals, and convergence.

**Tests:** noiseless data, noisy data, redundant features, outliers, held-out evaluation.

## Lab 8 — PCA from first principles
Center data, compute principal directions with SVD, project and reconstruct, plot explained variance and reconstruction error, and compare with a trusted PCA implementation.

**Tests:** verify centering and component orthogonality within tolerance; examine feature scaling.

## Lab 9 — Gaussian mixture model and EM
Generate a two-component dataset. Implement responsibilities in the E-step and parameter updates in the M-step. Track log-likelihood, visualize uncertainty, and repeat with different initializations.

**Tests:** responsibilities sum to one per point, covariance matrices remain valid, unstable local solutions are documented.

## Lab 10 — Linear support vector machine
Visualize a linearly separable 2D dataset. Implement a simple linear margin classifier or its core optimization. Compare the boundary with a trusted SVM and vary regularization.

**Tests:** scaled features, overlapping classes, explanation of what the margin does and does not guarantee.

## Lab engineering standard

Each lab should include:
- **README.md:** question, concepts, run instructions, conclusions.
- **derivation.md:** mathematics in your own words.
- **main.py or notebook:** implementation and plots.
- **tests or assertions:** correctness checks.
- **results:** generated plots or small result summaries, not huge datasets.
- **limitations:** assumptions, numerical issues, and known failure modes.

Make experiments reproducible. State random seeds when relevant, record dependencies, and distinguish theoretical error from floating-point error.

## Final integration project

Combine at least three methods from the book. Report the problem, assumptions, notation, central derivations, from-scratch implementations, tests, independent validation, controlled experiments, failure cases, library comparisons, and evidence-supported conclusions.
