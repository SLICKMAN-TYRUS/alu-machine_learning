cat << 'EOF' > README.md
# Calculus Project

This directory contains the Calculus project for the `alu-machine_learning` repository.

## Learning Objectives

At the end of this project, you should be able to explain, without using Google:

- Summation and Product notation
- What is a series?
- Common series
- What is a derivative?
- What is the product rule?
- What is the chain rule?
- Common derivative rules
- What is a partial derivative?
- What is an indefinite integral?
- What is a definite integral?
- What is a double integral?

## Contents

### Multiple Choice Tasks

Each of the following files contains the **number of the correct answer** for a multiple choice question:

- `0-sigma_is_for_sum`
- `1-seegma`
- `2-pi_is_for_product`
- `3-pee`
- `4-hello_derivatives`
- `5-log_on_fire`
- `6-voltaire`
- `7-partial_truths`
- `8-all-together`
- `11-integral`
- `12-integral`
- `13-definite`
- `14-definite`
- `15-definite`
- `16-double`

### Python Scripts

These Python files implement calculus-related functions:

- `9-sum_total.py`  
  - Defines `summation_i_squared(n)` which computes  
    \sum_{i=1}^{n} i^2  
    using recursion and no loops.

- `10-matisse.py`  
  - Defines `poly_derivative(poly)` which returns the derivative
    of a polynomial represented as a list of coefficients.

- `17-integrate.py`  
  - Defines `poly_integral(poly, C=0)` which returns the integral
    of a polynomial represented as a list of coefficients, with
    integration constant `C`.

All Python files:

- Use `#!/usr/bin/env python3` as the shebang
- Are compatible with Python 3
- Follow pycodestyle as much as possible
- Include module and function documentation strings

EOF
