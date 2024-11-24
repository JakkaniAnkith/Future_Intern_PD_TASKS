import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.configure(bg="#ffebcd")  # Background color for the window
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()

    def create_board(self):
        frame = tk.Frame(self.root, bg="#ffebcd")  # Frame to hold the grid
        frame.pack(pady=20)

        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    frame,
                    text="",
                    font=("Arial", 24, "bold"),
                    width=5,
                    height=2,
                    bg="#f0f8ff",  # Light blue background for buttons
                    fg="#333333",  # Default text color
                    activebackground="#add8e6",  # Light blue when hovered
                    command=lambda i=i, j=j: self.make_move(i, j),
                )
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons[i][j] = button

        self.reset_button = tk.Button(
            self.root,
            text="Restart Game",
            font=("Arial", 16, "bold"),
            bg="#90ee90",  # Light green button
            fg="#333333",  # Dark text
            command=self.reset_game,
        )
        self.reset_button.pack(pady=10)

    def make_move(self, i, j):
        if self.board[i][j] == "":
            self.board[i][j] = self.current_player
            color = "#ff4500" if self.current_player == "X" else "#1e90ff"  # Orange for X, Blue for O
            self.buttons[i][j].config(text=self.current_player, fg=color)
            if self.check_win(self.current_player):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
        else:
            messagebox.showwarning("Invalid Move", "Cell already taken! Choose another.")

    def check_win(self, player):
        # Check rows, columns, and diagonals
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or \
               all(self.board[j][i] == player for j in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)) or \
           all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def check_draw(self):
        return all(self.board[i][j] != "" for i in range(3) for j in range(3))

    def reset_game(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="", fg="#333333")  # Reset text and text color


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
