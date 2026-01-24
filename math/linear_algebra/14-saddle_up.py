#!/usr/bin/env python3
"""Module for numpy matrix multiplication"""
import numpy as np


def np_matmul(mat1, mat2):
    """
    Performs matrix multiplication

    Args:
        mat1: First numpy.ndarray
        mat2: Second numpy.ndarray

    Returns:
        A new numpy.ndarray that is the product of mat1 and mat2
    """
    return np.matmul(mat1, mat2)
