import random
import tkinter as tk
from tkinter import PhotoImage


def generate_board(n):
    board = []
    for _ in range(n):
        row = random.randint(0, n-1)
        board.append(row)
    return board


def calculate_attacking_pairs(board):
    if board is None:
        return 0  # Return 0 if board is None

    n = len(board)
    attacking_pairs = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                attacking_pairs += 1
    return attacking_pairs


def create_Board(board):
    board_window = tk.Toplevel()
    board_window.title("Board")
    board_window.geometry("500x500")

    for i in range(len(board)):
        board_window.columnconfigure(i, weight=1, minsize=1)
        board_window.rowconfigure(i, weight=1, minsize=1)
        for j in range(len(board)):
            if (i + j) % 2 == 0:
                bg_color = "#8B4513"  # Brown squares
            else:
                bg_color = "#F0D9B5"  # Light brown squares
            label = tk.Label(
                board_window,
                text=board[i][j],
                width=1,
                height=1,
                relief="solid",
                bg=bg_color,
                font=("Arial", 12, "bold"),
                bd=0
            )
            if board[i][j] == 'Q':
                try:
                    img = PhotoImage(
                        file="crown.png")
                    label.config(image=img)
                    label.image = img
                except tk.TclError as e:
                    print(f"Error loading image: {e}")

            label.grid(row=i, column=j, padx=0, pady=0, sticky="nsew")

    board_window.mainloop()
