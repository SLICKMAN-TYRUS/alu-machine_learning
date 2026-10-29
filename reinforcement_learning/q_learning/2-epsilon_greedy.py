#!/usr/bin/env python3
"""Epsilon greedy action selection"""
import numpy as np


def epsilon_greedy(Q, state, epsilon):
    """Uses epsilon-greedy to determine the next action

    Q: numpy.ndarray containing the q-table
    state: the current state
    epsilon: the epsilon to use for the calculation

    Returns: the next action index
    """
    if np.random.uniform(0, 1) > epsilon:
        return np.argmax(Q[state])
    return np.random.randint(0, Q.shape[1])
