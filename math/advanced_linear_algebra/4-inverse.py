#!/usr/bin/env python3
"""Module for calculating the inverse of a matrix."""


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
    """Helper function to calculate minor matrix."""
    n = len(matrix)
    
    if n == 1:
        return [[1]]

    minor_matrix = []
    for i in range(n):
        minor_row = []
        for j in range(n):
            submatrix = []
            for row_idx in range(n):
                if row_idx != i:
                    sub_row = []
                    for col_idx in range(n):
                        if col_idx != j:
                            sub_row.append(matrix[row_idx][col_idx])
                    submatrix.append(sub_row)
            
            minor_row.append(determinant(submatrix))
        minor_matrix.append(minor_row)

    return minor_matrix


def cofactor(matrix):
    """Helper function to calculate cofactor matrix."""
    n = len(matrix)
    minor_matrix = minor(matrix)

    cofactor_matrix = []
    for i in range(n):
        cofactor_row = []
        for j in range(n):
            sign = (-1) ** (i + j)
            cofactor_row.append(sign * minor_matrix[i][j])
        cofactor_matrix.append(cofactor_row)

    return cofactor_matrix


def adjugate(matrix):
    """Helper function to calculate adjugate matrix."""
    n = len(matrix)
    cofactor_matrix = cofactor(matrix)

    adjugate_matrix = []
    for j in range(n):
        adj_row = []
        for i in range(n):
            adj_row.append(cofactor_matrix[i][j])
        adjugate_matrix.append(adj_row)

    return adjugate_matrix


def inverse(matrix):
    """
    Calculates the inverse of a matrix.

    Args:
        matrix: A list of lists whose inverse should be calculated.

    Returns:
        The inverse of matrix, or None if matrix is singular.

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

    # Calculate determinant
    det = determinant(matrix)

    # Check if matrix is singular (determinant = 0)
    if det == 0:
        return None

    # Get adjugate matrix
    adj_matrix = adjugate(matrix)

    # Calculate inverse by dividing adjugate by determinant
    inverse_matrix = []
    for i in range(n):
        inv_row = []
        for j in range(n):
            inv_row.append(adj_matrix[i][j] / det)
        inverse_matrix.append(inv_row)

    return inverse_matrix
