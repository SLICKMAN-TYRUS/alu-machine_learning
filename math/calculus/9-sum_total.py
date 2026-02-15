#!/usr/bin/env python3
"""
Module for computing the summation of i^2 from i = 1 to n
without using loops.
"""


def summation_i_squared(n):
    """
    Compute the sum of squares from 1 to n, that is:
    sum_{i=1}^{n} i^2.

    Args:
        n (int): The upper bound of the summation (must be a positive int).

    Returns:
        int: The value of the summation if n is valid.
        None: If n is not a valid positive integer.
    """
    if type(n) is not int or n < 1:
        return None
    return n * (n + 1) * (2 * n + 1) // 6
