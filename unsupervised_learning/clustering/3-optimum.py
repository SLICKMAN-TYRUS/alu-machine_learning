#!/usr/bin/env python3
"""Optimize the number of clusters for K-means"""
import numpy as np
kmeans = __import__('1-kmeans').kmeans
variance = __import__('2-variance').variance


def optimum_k(X, kmin=1, kmax=None, iterations=1000):
    """Tests for the optimum number of clusters by variance

    X: numpy.ndarray of shape (n, d) containing the data set
    kmin: positive integer, minimum number of clusters (inclusive)
    kmax: positive integer, maximum number of clusters (inclusive)
    iterations: positive integer, maximum iterations for K-means

    Returns: results, d_vars or None, None on failure
        results: list of the outputs of K-means for each cluster size
        d_vars: list of the difference in variance from the smallest
                cluster size for each cluster size
    """
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        return None, None
    if kmax is None:
        kmax = X.shape[0]
    if not isinstance(kmin, int) or not isinstance(kmax, int):
        return None, None
    if not isinstance(iterations, int) or iterations <= 0:
        return None, None
    if kmin < 1 or kmax <= kmin or kmax > X.shape[0]:
        return None, None
    results = []
    d_vars = []
    first_var = None
    for k in range(kmin, kmax + 1):
        C, clss = kmeans(X, k, iterations)
        if C is None:
            return None, None
        var = variance(X, C)
        if first_var is None:
            first_var = var
        results.append((C, clss))
        d_vars.append(first_var - var)
    return results, d_vars
