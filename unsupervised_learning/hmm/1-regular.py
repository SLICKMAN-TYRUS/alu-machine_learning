#!/usr/bin/env python3
"""Steady state of a regular markov chain"""
import numpy as np


def regular(P):
    """Determines the steady state probabilities of a regular markov chain

    P: square 2D numpy.ndarray of shape (n, n), the transition matrix

    Returns: numpy.ndarray of shape (1, n) with the steady state
             probabilities, or None on failure
    """
    if not isinstance(P, np.ndarray) or P.ndim != 2:
        return None
    n = P.shape[0]
    if P.shape != (n, n) or np.any(P < 0):
        return None
    if not np.allclose(np.sum(P, axis=1), 1):
        return None
    adj = (P > 0).astype(float)
    power = adj.copy()
    for _ in range((n - 1) ** 2):
        power = (np.matmul(power, adj) > 0).astype(float)
    if not np.all(power > 0):
        return None
    vals, vecs = np.linalg.eig(P.T)
    v = np.real(vecs[:, np.argmin(np.abs(vals - 1))])
    return (v / np.sum(v)).reshape(1, n)
