#!/usr/bin/python3

"""
In a text file, there is a single character H.
Your text editor can execute only two operations in this file: Copy All n Paste
Given a number n, write a method that calculates the fewest number of
operations needed to result in exactly n H characters in the file.
"""

from typing import List


def minOperations(n: float) -> int:
    """
    Returns min no. of operations to achieve n 'H' characters in a text file.

    Parameters:
    n (float): The target number of 'H' characters.

    Returns:
    int: The minimum number of operations.
    """
    if n < 1:
        return 0

    return sum(prime_factors(n))


def prime_factors(n: float) -> List[int]:
    """
    Compute the prime factors of a given number.

    Parameters:
    n (float): The number to factorize.

    Returns:
    List[int]: A list of prime factors of the number.
    """
    i: int = 2
    factors: List[int] = []
    while (n != 1):
        if (n % i) == 0:
            n = n / i
            factors.append(i)
        else:
            i += 1
    return factors
