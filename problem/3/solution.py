import sys
from math import isqrt

input = int(sys.argv[1])

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


def is_prime(n: int):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def largest_prime_factor(n: int):
    ceil = isqrt(n)
    for p in range(ceil, 1, -1):
        is_factor = n % p == 0
        if is_factor and is_prime(p):
            return p


print(largest_prime_factor(input))  # 6857
