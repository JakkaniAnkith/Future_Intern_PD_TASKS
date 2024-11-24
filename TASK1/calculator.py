import tkinter as tk
from tkinter import messagebox

# Function to handle button presses
def press(key):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + key)

# Function to clear the input field
def clear():
    entry.delete(0, tk.END)

# Function to evaluate the entered expression
def calculate():
    try:
        # Evaluate the mathematical expression
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero is not allowed.")
    except Exception as e:
        messagebox.showerror("Error", "Invalid input.")

# Create the main application window
root = tk.Tk()
root.title("CALCULATOR")
root.geometry("300x400")

# Center the window on the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 300
window_height = 400
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

# Entry widget for input and displaying results
entry = tk.Entry(root, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=10, padx=10, pady=10)

# Define button layout and their corresponding actions
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('.', 4, 2), ('+', 4, 3),
    ('=', 5, 0)
]

# Create buttons dynamically and add them to the grid
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, width=34, height=2, bg="lightblue", fg="black",
                        font=("Arial", 12), command=calculate)
        btn.grid(row=row, column=col, columnspan=4, padx=5, pady=5)
    elif text == 'C':
        btn = tk.Button(root, text=text, width=8, height=2, bg="red", fg="white",
                        font=("Arial", 12), command=clear)
        btn.grid(row=row, column=col, padx=5, pady=5)
    else:
        btn = tk.Button(root, text=text, width=8, height=2, bg="lightgray", fg="black",
                        font=("Arial", 12), command=lambda t=text: press(t))
        btn.grid(row=row, column=col, padx=5, pady=5)

# Start the application
root.mainloop()
