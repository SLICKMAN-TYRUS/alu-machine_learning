#!/usr/bin/env python3
"""Module for matrix transpose operation"""


def matrix_transpose(matrix):
    """
    Returns the transpose of a 2D matrix

    Args:
        matrix: A 2D matrix (list of lists)

    Returns:
        A new matrix that is the transpose of the input matrix
    """
    return [[matrix[row][col] for row in range(len(matrix))]
            for col in range(len(matrix[0]))]
