#!/usr/bin/env python3
"""PDF of a multivariate Gaussian distribution"""
import numpy as np


def pdf(X, m, S):
    """Calculates the probability density function of a Gaussian

    X: numpy.ndarray of shape (n, d) with the points to evaluate
    m: numpy.ndarray of shape (d,) with the mean of the distribution
    S: numpy.ndarray of shape (d, d) with the covariance

    Returns: P, numpy.ndarray of shape (n,) with the PDF values
             (minimum value 1e-300), or None on failure
    """
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        return None
    if not isinstance(m, np.ndarray) or m.shape != (X.shape[1],):
        return None
    if not isinstance(S, np.ndarray) or S.shape != (X.shape[1],) * 2:
        return None
    d = X.shape[1]
    diff = X - m
    inv = np.linalg.inv(S)
    det = np.linalg.det(S)
    expo = -0.5 * np.sum(np.matmul(diff, inv) * diff, axis=1)
    P = np.exp(expo) / np.sqrt(((2 * np.pi) ** d) * det)
    return np.maximum(P, 1e-300)
