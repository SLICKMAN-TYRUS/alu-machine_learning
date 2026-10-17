#!/usr/bin/env python3
"""Agglomerative clustering with Ward linkage"""
import scipy.cluster.hierarchy
import matplotlib.pyplot as plt


def agglomerative(X, dist):
    """Performs agglomerative clustering on a dataset

    X: numpy.ndarray of shape (n, d) containing the dataset
    dist: the maximum cophenetic distance for all clusters

    Displays the dendrogram with each cluster in a different color.

    Returns: clss, numpy.ndarray of shape (n,) with the cluster indices
    """
    hierarchy = scipy.cluster.hierarchy
    link = hierarchy.linkage(X, method='ward')
    clss = hierarchy.fcluster(link, t=dist, criterion='distance')
    plt.figure()
    hierarchy.dendrogram(link, color_threshold=dist)
    plt.show()
    return clss
