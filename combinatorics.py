import math


def stirling(n):
    """
    Compute Stirling approximation for factorial
    http://en.wikipedia.org/wiki/Stirling%27s_approximation
    """
    return math.sqrt(2 * math.pi * n) * (n / math.e) ** n


def nPr_approx(n, r):
    """
    Get an approximation of nPr
    """
    if n > 20:
        return stirling(n) / stirling(n - r)
    else:
        return math.factorial(n) / math.factorial(n - r)


def nCr_approx(n, r):
    """
    Get an approximation of nCr
    """
    if n > 20:
        return stirling(n) / stirling(r) / stirling(n - r)
    else:
        return


def nPr(n, r):
    """
    Get number of permutations
    """
    return math.factorial(n) / math.factorial(n - r)


def nCr(n, r):
    """
    Get number of combinations
    """
    return math.factorial(n) / math.factorial(r) / math.factorial(n - r)