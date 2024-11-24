import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.root.geometry("600x500")  # Increased height for score display
        self.root.configure(bg="black")

        # Game Configuration
        self.width = 600
        self.height = 400
        self.cell_size = 20
        self.snake = [(100, 100)]  # Initial snake position
        self.food = None
        self.direction = "Right"
        self.running = False  # Game starts in a paused state
        self.score = 0
        self.best_score = 0

        # UI Controls
        self.create_ui_controls()

        # Canvas
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height, bg="black")
        self.canvas.pack()

        # Initialize game elements
        self.create_food()
        self.root.bind("<KeyPress>", self.change_direction)

        # To store the after() loop ID
        self.game_loop_id = None  

    def create_ui_controls(self):
        controls_frame = tk.Frame(self.root, bg="black")
        controls_frame.pack(side=tk.TOP, fill=tk.X)

        start_btn = tk.Button(
            controls_frame,
            text="Start",
            bg="lightgreen",
            font=("Arial", 10),
            command=self.start_game
        )
        start_btn.pack(side=tk.LEFT, padx=5, pady=5)

        stop_btn = tk.Button(
            controls_frame,
            text="Stop",
            bg="red",
            font=("Arial", 10),
            command=self.stop_game
        )
        stop_btn.pack(side=tk.LEFT, padx=5, pady=5)

        resume_btn = tk.Button(
            controls_frame,
            text="Resume",
            bg="lightblue",
            font=("Arial", 10),
            command=self.resume_game
        )
        resume_btn.pack(side=tk.LEFT, padx=5, pady=5)

        restart_btn = tk.Button(
            controls_frame,
            text="Restart",
            bg="orange",
            font=("Arial", 10),
            command=self.restart_game
        )
        restart_btn.pack(side=tk.LEFT, padx=5, pady=5)

        # Score and Best Score Labels
        self.score_label = tk.Label(self.root, text=f"Score: {self.score}", fg="white", bg="black", font=("Arial", 14))
        self.score_label.pack(side=tk.LEFT, padx=10)

        self.best_score_label = tk.Label(self.root, text=f"Best Score: {self.best_score}", fg="gold", bg="black", font=("Arial", 14))
        self.best_score_label.pack(side=tk.RIGHT, padx=10)

    def start_game(self):
        if not self.running:
            self.running = True
            self.run_game()

    def stop_game(self):
        self.running = False

    def resume_game(self):
        if not self.running:
            self.running = True
            self.run_game()

    def restart_game(self):
        # Stop the current game loop if it exists
        if self.game_loop_id:
            self.root.after_cancel(self.game_loop_id)

        # Reset game state
        self.running = False
        self.snake = [(100, 100)]  # Reset snake to initial position
        self.direction = "Right"  # Reset direction
        self.score = 0  # Reset score
        self.update_score()  # Update score display
        self.create_food()  # Generate new food
        self.canvas.delete("all")  # Clear the canvas
        self.start_game()  # Restart the game

    def create_food(self):
        while True:
            x = random.randint(0, (self.width // self.cell_size) - 1) * self.cell_size
            y = random.randint(0, (self.height // self.cell_size) - 1) * self.cell_size
            if (x, y) not in self.snake:
                self.food = (x, y)
                break

    def draw_snake(self):
        self.canvas.delete("snake")
        for segment in self.snake:
            self.canvas.create_rectangle(
                segment[0], segment[1],
                segment[0] + self.cell_size, segment[1] + self.cell_size,
                fill="lime", tag="snake"
            )

    def draw_food(self):
        self.canvas.delete("food")
        self.canvas.create_oval(
            self.food[0], self.food[1],
            self.food[0] + self.cell_size, self.food[1] + self.cell_size,
            fill="red", tag="food"
        )

    def move_snake(self):
        if not self.running:
            return

        head_x, head_y = self.snake[-1]

        if self.direction == "Up":
            head_y -= self.cell_size
        elif self.direction == "Down":
            head_y += self.cell_size
        elif self.direction == "Left":
            head_x -= self.cell_size
        elif self.direction == "Right":
            head_x += self.cell_size

        # Check collisions
        if (
            head_x < 0 or head_x >= self.width or
            head_y < 0 or head_y >= self.height or
            (head_x, head_y) in self.snake
        ):
            self.game_over()
            return

        # Add new head to the snake
        self.snake.append((head_x, head_y))

        # Check if food is eaten
        if (head_x, head_y) == self.food:
            self.score += 10  # Increase score by 10
            self.update_score()
            self.create_food()
        else:
            self.snake.pop(0)  # Remove the tail if no food is eaten

    def change_direction(self, event):
        key = event.keysym
        if key == "Up" and self.direction != "Down":
            self.direction = "Up"
        elif key == "Down" and self.direction != "Up":
            self.direction = "Down"
        elif key == "Left" and self.direction != "Right":
            self.direction = "Left"
        elif key == "Right" and self.direction != "Left":
            self.direction = "Right"

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")
        if self.score > self.best_score:
            self.best_score = self.score
            self.best_score_label.config(text=f"Best Score: {self.best_score}")

    def game_over(self):
        self.running = False
        self.canvas.create_text(
            self.width // 2, self.height // 2,
            text="GAME OVER", fill="white", font=("Arial", 24, "bold")
        )

    def run_game(self):
        if self.running:
            self.move_snake()
            self.draw_snake()
            self.draw_food()
        # Save the loop ID so it can be canceled later if necessary
        self.game_loop_id = self.root.after(150, self.run_game)

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
