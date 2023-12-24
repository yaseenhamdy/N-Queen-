import tkinter as tk
from tkinter import ttk
from Algorithms.Genetic_algo import Genetic
from Algorithms.Hill_Climbing import hill_climbing
from Algorithms.Back_Tracking import solve_n_queens
from Algorithms.Best_First_Algo import best_first


def create_main_window():
    root = tk.Tk()
    root.title("N-Queens Solver")
    root.resizable(True, True)
    menu_frame = tk.Frame(root, padx=20, pady=20, bg="#F0D9B5")
    menu_frame.pack()

    entry_label = tk.Label(
        menu_frame, text="Select a number:", font=("Arial", 12), bg="#F0D9B5")
    entry_label.grid(row=0, column=0, sticky="e")

    # Create a list of numbers from 4 to 19
    numbers = list(range(4, 20))

    # Create a tkinter variable to hold the selected number
    selected_number = tk.StringVar(root)
    selected_number.set(numbers[0])  # Set the default selected number

    # Create the style for the drop-down menu
    style = ttk.Style()
    style.theme_use('clam')  # Choose a theme for the drop-down menu

    # Create the drop-down menu
    dropdown_menu = ttk.Combobox(menu_frame, textvariable=selected_number, values=numbers, font=("Arial", 12), state="readonly")
    dropdown_menu.grid(row=0, column=1, padx=5)

    button1 = tk.Button(menu_frame, text="Genetic Algorithm", command=lambda: Genetic(int(selected_number.get())), font=(
        "Arial", 12), bg="#8B4513", fg="white", width=20)
    button1.grid(row=1, column=0, pady=(15, 0), padx=(0, 10))

    button2 = tk.Button(menu_frame, text="Hill Climbing Algorithm", command=lambda: hill_climbing(int(selected_number.get())), font=(
        "Arial", 12), bg="#8B4513", fg="white", width=20)
    button2.grid(row=1, column=1, pady=(15, 0))

    button3 = tk.Button(menu_frame, text="Backtracking Algorithm", command=lambda: solve_n_queens(int(selected_number.get())), font=(
        "Arial", 12), bg="#8B4513", fg="white", width=20)
    button3.grid(row=2, column=0, pady=(15, 0), padx=(0, 10))

    button4 = tk.Button(menu_frame, text="Best First Search", command=lambda: best_first(int(selected_number.get())), font=(
        "Arial", 12), bg="#8B4513", fg="white", width=20)
    button4.grid(row=2, column=1, pady=(15, 0))

    root.mainloop()


create_main_window()