import heapq
import time
from Functions import calculate_attacking_pairs, create_Board


def is_valid(board, row, col):
    # Check if the current position is under attack
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def best_first_search(n):
    initial_state = ([-1] * n, 0, 0)
    heap = [(calculate_attacking_pairs(initial_state[0]), initial_state)]
    heapq.heapify(heap)

    while heap:
        _, state = heapq.heappop(heap)
        board, row, cost = state[0], state[1], state[2]

        if row == n:
            return board

        for col in range(n):
            if is_valid(board, row, col):
                new_board = list(board)
                new_board[row] = col
                new_state = (new_board, row + 1, cost +
                             abs(col - board[row]) + 1)
                heapq.heappush(
                    heap, (calculate_attacking_pairs(new_state[0]), new_state))

    return None


def best_first(n):
    start = time.time()
    solution = best_first_search(n)
    List = [['Q' if i == row else '-' for i in range(n)]for row in solution]
    end = time.time()
    if solution:
        create_Board(List)
        print("Best-First took :", end-start)
