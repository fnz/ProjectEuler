import math
import random


def gen_primes():
    """
    Generate an infinite sequence of prime numbers.
    """
    d = {}
    q = 2

    while True:
        if q not in d:
            yield q
            d[q * q] = [q]
        else:
            for p in d[q]:
                d.setdefault(p + q, []).append(p)
            del d[q]

        q += 1


def is_prime(n):
    """
    Check if n is a prime using a probability check followed by deterministic check
    """
    if not is_prime_candidate_fermat(n, 5):
        return False

    return is_prime_brute(n)


def is_prime_brute(n):
    """
    Check if n is a prime number with a deterministic approach
    """
    if n == 1:
        return False
    return all(n % i for i in range(2, int(math.sqrt(n) + 1)))


def is_prime_candidate_fermat(n, t):
    """
    Check if x is probably a prime
    """
    if n == 1:
        return False

    for time in range(t):
        m = random.randint(2, n) - 1

        if pow(m, n - 1, n) != 1:
            return False

    return True