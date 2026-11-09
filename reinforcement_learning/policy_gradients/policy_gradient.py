#!/usr/bin/env python3
"""Monte-Carlo policy gradient (REINFORCE) helpers"""
import numpy as np


def policy(matrix, weight):
    """Computes the softmax policy: probability of each action

    matrix: state matrix of shape (1, n_features)
    weight: weight matrix of shape (n_features, n_actions)
    Returns: matrix of action probabilities
    """
    z = matrix.dot(weight)
    e = np.exp(z - np.max(z))
    return e / e.sum()


def policy_gradient(state, weight):
    """Computes the Monte-Carlo policy gradient

    state: current observation of shape (1, n_features)
    weight: weight matrix of shape (n_features, n_actions)
    Returns: the sampled action and the gradient of log-policy
    """
    probs = policy(state, weight)
    action = np.random.choice(probs.shape[1], p=probs[0])
    s = probs.reshape(-1, 1)
    jacobian = np.diagflat(s) - s.dot(s.T)
    dlog = jacobian[action] / probs[0, action]
    grad = state.T.dot(dlog[None, :])
    return action, grad
