""""
Basic Rules:

    Rock beats Scissors.
    Scissors beats Paper.
    Paper beats Rock.

Tie Condition:
    If both the user and the computer choose the same option (e.g., both choose Rock, or both choose Paper), the result is a tie.

Win Conditions:
    If the user’s choice beats the computer’s choice, the user wins.
        Rock beats Scissors → User wins.
        Scissors beats Paper → User wins.
        Paper beats Rock → User wins.

If the computer’s choice beats the user’s choice, the computer wins.
    Scissors beats Rock → Computer wins.
    Paper beats Scissors → Computer wins.
    Rock beats Paper → Computer wins
"""





import tkinter as tk
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == "rock":
        return "You win!" if computer_choice == "scissors" else "Computer wins!"
    elif user_choice == "paper":
        return "You win!" if computer_choice == "rock" else "Computer wins!"
    elif user_choice == "scissors":
        return "You win!" if computer_choice == "paper" else "Computer wins!"

# Function to handle user's choice and compute the result
def user_choice(choice):
    # List of choices
    choices = ["rock", "paper", "scissors"]
    
    # Randomly pick computer's choice
    computer_choice = random.choice(choices)
    
    # Determine the winner
    result = determine_winner(choice, computer_choice)
    
    # Update the labels with choices and result
    user_choice_label.config(text=f"You chose: {choice.capitalize()}")
    computer_choice_label.config(text=f"Computer chose: {computer_choice.capitalize()}")
    result_label.config(text=result)

# Set up the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry("400x300")

# User's choice label
user_choice_label = tk.Label(root, text="You chose:", font=("Arial", 14))
user_choice_label.pack(pady=10)

# Computer's choice label
computer_choice_label = tk.Label(root, text="Computer chose:", font=("Arial", 14))
computer_choice_label.pack(pady=10)

# Result label
result_label = tk.Label(root, text="Let's play!", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

# Create buttons for the user to select rock, paper, or scissors
rock_button = tk.Button(root, text="Rock", font=("Arial", 14), bg="lightblue", width=10, command=lambda: user_choice("rock"))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", font=("Arial", 14), bg="lightgreen", width=10, command=lambda: user_choice("paper"))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", font=("Arial", 14), bg="lightcoral", width=10, command=lambda: user_choice("scissors"))
scissors_button.pack(pady=5)

# Start the application
root.mainloop()
