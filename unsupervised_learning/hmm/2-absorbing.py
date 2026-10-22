#!/usr/bin/env python3
"""Absorbing markov chain"""
import numpy as np


def absorbing(P):
    """Determines if a markov chain is absorbing

    P: square 2D numpy.ndarray of shape (n, n), the transition matrix

    Returns: True if it is absorbing, or False on failure
    """
    if not isinstance(P, np.ndarray) or P.ndim != 2:
        return False
    n = P.shape[0]
    if P.shape != (n, n) or np.any(P < 0):
        return False
    if not np.allclose(np.sum(P, axis=1), 1):
        return False
    stuck = np.diagonal(P) == 1
    if not np.any(stuck):
        return False
    reach = ((P > 0) | np.eye(n, dtype=bool)).astype(float)
    for _ in range(n):
        reach = (np.matmul(reach, reach) > 0).astype(float)
    return bool(np.all(np.any(reach[:, stuck] > 0, axis=1)))
