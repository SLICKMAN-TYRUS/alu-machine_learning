#!/usr/bin/env python3
"""
Binomial distribution
"""


class Binomial:
    """
    Represents a binomial distribution
    """
    def __init__(self, data=None, n=1, p=0.5):
        """
        Initialize the Binomial distribution
        """
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            mean = sum(data) / len(data)
            variance = sum([(x - mean) ** 2 for x in data]) / len(data)
            p = 1 - (variance / mean)
            self.n = int(round(mean / p))
            self.p = float(mean / self.n)

    def pmf(self, k):
        """
        Calculates the value of the PMF for a given number of "successes"
        """
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0

        n_fact = 1
        k_fact = 1
        n_k_fact = 1

        for i in range(1, self.n + 1):
            n_fact *= i
        for i in range(1, k + 1):
            k_fact *= i
        for i in range(1, self.n - k + 1):
            n_k_fact *= i

        n_choose_k = n_fact / (k_fact * n_k_fact)

        return n_choose_k * (self.p ** k) * ((1 - self.p) ** (self.n - k))

    def cdf(self, k):
        """
        Calculates the value of the CDF for a given number of "successes"
        """
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0

        cdf_val = 0
        for i in range(k + 1):
            cdf_val += self.pmf(i)
        return cdf_val
