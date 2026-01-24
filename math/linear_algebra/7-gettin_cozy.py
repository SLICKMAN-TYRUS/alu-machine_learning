#!/usr/bin/env python3
"""Module for 2D matrix concatenation"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis

    Args:
        mat1: First 2D matrix (list of lists)
        mat2: Second 2D matrix (list of lists)
        axis: Axis along which to concatenate (0=rows, 1=columns)

    Returns:
        A new concatenated matrix, or None if matrices cannot be concatenated
    """
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        return [row[:] for row in mat1] + [row[:] for row in mat2]
    elif axis == 1:
        if len(mat1) != len(mat2):
            return None
        return [mat1[i][:] + mat2[i][:] for i in range(len(mat1))]
    return None
