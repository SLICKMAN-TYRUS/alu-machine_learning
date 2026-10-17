#!/usr/bin/env python3
"""Find the best number of clusters for a GMM using BIC"""
import numpy as np
expectation_maximization = __import__('8-EM').expectation_maximization


def BIC(X, kmin=1, kmax=None, iterations=1000, tol=1e-5, verbose=False):
    """Finds the best number of clusters for a GMM using the BIC

    X: numpy.ndarray of shape (n, d) containing the data set
    kmin: positive integer, minimum number of clusters (inclusive)
    kmax: positive integer, maximum number of clusters (inclusive)
    iterations: positive integer, maximum iterations for EM
    tol: non-negative float, tolerance for EM
    verbose: boolean, whether EM prints information

    Returns: best_k, best_result, l, b or None, None, None, None on failure
        best_k: best value for k based on its BIC
        best_result: tuple (pi, m, S) for the best number of clusters
        l: numpy.ndarray of shape (kmax - kmin + 1) of log likelihoods
        b: numpy.ndarray of shape (kmax - kmin + 1) of BIC values
    """
    fail = (None, None, None, None)
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        return fail
    n, d = X.shape
    if kmax is None:
        kmax = n
    if not isinstance(kmin, int) or not isinstance(kmax, int):
        return fail
    if kmin < 1 or kmax <= kmin or kmax > n:
        return fail
    if not isinstance(iterations, int) or iterations <= 0:
        return fail
    if not isinstance(tol, (int, float)) or tol < 0:
        return fail
    if not isinstance(verbose, bool):
        return fail
    size = kmax - kmin + 1
    logl = np.zeros(size)
    b = np.zeros(size)
    best_k = None
    best_result = None
    best_b = np.inf
    for idx in range(size):
        k = kmin + idx
        pi, m, S, _, ll = expectation_maximization(
            X, k, iterations, tol, verbose)
        if pi is None:
            return fail
        p = k * d + k * d * (d + 1) / 2 + k - 1
        logl[idx] = ll
        b[idx] = p * np.log(n) - 2 * ll
        if b[idx] < best_b:
            best_b = b[idx]
            best_k = k
            best_result = (pi, m, S)
    return best_k, best_result, logl, b
