#!/usr/bin/python3

"""
Module uses Sieve of Eratosthenes algorithm to solve prime game problem
"""

from typing import List


def isWinner(x: int, nums: List[int]) -> str:
    """
    returns winner of prime game

    args:
    x (int): no. of rounds
    nums (int): array of numbers which are upper bound for prime game

    returns:
    (str) Maria | Ben
    """
    maria_wins: int = 0
    ben_wins: int = 0

    if x != len(nums):
        return "Error: no. of elements in nums should be equal to x"

    for _ in range(x):
        # if no. of prime numbers is odd, Maria wins
        if len(sieveofEratosthenes(nums[_])) % 2:
            maria_wins = maria_wins + 1
        else:
            ben_wins = ben_wins + 1
    return "Maria" if maria_wins > ben_wins else "Ben"


def sieveofEratosthenes(n: int) -> List[int]:
    """
    returns list of prime numbers less than or equal to n

    args:
    n (int) number in question

    returns:
    (List[int]) list of prime numbers less than or equal to n
    """
    prime_nums: List[int] = []

    if n < 2:
        return prime_nums

    prime = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:

        # If prime[p] is not
        # changed, then it is a prime
        if prime[p] is True:

            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    # Print all prime numbers
    for p in range(2, n + 1):
        if prime[p]:
            prime_nums.append(p)

    return prime_nums
