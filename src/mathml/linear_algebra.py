"""Foundational linear-algebra routines with explicit validation."""

from __future__ import annotations

import numpy as np
from numpy.typing import ArrayLike, NDArray

FloatArray = NDArray[np.float64]


def least_squares(A: ArrayLike, b: ArrayLike) -> tuple[FloatArray, float]:
    """Return the least-squares solution and residual 2-norm.

    Uses numpy.linalg.lstsq rather than explicitly inverting A.T @ A.
    """
    matrix = np.asarray(A, dtype=np.float64)
    target = np.asarray(b, dtype=np.float64)
    if matrix.ndim != 2:
        raise ValueError("A must be a two-dimensional matrix")
    if target.ndim != 1:
        raise ValueError("b must be a one-dimensional vector")
    if matrix.shape[0] != target.shape[0]:
        raise ValueError("A and b must have matching row dimensions")
    if matrix.shape[0] == 0 or matrix.shape[1] == 0:
        raise ValueError("A must have at least one row and one column")
    if not np.isfinite(matrix).all() or not np.isfinite(target).all():
        raise ValueError("A and b must contain only finite values")
    x_hat, _, _, _ = np.linalg.lstsq(matrix, target, rcond=None)
    residual_norm = float(np.linalg.norm(matrix @ x_hat - target, ord=2))
    return np.asarray(x_hat, dtype=np.float64), residual_norm
