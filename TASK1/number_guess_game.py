import tkinter as tk
from tkinter import messagebox
import random

# Function to initialize or reset the game
def start_game():
    global number_to_guess, attempts
    number_to_guess = random.randint(1, 100)
    attempts = 0
    entry_box.delete(0, tk.END)
    feedback_label.config(text="Guess a number between 1 and 100!")

# Function to process the user's guess
def check_guess():
    global attempts
    try:
        guess = int(entry_box.get())
        attempts += 1

        if guess < 1 or guess > 100:
            feedback_label.config(text="Please guess a number between 1 and 100.")
        elif guess < number_to_guess:
            feedback_label.config(text="Too low! Try again.")
        elif guess > number_to_guess:
            feedback_label.config(text="Too high! Try again.")
        else:
            messagebox.showinfo("Congratulations!", f"You guessed it right in {attempts} attempts!")
            start_game()  # Restart the game
    except ValueError:
        feedback_label.config(text="Invalid input. Please enter a number.")

# Create the main application window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x300")

# Allow the window to be resizable (enable maximize and minimize)
root.resizable(True, True)

# Widgets for the UI
title_label = tk.Label(root, text="Number Guessing Game", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

feedback_label = tk.Label(root, text="Guess a number between 1 and 100!", font=("Arial", 12))
feedback_label.pack(pady=10)

entry_box = tk.Entry(root, font=("Arial", 14), justify="center", width=10)
entry_box.pack(pady=10)

guess_button = tk.Button(root, text="Guess", font=("Arial", 12), bg="lightblue", command=check_guess)
guess_button.pack(pady=5)

reset_button = tk.Button(root, text="Restart Game", font=("Arial", 12), bg="orange", command=start_game)
reset_button.pack(pady=5)

# Initialize the game
start_game()

# Start the application
root.mainloop()
