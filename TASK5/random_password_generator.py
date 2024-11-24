import random
import string
import tkinter as tk
from tkinter import messagebox

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Password Generator")
        
        # Set window size
        self.root.geometry("400x450")
        self.root.configure(bg="#f4f4f9")  # Set background color
        
        # UI Elements
        self.create_ui()

    def create_ui(self):
        # Title label
        self.title_label = tk.Label(self.root, text="Random Password Generator", font=("Arial", 16, "bold"), bg="#f4f4f9")
        self.title_label.pack(pady=10)

        # Frame for aligning length entry and checkbox labels
        frame = tk.Frame(self.root, bg="#f4f4f9")
        frame.pack(pady=5)

        # Password Length Label and Entry (Align with conditions)
        self.length_label = tk.Label(frame, text="Password Length:", font=("Arial", 12), bg="#f4f4f9")
        self.length_label.grid(row=0, column=0, padx=10)

        self.length_entry = tk.Entry(frame, font=("Arial", 12), width=10, bd=2)
        self.length_entry.grid(row=0, column=1, padx=10)

        # Character Sets Conditions (Align with password length)
        self.character_sets_label = tk.Label(self.root, text="Include the following:", font=("Arial", 12), bg="#f4f4f9")
        self.character_sets_label.pack(pady=5)

        self.uppercase_var = tk.BooleanVar()
        self.lowercase_var = tk.BooleanVar()
        self.numbers_var = tk.BooleanVar()
        self.special_char_var = tk.BooleanVar()

        # Checkbox options
        self.uppercase_check = tk.Checkbutton(self.root, text="Uppercase Letters", variable=self.uppercase_var, font=("Arial", 10), bg="#f4f4f9", activebackground="#f4f4f9")
        self.uppercase_check.pack(anchor="w", padx=520)

        self.lowercase_check = tk.Checkbutton(self.root, text="Lowercase Letters", variable=self.lowercase_var, font=("Arial", 10), bg="#f4f4f9", activebackground="#f4f4f9")
        self.lowercase_check.pack(anchor="w", padx=520)

        self.numbers_check = tk.Checkbutton(self.root, text="Numbers", variable=self.numbers_var, font=("Arial", 10), bg="#f4f4f9", activebackground="#f4f4f9")
        self.numbers_check.pack(anchor="w", padx=520)

        self.special_char_check = tk.Checkbutton(self.root, text="Special Characters", variable=self.special_char_var, font=("Arial", 10), bg="#f4f4f9", activebackground="#f4f4f9")
        self.special_char_check.pack(anchor="w", padx=520)

        # Generate Button
        self.generate_btn = tk.Button(self.root, text="Generate Password", command=self.generate_password, bg="#4CAF50", fg="white", font=("Arial", 12), width=20, bd=2)
        self.generate_btn.pack(pady=20)

        # Display Generated Password
        self.result_label = tk.Label(self.root, text="Generated Password:", font=("Arial", 12), bg="#f4f4f9")
        self.result_label.pack()

        self.password_label = tk.Label(self.root, text="", font=("Arial", 14, "bold"), bg="#f4f4f9", fg="#ff5733")  # Color updated for visibility
        self.password_label.pack(pady=5)

    def generate_password(self):
        # Get user inputs
        try:
            length = int(self.length_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for password length.")
            return

        # Validate length
        if length < 8:
            messagebox.showerror("Invalid Length", "Password length should be at least 8 characters for security.")
            return

        # Define character sets
        characters = ""
        if self.uppercase_var.get():
            characters += string.ascii_uppercase
        if self.lowercase_var.get():
            characters += string.ascii_lowercase
        if self.numbers_var.get():
            characters += string.digits
        if self.special_char_var.get():
            characters += string.punctuation

        # Ensure at least one character set is selected
        if not characters:
            messagebox.showerror("Invalid Selection", "Please select at least one type of character.")
            return

        # Generate a random password
        password = ''.join(random.choice(characters) for _ in range(length))

        # Display the password
        self.password_label.config(text=password)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
