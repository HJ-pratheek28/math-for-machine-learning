# Complete Resource Library

This repository deliberately uses **one primary textbook**. Everything else is classified as a prerequisite, an intuition aid, an implementation reference, or an advanced follow-up. Do not turn this into a playlist-collecting exercise.

## 1. Primary resource — complete this first

### Mathematics for Machine Learning

- **Authors:** Marc Peter Deisenroth, A. Aldo Faisal, Cheng Soon Ong.
- **Official site and free book:** https://mml-book.github.io/
- **Role:** the single source of truth for the core curriculum.
- **How to use it:** follow the chapter order in [ROADMAP.md](ROADMAP.md), work the derivations, solve exercises, and complete the matching implementation labs.
- **Core scope:** linear algebra, analytic geometry, matrix decompositions, vector calculus, probability and distributions, continuous optimization, model/data connections, linear regression, PCA, Gaussian mixture models and support vector machines.

Do not replace the book with video summaries. Videos may help you visualize an idea, but the book and your own derivations are the evidence of mastery.

## 2. Prerequisites — use only to repair gaps

These are not parallel primary courses. Open them when a prerequisite blocks progress, then return to the book.

| Gap | Resource | Use it for |
|---|---|---|
| Algebra and functions | [Khan Academy Algebra](https://www.khanacademy.org/math/algebra) | Equations, exponents, logarithms, functions and notation |
| Single-variable calculus | [Khan Academy Calculus 1](https://www.khanacademy.org/math/calculus-1) | Limits, derivatives, chain rule and basic integrals |
| Probability basics | [Khan Academy Statistics and Probability](https://www.khanacademy.org/math/statistics-probability) | Events, conditional probability, expectation and variance |
| Linear algebra intuition | [3Blue1Brown — Essence of Linear Algebra](https://www.3blue1brown.com/topics/linear-algebra) | Visual intuition for vectors, transformations, determinants and eigenvectors |
| Calculus intuition | [3Blue1Brown — Essence of Calculus](https://www.3blue1brown.com/topics/calculus) | Visual intuition for derivatives, integrals and chain rule |

**Rule:** use a supplemental resource to answer a named question, not to avoid the main reading.

## 3. Chapter-to-resource map

| Primary-book topic | Required work | Optional support |
|---|---|---|
| Linear algebra | Vectors, subspaces, rank, null spaces, projections, least squares | 3Blue1Brown linear algebra; [MIT 18.06 Linear Algebra](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/) |
| Analytic geometry | Inner products, norms, distances, hyperplanes and projections | 3Blue1Brown linear algebra |
| Matrix decompositions | Eigenvalues, eigenvectors, SVD and positive semidefinite matrices | MIT 18.06; [Numerical Linear Algebra notes by Stanford](https://web.stanford.edu/~boyd/vmls/) |
| Vector calculus | Partial derivatives, gradients, Jacobians, Hessians and chain rule | 3Blue1Brown calculus; [MIT 18.02SC Multivariable Calculus](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/) |
| Probability and distributions | Conditional probability, expectation, covariance and Gaussian distributions | [Harvard Stat 110](https://stat110.hsites.harvard.edu/) |
| Continuous optimization | Convexity, optimality and gradient descent | [Boyd & Vandenberghe — Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/) |
| Linear regression | Least squares, residuals, objective functions and optimization | Primary book first; use scikit-learn docs only to compare implementation |
| PCA | Covariance, eigenvectors, SVD, variance and reconstruction error | MIT 18.06; [scikit-learn PCA guide](https://scikit-learn.org/stable/modules/decomposition.html#pca) |
| Gaussian mixture models and EM | Likelihood, latent assignments, responsibilities and iterative updates | [scikit-learn Gaussian mixture guide](https://scikit-learn.org/stable/modules/mixture.html) |
| Support vector machines | Hyperplanes, margins, hinge loss and regularization | [scikit-learn SVM guide](https://scikit-learn.org/stable/modules/svm.html) |

## 4. Implementation tools

Use these to test mathematical understanding, not to outsource it.

- **Python:** https://www.python.org/
- **Jupyter:** https://jupyter.org/
- **NumPy:** https://numpy.org/doc/stable/
- **Matplotlib:** https://matplotlib.org/stable/
- **SciPy:** https://docs.scipy.org/doc/scipy/
- **scikit-learn:** https://scikit-learn.org/stable/

Recommended local setup:
- Python 3.11 or 3.12 in an isolated environment.
- JupyterLab or notebooks in VS Code.
- NumPy for vectors, matrices, decompositions and numerical experiments.
- Matplotlib for geometric visualizations and convergence plots.
- SciPy for comparison against trusted numerical routines.
- scikit-learn only as a baseline or verification tool after your own implementation.

Keep a requirements file and a random seed for reproducible experiments. Record library versions for the integration project.

## 5. Advanced references — only after the matching core

These texts are deeper follow-ups, not prerequisites for starting the primary book.

### Numerical linear algebra
- **[Numerical Linear Algebra](https://people.maths.ox.ac.uk/trefethen/text.html)** by Lloyd N. Trefethen and David Bau III.
- Use for numerical stability, conditioning, error, and why mathematically equivalent computations may behave differently on a computer.

### Convex optimization
- **[Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/)** by Stephen Boyd and Lieven Vandenberghe.
- Use for convex sets/functions, duality, KKT conditions, and constrained optimization.

### Statistical learning
- **[The Elements of Statistical Learning](https://hastie.su.domains/ElemStatLearn/)** by Hastie, Tibshirani and Friedman.
- Use after the core to connect mathematical foundations to statistical learning methods, regularization and model assessment.

### Probabilistic machine learning
- **[Probabilistic Machine Learning: An Introduction](https://probml.github.io/pml-book/book1.html)** by Kevin P. Murphy.
- Use for probability-driven modeling, inference and modern probabilistic ML.

### Deep learning
- **[Dive into Deep Learning](https://d2l.ai/)**.
- Use after multivariable calculus, linear algebra and optimization to connect the mathematics to neural networks and practical implementations.

### Information theory
- **[Elements of Information Theory — Wiley](https://www.wiley.com/en-us/Elements+of+Information+Theory%2C+2nd+Edition-p-9780471241959)** by Thomas M. Cover and Joy A. Thomas.
- Use for entropy, KL divergence, mutual information and coding-theoretic foundations.

## 6. What not to do

- Do not study five textbooks simultaneously.
- Do not watch a full course before attempting the relevant chapter.
- Do not memorize formulas without knowing assumptions and dimensions.
- Do not trust a library result until you can state what it computes.
- Do not confuse a successful notebook run with mathematical understanding.
- Do not use advanced references to postpone prerequisites.

## 7. The resource workflow

1. Start with the primary book chapter.
2. Write down the exact concept you do not understand.
3. Consult one support resource for that concept only.
4. Close the support resource and reconstruct the idea yourself.
5. Solve an exercise and implement a numerical check.
6. Record the result in the progress tracker.
7. Return to the primary book.
