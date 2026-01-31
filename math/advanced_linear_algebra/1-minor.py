#!/usr/bin/env python3
"""Module for calculating the minor matrix of a matrix."""


def determinant(matrix):
    """Helper function to calculate determinant."""
    n = len(matrix)
    
    if n == 1:
        return matrix[0][0]
    
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    for j in range(n):
        minor = []
        for i in range(1, n):
            minor_row = []
            for k in range(n):
                if k != j:
                    minor_row.append(matrix[i][k])
            minor.append(minor_row)
        cofactor = ((-1) ** j) * matrix[0][j]
        det += cofactor * determinant(minor)
    
    return det


def minor(matrix):
    """
    Calculates the minor matrix of a matrix.

    Args:
        matrix: A list of lists whose minor matrix should be calculated.

    Returns:
        The minor matrix of matrix.

    Raises:
        TypeError: If matrix is not a list of lists.
        ValueError: If matrix is not square or is empty.
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")

    if len(matrix) == 0 or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    # Check if matrix is empty or non-square
    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    # Special case: 1x1 matrix
    if n == 1:
        return [[1]]

    # Calculate minor matrix
    minor_matrix = []
    for i in range(n):
        minor_row = []
        for j in range(n):
            # Create submatrix by removing row i and column j
            submatrix = []
            for row_idx in range(n):
                if row_idx != i:
                    sub_row = []
                    for col_idx in range(n):
                        if col_idx != j:
                            sub_row.append(matrix[row_idx][col_idx])
                    submatrix.append(sub_row)
            
            # Calculate determinant of submatrix
            minor_row.append(determinant(submatrix))
        minor_matrix.append(minor_row)

    return minor_matrix
