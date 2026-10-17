#!/usr/bin/env python3
"""Expectation Maximization for a GMM"""
import numpy as np
initialize = __import__('4-initialize').initialize
expectation = __import__('6-expectation').expectation
maximization = __import__('7-maximization').maximization


def expectation_maximization(X, k, iterations=1000, tol=1e-5, verbose=False):
    """Performs the expectation maximization for a GMM

    X: numpy.ndarray of shape (n, d) containing the data set
    k: positive integer, the number of clusters
    iterations: positive integer, maximum number of iterations
    tol: non-negative float, tolerance of the log likelihood
    verbose: boolean, whether to print the log likelihood progress

    Returns: pi, m, S, g, l or None, None, None, None, None on failure
        pi: numpy.ndarray of shape (k,) with the priors
        m: numpy.ndarray of shape (k, d) with the centroid means
        S: numpy.ndarray of shape (k, d, d) with the covariances
        g: numpy.ndarray of shape (k, n) with the posteriors
        l: the log likelihood of the model
    """
    fail = (None, None, None, None, None)
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        return fail
    if not isinstance(k, int) or k <= 0 or k > X.shape[0]:
        return fail
    if not isinstance(iterations, int) or iterations <= 0:
        return fail
    if not isinstance(tol, (int, float)) or tol < 0:
        return fail
    if not isinstance(verbose, bool):
        return fail
    pi, m, S = initialize(X, k)
    if pi is None:
        return fail
    l_prev = np.inf
    i = 0
    for i in range(iterations + 1):
        g, ll = expectation(X, pi, m, S)
        if g is None:
            return fail
        if verbose and i % 10 == 0:
            print('Log Likelihood after {} iterations: {}'.format(
                i, round(ll, 5)))
        if i == iterations or abs(ll - l_prev) <= tol:
            break
        pi, m, S = maximization(X, g)
        l_prev = ll
    if verbose and i % 10 != 0:
        print('Log Likelihood after {} iterations: {}'.format(
            i, round(ll, 5)))
    return pi, m, S, g, ll
