#!/usr/bin/env python3
"""Markov chain state probabilities"""
import numpy as np


def markov_chain(P, s, t=1):
    """Determines the probability of a markov chain being in a particular
    state after a specified number of iterations

    P: square 2D numpy.ndarray of shape (n, n), the transition matrix
    s: numpy.ndarray of shape (1, n), probability of starting in each state
    t: number of iterations that the markov chain has been through

    Returns: numpy.ndarray of shape (1, n) with the probability of being in
             each state after t iterations, or None on failure
    """
    if not isinstance(P, np.ndarray) or P.ndim != 2:
        return None
    n = P.shape[0]
    if P.shape != (n, n):
        return None
    if not isinstance(s, np.ndarray) or s.shape != (1, n):
        return None
    if not isinstance(t, int) or t < 0:
        return None
    return np.matmul(s, np.linalg.matrix_power(P, t))
