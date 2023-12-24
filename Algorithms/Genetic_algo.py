from Functions import calculate_attacking_pairs, generate_board, create_Board
import random
import time


def fitness(board):
    n = len(board)
    # return 28 - calculate_attacking_pairs(board)
    return 1 / (calculate_attacking_pairs(board) + 1)
    # return n * (n - 1) // 2 - calculate_attacking_pairs(board)


def crossover(parent1, parent2):
    n = len(parent1)
    crossover_point = random.randint(1, n - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    return child1


def mutate(board, mutation_rate):
    n = len(board)
    for i in range(n):
        if random.random() < mutation_rate:
            board[i] = random.randint(0, n-1)
    return board


def select_parents(population):
    tournament_size = 20
    selected_parents = random.sample(population, tournament_size)
    selected_parents.sort(key=lambda x: fitness(x), reverse=True)
    parent1 = selected_parents[0]
    parent2 = selected_parents[1]
    return parent1, parent2


def genetic_algorithm(population_size, mutation_rate, n):
    population = [generate_board(n) for _ in range(population_size)]
    generation = 5000

    for _ in range(generation):
        new_population = []
        for _ in range(population_size):
            parent1, parent2 = select_parents(population)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)

        population = new_population
        for board in population:
            if calculate_attacking_pairs(board) == 0:
                return board


def Genetic(n):
    if n > 3:
        start = time.time()
        population_size = 100
        mutation_rate = 0.1
        solution = genetic_algorithm(
            population_size, mutation_rate, n)
        if solution:
            A = [
                ['Q' if i == row else '-' for i in range(n)]for row in solution]
            end = time.time()
            create_Board(A)
            print("Genetic took :", end-start)
        else:
            print("No solution found.")
