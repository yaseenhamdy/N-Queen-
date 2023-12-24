import time
from Functions import create_Board


def solve_n_queens(n):
    start = time.time()
    board = [['-'] * n for _ in range(n)]

    def is_safe(board, row, col):
        for i in range(col):
            if board[row][i] == 'Q':
                return False

        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        i, j = row, col
        while i < n and j >= 0:
            if board[i][j] == 'Q':
                return False
            i += 1
            j -= 1

        return True

    def solve_util(board, col):
        if col >= n:
            return True

        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 'Q'

                if solve_util(board, col + 1):
                    return True

                board[i][col] = '-'

        return False

    if not solve_util(board, 0):
        print("No solution exists , Choose a number > 3.")
    else:
        end = time.time()
        create_Board(board)
        print("BackTracking took:", end-start)
