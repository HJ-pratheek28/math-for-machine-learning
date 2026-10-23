import numpy as np
import pytest

from mathml.linear_algebra import least_squares


def test_exactly_solvable_system_returns_solution_and_zero_residual():
    A = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]])
    expected = np.array([2.0, -1.0])
    actual, residual = least_squares(A, A @ expected)
    np.testing.assert_allclose(actual, expected, rtol=1e-12, atol=1e-12)
    assert residual < 1e-12


def test_overdetermined_residual_is_orthogonal_to_column_space():
    A = np.array([[1.0], [1.0], [1.0]])
    b = np.array([1.0, 2.0, 4.0])
    x_hat, _ = least_squares(A, b)
    np.testing.assert_allclose(A.T @ (b - A @ x_hat), [0.0], atol=1e-12)


def test_rank_deficient_matrix_returns_finite_solution():
    A = np.array([[1.0, 2.0], [2.0, 4.0], [3.0, 6.0]])
    x_hat, residual = least_squares(A, np.array([1.0, 2.0, 3.0]))
    assert np.isfinite(x_hat).all()
    assert residual < 1e-12


@pytest.mark.parametrize(
    ("A", "b"),
    [
        (np.array([1.0, 2.0]), np.array([1.0, 2.0])),
        (np.ones((2, 2)), np.ones((2, 1))),
        (np.ones((2, 2)), np.ones(3)),
        (np.empty((0, 2)), np.empty(0)),
        (np.array([[np.nan]]), np.array([1.0])),
    ],
)
def test_invalid_inputs_raise_value_error(A, b):
    with pytest.raises(ValueError):
        least_squares(A, b)
