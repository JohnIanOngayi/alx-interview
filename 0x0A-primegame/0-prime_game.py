#!/usr/bin/python3

"""
Module uses Sieve of Eratosthenes algorithm to solve prime game problem
"""


def isWinner(x, nums):
    """
    returns winner of prime game

    args:
    x (int): no. of rounds
    nums (int): array of numbers which are upper bound for prime game

    returns:
    (str) Maria | Ben
    """
    if x != len(nums):
        return None

    max_num = max(nums)
    primes = sieveofEratosthenes(max_num)

    maria_wins = 0
    ben_wins = 0

    for num in nums:
        prime_count = sum(1 for p in primes if p <= num)
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    else:
        return "Ben"


def sieveofEratosthenes(n):
    """
    returns list of prime numbers less than or equal to n

    args:
    n (int) number in question

    returns:
    (List[int]) list of prime numbers less than or equal to n
    """
    prime_nums = []

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
