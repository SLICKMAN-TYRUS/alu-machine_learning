#!/usr/bin/env python3
"""Module for determining the definiteness of a matrix."""
import numpy as np


def definiteness(matrix):
    """
    Calculates the definiteness of a matrix.

    Args:
        matrix: A numpy.ndarray of shape (n, n) whose definiteness
                should be calculated.

    Returns:
        A string indicating the definiteness: "Positive definite",
        "Positive semi-definite", "Negative semi-definite",
        "Negative definite", or "Indefinite".
        Returns None if the matrix is not valid.

    Raises:
        TypeError: If matrix is not a numpy.ndarray.
    """
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    # Check if matrix is valid (square and not empty)
    if matrix.size == 0:
        return None

    if len(matrix.shape) != 2:
        return None

    n, m = matrix.shape
    if n != m:
        return None

    # Check if matrix is symmetric
    if not np.allclose(matrix, matrix.T):
        return None

    # Calculate eigenvalues
    try:
        eigenvalues = np.linalg.eigvals(matrix)
    except Exception:
        return None

    # Check eigenvalues with a small tolerance for numerical errors
    tolerance = 1e-10

    positive = np.all(eigenvalues > tolerance)
    negative = np.all(eigenvalues < -tolerance)
    non_negative = np.all(eigenvalues > -tolerance)
    non_positive = np.all(eigenvalues < tolerance)

    if positive:
        return "Positive definite"
    elif non_negative:
        return "Positive semi-definite"
    elif negative:
        return "Negative definite"
    elif non_positive:
        return "Negative semi-definite"
    else:
        return "Indefinite"
