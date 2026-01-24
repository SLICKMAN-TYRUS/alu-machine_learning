#!/usr/bin/env python3
"""Module for array addition"""


def add_arrays(arr1, arr2):
    """
    Adds two arrays element-wise

    Args:
        arr1: First array (list of ints/floats)
        arr2: Second array (list of ints/floats)

    Returns:
        A new list containing the element-wise sum,
        or None if arrays are not the same shape
    """
    if len(arr1) != len(arr2):
        return None
    return [arr1[i] + arr2[i] for i in range(len(arr1))]
