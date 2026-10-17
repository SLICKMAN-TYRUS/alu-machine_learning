#!/usr/bin/env python3
"""Initialize K-means centroids"""
import numpy as np


def initialize(X, k):
    """Initializes cluster centroids for K-means

    X: numpy.ndarray of shape (n, d) containing the dataset
    k: positive integer, the number of clusters

    Returns: numpy.ndarray of shape (k, d) of centroids, or None on failure
    """
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        return None
    if not isinstance(k, int) or k <= 0:
        return None
    low = X.min(axis=0)
    high = X.max(axis=0)
    return np.random.uniform(low, high, size=(k, X.shape[1]))
