# Probability

This directory contains the Probability project for the `alu-machine_learning` repository.

## Learning Objectives

At the end of this project, you should be able to explain, without using Google:

- What is a distribution?
- What is a random variable?
- What is a probability mass function (PMF)?
- What is a probability density function (PDF)?
- What is a cumulative distribution function (CDF)?
- What are the most common probability distributions?
- What is the Poisson distribution?

## Contents

### Python Scripts

- `poisson.py`: Contains the `Poisson` class that represents a Poisson distribution.

## Tasks

### 0. Initialize Poisson
Create a class `Poisson` that represents a poisson distribution:

- Class constructor `def __init__(self, data=None, lambtha=1.):`
    - `data` is a list of the data to be used to estimate the distribution
    - `lambtha` is the expected number of occurences in a given time frame
    - Sets the instance attribute `lambtha`
        - Saves `lambtha` as a float
    - If `data` is not given, (i.e. `None`):
        - Use the given `lambtha`
        - If `lambtha` is not a positive value or equals to 0, raise a ValueError with the message `lambtha must be a positive value`
    - If `data` is given:
        - Calculate the `lambtha` of `data`
        - If `data` is not a list, raise a TypeError with the message `data must be a list`
        - If `data` does not contain at least two data points, raise a ValueError with the message `data must contain multiple values`
