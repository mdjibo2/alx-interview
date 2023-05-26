#!/usr/bin/python3

import sys


def solve_nqueens(n):
    """
    Solves the N queens problem and prints all possible solutions.

    Args:
        n (int): The size of the chessboard and the number of queens.

    Returns:
        None
    """
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solutions = []
    solve_nqueens_util(board, 0, solutions)

    for solution in solutions:
        print_solution(solution)


def solve_nqueens_util(board, col, solutions):
    """
    Recursive utility function to solve the N queens problem.

    Args:
        board (list): List representing the chessboard.
        col (int): Current column being processed.
        solutions (list): List to store the found solutions.

    Returns:
        None
    """
    n = len(board)
    if col >= n:
        solutions.append(board.copy())
        return

    for i in range(n):
        if is_safe(board, i, col):
            board[col] = i
            solve_nqueens_util(board, col + 1, solutions)
            board[col] = -1


def is_safe(board, row, col):
    """
    Checks if it is safe to place a queen at the given position.

    Args:
        board (list): List representing the chessboard.
        row (int): Row index of the position being checked.
        col (int): Column index of the position being checked.

    Returns:
        bool: True if it is safe to place a queen, False otherwise.
    """
    for i in range(col):
        if board[i] == row or board[i] == row - col + i or \
                board[i] == row + col - i:
            return False
    return True


def print_solution(board):
    """
    Prints a single solution of the N queens problem.

    Args:
        board (list): List representing the chessboard.

    Returns:
        None
    """
    n = len(board)
    solution = [[i, board[i]] for i in range(n)]
    print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(N)
