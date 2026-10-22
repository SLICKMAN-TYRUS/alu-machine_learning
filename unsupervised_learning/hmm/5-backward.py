#!/usr/bin/env python3
"""The backward algorithm for a hidden markov model"""
import numpy as np


def backward(Observation, Emission, Transition, Initial):
    """Performs the backward algorithm for a hidden markov model

    Observation: numpy.ndarray of shape (T,) with the observation indices
    Emission: numpy.ndarray of shape (N, M), emission probabilities
    Transition: numpy.ndarray of shape (N, N), transition probabilities
    Initial: numpy.ndarray of shape (N, 1), starting probabilities

    Returns: P, B or None, None on failure
        P: the likelihood of the observations given the model
        B: numpy.ndarray of shape (N, T) with the backward path probabilities
    """
    if not isinstance(Observation, np.ndarray) or Observation.ndim != 1:
        return None, None
    if not isinstance(Emission, np.ndarray) or Emission.ndim != 2:
        return None, None
    N, M = Emission.shape
    if not isinstance(Transition, np.ndarray) or Transition.shape != (N, N):
        return None, None
    if not isinstance(Initial, np.ndarray) or Initial.shape != (N, 1):
        return None, None
    if Observation.size == 0 or Observation.dtype.kind not in 'iu':
        return None, None
    if Observation.min() < 0 or Observation.max() >= M:
        return None, None
    T = Observation.shape[0]
    B = np.zeros((N, T))
    B[:, -1] = 1
    for t in range(T - 2, -1, -1):
        B[:, t] = np.matmul(
            Transition, Emission[:, Observation[t + 1]] * B[:, t + 1])
    P = np.sum(Initial[:, 0] * Emission[:, Observation[0]] * B[:, 0])
    return P, B
