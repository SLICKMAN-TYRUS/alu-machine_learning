#!/usr/bin/env python3
"""Module for 2D matrix addition"""


def add_matrices2D(mat1, mat2):
    """
    Adds two 2D matrices element-wise

    Args:
        mat1: First 2D matrix (list of lists of ints/floats)
        mat2: Second 2D matrix (list of lists of ints/floats)

    Returns:
        A new matrix containing the element-wise sum,
        or None if matrices are not the same shape
    """
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None
    return [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))]
            for i in range(len(mat1))]
