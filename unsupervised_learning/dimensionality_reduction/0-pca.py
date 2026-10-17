#!/usr/bin/env python3
"""PCA that keeps a fraction of the variance"""
import numpy as np


def pca(X, var=0.95):
    """Performs PCA on a dataset

    X: numpy.ndarray of shape (n, d) with zero mean across all data points
    var: fraction of the variance that the PCA transformation should keep

    Returns: the weights matrix W, numpy.ndarray of shape (d, nd), where
             nd is the new dimensionality of the transformed X
    """
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        return None
    if not isinstance(var, (int, float)) or not 0 < var <= 1:
        return None
    _, s, Vt = np.linalg.svd(X, full_matrices=False)
    ratio = np.cumsum(s) / np.sum(s)
    nd = np.searchsorted(ratio, var) + 1
    return Vt[:nd].T
