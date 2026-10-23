# Linear Algebra — Practice

## By hand
1. Compute the dot product of `a = [2, -1, 3]` and `b = [4, 0, -2]`.
2. For `A = [[1, 2], [3, 4]]` and `B = [[2, 0], [1, 2]]`, calculate `AB` and `BA`. Are they equal?
3. Solve `2x + y = 5`, `x - y = 1`.
4. Explain linear independence, span and basis.
5. What does a zero dot product mean geometrically?
6. Find eigenvalues and eigenvectors of `A = [[2, 0], [0, 3]]`.
7. What does SVD decompose a matrix into?

## Python / NumPy
1. Calculate a dot product using Python and `numpy.dot`.
2. Implement matrix multiplication with loops and compare with `A @ B`.
3. Calculate the rank and eigenvalues of a small matrix.
4. Transform 2D points with a matrix and plot before/after.
5. Use `numpy.linalg.svd` and reconstruct a matrix.

## ML connection
A dense neural-network layer is `y = Wx + b`. State the shapes of `W`, `x`, `b`, and `y` for 4 input features and 3 output units.