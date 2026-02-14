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
        n (int): The upper bound of the summation (must be a non-negative int).

    Returns:
        int: The value of the summation if n is valid.
        None: If n is not an integer or is negative.
    """
    if not isinstance(n, int) or n < 0:
        return None
    if n == 0:
        return 0
    return n * n + summation_i_squared(n - 1)
