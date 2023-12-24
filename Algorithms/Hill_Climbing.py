import random
import time
from Functions import calculate_attacking_pairs, generate_board, create_Board


def hill_climbing_algo(n, num_restarts=100):
    best_solution = None
    best_heuristic = float('inf')

    for _ in range(num_restarts):
        current_board = generate_board(n)
        current_heuristic = calculate_attacking_pairs(current_board)

        while current_heuristic > 0:
            next_board = current_board.copy()
            best_moves = []
            best_heuristic = current_heuristic

            for column in range(n):
                for row in range(n):
                    if current_board[column] == row:
                        continue

                    next_board[column] = row
                    next_heuristic = calculate_attacking_pairs(next_board)

                    if next_heuristic < best_heuristic:
                        best_moves = [(column, row)]
                        best_heuristic = next_heuristic
                    elif next_heuristic == best_heuristic:
                        best_moves.append((column, row))

                    next_board[column] = current_board[column]

            if best_heuristic == current_heuristic:
                break

            best_move = random.choice(best_moves)
            current_board[best_move[0]] = best_move[1]
            current_heuristic = best_heuristic

        if current_heuristic == 0:
            return current_board

        if best_heuristic < calculate_attacking_pairs(best_solution):
            best_solution = current_board

    return best_solution


def hill_climbing(n):
    if n > 3:
        start = time.time()
        solution = hill_climbing_algo(n)
        if solution is None:
            print("No solution found.")
        else:
            A = [
                ['Q' if i == row else '-' for i in range(n)]for row in solution]
            end = time.time()
            create_Board(A)
            print("Hill-CLimbing :", end-start)
