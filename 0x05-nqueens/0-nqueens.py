#!/usr/bin/python3

"""Module solves the n queens problem"""

import sys


def is_safe(board, r, c, N):
    """Check the column on the left side"""
    for i in range(r):
        if board[i] == c or board[i] - i == c - r or board[i] + i == c + r:
            return False
    return True


def solve_nqueens(N):
    def solve(board, r):
        if r == N:
            # Once we have valid configuration, print it in the desired format
            print([[i, board[i]] for i in range(N)])
        else:
            for c in range(N):
                if is_safe(board, r, c, N):
                    board[r] = c
                    solve(board, r + 1)

    # Start with an empty board (represented by a list of -1)
    board = [-1] * N
    solve(board, 0)


if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Validate that N is an integer
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Validate that N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N-Queens puzzle
    solve_nqueens(N)
