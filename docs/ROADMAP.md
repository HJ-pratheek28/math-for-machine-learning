# 12-Week Roadmap

Designed for roughly 1–2 hours per day. For each topic, build intuition, derive key equations, solve problems, and implement a small example.

## Weeks 1–2: Linear Algebra
- [ ] Vectors, dot products, norms
- [ ] Matrices, matrix multiplication, transpose, inverse
- [ ] Linear systems, span, basis, dimension, rank
- [ ] Linear independence, orthogonality, projections
- [ ] Eigenvalues, eigenvectors, singular value decomposition (SVD)
- [ ] Least squares and PCA connections
Resources: [3Blue1Brown](https://www.3blue1brown.com/topics/linear-algebra) · [MIT 18.06](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/) · [MML book](https://mml-book.github.io/)
**Exit check:** explain matrix-vector multiplication geometrically; inspect rank and eigenvalues with NumPy.

## Weeks 3–4: Calculus
- [ ] Functions, limits, derivatives and differentiation rules
- [ ] Chain rule; exponential and logarithmic derivatives
- [ ] Partial derivatives, gradients and directional derivatives
- [ ] Jacobian and Hessian intuition
- [ ] Integration as accumulation
- [ ] Chain rule in backpropagation
Resources: [3Blue1Brown](https://www.3blue1brown.com/topics/calculus) · [MIT 18.01](https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/) · [MIT 18.02SC](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/)
**Exit check:** derive a gradient for a two-variable function and compare with finite differences.

## Weeks 5–7: Probability and Statistics
- [ ] Sample spaces, events, conditional probability, Bayes' theorem
- [ ] Independence; random variables; PMF, PDF, CDF
- [ ] Expectation, variance, covariance, correlation
- [ ] Bernoulli, binomial, normal and other common distributions
- [ ] Joint and conditional distributions
- [ ] Sampling, law of large numbers, central limit theorem
- [ ] Point estimation, bias, variance, MSE, maximum likelihood
- [ ] Confidence intervals and hypothesis-testing basics
Resources: [Seeing Theory](https://seeing-theory.brown.edu/) · [Harvard Statistics 110](https://stat110.hsites.harvard.edu/) · [MIT 18.05](https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/)
**Exit check:** simulate a distribution and explain bias–variance trade-offs.

## Weeks 8–9: Optimization
- [ ] Objective and loss functions
- [ ] Gradient descent, learning rate and convergence
- [ ] Batch, stochastic and mini-batch gradient descent
- [ ] Convexity, momentum, Adam
- [ ] Regularization and constrained optimization basics
Resources: [MML book](https://mml-book.github.io/) · [Dive into Deep Learning](https://d2l.ai/) · [Stanford CS229](https://cs229.stanford.edu/)
**Exit check:** implement gradient descent for linear regression and plot loss by iteration.

## Week 10: Discrete Mathematics
- [ ] Logic, predicates, quantifiers, sets, functions and relations
- [ ] Direct proof and mathematical induction
- [ ] Permutations, combinations, graphs and recurrence relations
Resource: [MIT 6.042J](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/)
**Exit check:** solve counting problems and represent a graph with an adjacency list.

## Week 11: Consolidation
- [ ] Review weak linear algebra and calculus concepts
- [ ] Solve mixed probability and statistics problems
- [ ] Derive least-squares objective
- [ ] Implement linear regression with NumPy and compare with scikit-learn

## Week 12: Information Theory and Integration
- [ ] Self-information, entropy, cross-entropy, KL divergence
- [ ] Information gain and mutual information intuition
- [ ] Implement logistic regression and binary cross-entropy
- [ ] Compare NumPy implementation with scikit-learn
- [ ] Write a report covering math, assumptions, results and limitations
Resources: [Dive into Deep Learning](https://d2l.ai/) · [MML book](https://mml-book.github.io/)

## After the 12 weeks
Continue with matrix decompositions, statistical inference, numerical optimization, Bayesian methods, and neural-network mathematics as projects require. This roadmap is a foundation, not research-level mastery.