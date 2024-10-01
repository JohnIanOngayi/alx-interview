#!/usr/bin/python3

"""makechange solution"""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """
    function calculates minno.of coins to make change for total
    args:
        coins (int) - available denominations to make change with
        total (int) - amount to be broken down

    returns:
        (int) no of coins if total is met
                else -1 if total is not met or total == 0
    """
    if total == 0:
        return -1
    change = [total + 1] * (total + 1)
    change[0] = 0

    for amount in range(1, total + 1):
        for coin in coins:
            if amount - coin >= 0:
                change[amount] = min(change[amount], 1 + change[amount - coin])

    return change[total] if change[total] != (total + 1) else -1
