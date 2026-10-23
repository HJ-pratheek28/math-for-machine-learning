# Least Squares: Projection, Derivation, and Numerical Reality

> **Domain:** Linear algebra and geometry · **Difficulty:** Foundation → Intermediate  
> **Prerequisites:** Matrix multiplication, transpose, dot product, orthogonality  
> **Primary reading:** [Mathematics for Machine Learning](https://mml-book.github.io/); supplement with [MIT 18.06](https://math.mit.edu/~gs/linearalgebra/)

## Learning objectives
- Derive the normal equations for least squares.
- Explain least squares as an orthogonal projection.
- Implement least squares with NumPy.
- Explain why explicitly solving the normal equations may be numerically fragile.

## 1. The problem

Let \(A \in \mathbb{R}^{m\times n}\) and \(b \in \mathbb{R}^{m}\). We seek \(x \in \mathbb{R}^{n}\) minimizing the squared Euclidean error:

\[\min_{x\in\mathbb{R}^n} \|Ax-b\|_2^2.\]

When \(b\) is not in the column space of \(A\), an exact solution to \(Ax=b\) may not exist. Least squares finds the closest vector in that column space.

## 2. Derive the normal equations

Define \(f(x)=(Ax-b)^T(Ax-b)\). Expanding,

\[f(x)=x^TA^TAx-2b^TAx+b^Tb.\]

The gradient is

\[\nabla_x f(x)=2A^TAx-2A^Tb.\]

Setting the gradient to zero yields the **normal equations**:

\[A^TAx=A^Tb.\]

If \(A\) has full column rank, \(A^TA\) is positive definite and the minimizer is unique. The symbolic expression \((A^TA)^{-1}A^Tb\) is useful for derivation, but explicitly forming the inverse is not recommended in numerical code.

## 3. Geometric interpretation

At a least-squares solution, residual \(r=b-A\hat{x}\) is orthogonal to every column of \(A\):

\[A^T(b-A\hat{x})=0.\]

Thus \(A\hat{x}\) is the orthogonal projection of \(b\) onto the column space of \(A\).

## 4. NumPy implementation

The function `mathml.linear_algebra.least_squares` uses `numpy.linalg.lstsq`, validates dimensions and finite values, and returns the solution and residual norm. Run `pytest` to reproduce the small correctness examples.

## 5. Numerical investigation

Compare `numpy.linalg.lstsq(A, b, rcond=None)` against solving \(A^TAx=A^Tb\) for well-conditioned matrices and matrices with nearly dependent columns. For full-column-rank \(A\),

\[\kappa_2(A^TA)=\kappa_2(A)^2.\]

Forming \(A^TA\) can therefore worsen numerical sensitivity.

## 6. Exercises
1. Explain why \(A^TA\) is positive definite when \(A\) has full column rank.
2. Show that the residual is orthogonal to the column space.
3. Construct a matrix with nearly dependent columns and compare approaches.
4. Explain why the inverse expression is not the preferred implementation.

## 7. Mastery gate
- [ ] Derive the normal equations without copying.
- [ ] Explain the projection geometry.
- [ ] Implement least squares with a stable solver.
- [ ] Test well-conditioned and ill-conditioned examples.
- [ ] State the rank assumption behind uniqueness.

## Further reading
- [Mathematics for Machine Learning](https://mml-book.github.io/)
- [MIT 18.06 Linear Algebra](https://math.mit.edu/~gs/linearalgebra/)
- [NumPy least-squares documentation](https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html)
