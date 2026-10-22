#!/usr/bin/env python3
"""The Baum-Welch algorithm for a hidden markov model"""
import numpy as np


def baum_welch(Observations, Transition, Emission, Initial, iterations=1000):
    """Performs the Baum-Welch algorithm for a hidden markov model

    Observations: numpy.ndarray of shape (T,) with the observation indices
    Transition: numpy.ndarray of shape (M, M), initial transition
                probabilities
    Emission: numpy.ndarray of shape (M, N), initial emission probabilities
    Initial: numpy.ndarray of shape (M, 1), initial starting probabilities
    iterations: number of times expectation-maximization is performed

    Returns: the converged Transition, Emission, or None, None on failure
    """
    if not isinstance(Observations, np.ndarray) or Observations.ndim != 1:
        return None, None
    if not isinstance(Emission, np.ndarray) or Emission.ndim != 2:
        return None, None
    M, N = Emission.shape
    if not isinstance(Transition, np.ndarray) or Transition.shape != (M, M):
        return None, None
    if not isinstance(Initial, np.ndarray) or Initial.shape != (M, 1):
        return None, None
    if not isinstance(iterations, int) or iterations <= 0:
        return None, None
    if Observations.size < 2 or Observations.dtype.kind not in 'iu':
        return None, None
    if Observations.min() < 0 or Observations.max() >= N:
        return None, None
    T = Observations.shape[0]
    onehot = (Observations[:, None] == np.arange(N)).astype(float)
    A = Transition.copy()
    E = Emission.copy()
    for _ in range(iterations):
        alpha = np.zeros((M, T))
        beta = np.ones((M, T))
        alpha[:, 0] = Initial[:, 0] * E[:, Observations[0]]
        for t in range(1, T):
            alpha[:, t] = np.matmul(A.T, alpha[:, t - 1]) * \
                E[:, Observations[t]]
        for t in range(T - 2, -1, -1):
            beta[:, t] = np.matmul(
                A, E[:, Observations[t + 1]] * beta[:, t + 1])
        xi = alpha[:, None, :-1] * A[:, :, None] * \
            E[:, Observations[1:]][None] * beta[None, :, 1:]
        xi = xi / np.sum(xi, axis=(0, 1))
        gamma = alpha * beta
        gamma = gamma / np.sum(gamma, axis=0)
        new_A = np.sum(xi, axis=2) / np.sum(gamma[:, :-1], axis=1)[:, None]
        new_E = np.matmul(gamma, onehot) / np.sum(gamma, axis=1)[:, None]
        if np.array_equal(new_A, A) and np.array_equal(new_E, E):
            break
        A, E = new_A, new_E
    return A, E
