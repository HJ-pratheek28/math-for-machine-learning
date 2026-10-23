# Optimization — Practice

## By hand
1. Define parameters, objective function and loss function.
2. For `L(w) = (w - 4)^2`, calculate the gradient and one update from `w = 0` with learning rate `0.1`.
3. What happens when the learning rate is extremely small or too large?
4. Explain batch, stochastic and mini-batch gradient descent.
5. What does convexity mean, and why is it useful?
6. At a differentiable local minimum in an unconstrained problem, what condition often holds for the gradient?

## Python
1. Implement gradient descent for `L(w) = (w - 4)^2`.
2. Plot loss against iteration for learning rates `0.01`, `0.1` and `1.1`.
3. Implement linear regression with NumPy and gradient descent.
4. Standardize features and compare convergence.
5. Compare predictions with scikit-learn linear regression.

## ML connection
Why are parameters updated in the negative gradient direction when minimizing a differentiable loss?