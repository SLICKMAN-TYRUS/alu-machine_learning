cat << 'EOF' > 17-integrate.py
#!/usr/bin/env python3
"""
Module for computing the integral of a polynomial represented
as a list of coefficients.
"""


def poly_integral(poly, C=0):
    """
    Calculate the integral of a polynomial.

    The polynomial is represented by a list of coefficients "poly"
    where poly[i] is the coefficient of x^i.

    Args:
        poly (list): List of integers or floats representing a polynomial.
        C (int, optional): Constant of integration. Defaults to 0.

    Returns:
        list: New list of coefficients representing the integral.
        None: If poly or C are not valid.
    """
    if not isinstance(poly, list) or len(poly) == 0:
        return None

    for c in poly:
        if not isinstance(c, (int, float)):
            return None

    if not isinstance(C, int):
        return None

    integ = [C]
    i = 0
    while i < len(poly):
        coeff = poly[i] / float(i + 1)
        if coeff.is_integer():
            coeff = int(coeff)
        integ.append(coeff)
        i += 1

    # Trim trailing zeros to keep list as small as possible
    while len(integ) > 1 and integ[-1] == 0:
        integ.pop()

    return integ
EOF
