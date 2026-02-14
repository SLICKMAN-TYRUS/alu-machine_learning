cat << 'EOF' > 10-matisse.py
#!/usr/bin/env python3
"""
Module for computing the derivative of a polynomial represented
as a list of coefficients.
"""


def poly_derivative(poly):
    """
    Calculate the derivative of a polynomial.

    The polynomial is represented by a list of coefficients "poly"
    where poly[i] is the coefficient of x^i.

    Args:
        poly (list): List of integers or floats representing a polynomial.

    Returns:
        list: New list of coefficients representing the derivative.
        None: If poly is not valid.
    """
    if (not isinstance(poly, list)) or len(poly) == 0:
        return None

    for c in poly:
        if not isinstance(c, (int, float)):
            return None

    if len(poly) == 1:
        return [0]

    deriv = []
    i = 1
    while i < len(poly):
        deriv.append(i * poly[i])
        i += 1

    all_zero = True
    for c in deriv:
        if c != 0:
            all_zero = False
            break
    if all_zero:
        return [0]

    return deriv
EOF
