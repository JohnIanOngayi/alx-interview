#!/usr/bin/python3

"""
Pascal's Triangle
"""


def pascal_triangle(n: int):
    """
    Returns values for the Pascals Triangle
    """
    if n <= 0:
        return []

    result = [[1]]

    # creating rows
    for _ in range(n - 1):
        temp = [0] + result[-1] + [0]
        row = []

        # creating next row
        for j in range(len(result[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        result.append(row)

    return result
