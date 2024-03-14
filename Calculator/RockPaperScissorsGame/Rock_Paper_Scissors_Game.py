import random
import tkinter as tk
from tkinter import messagebox

# Choices and outcomes
choices = ["rock", "scissor", "paper"]
outcomes = {
    "rock": {"rock": "Draw", "scissor": "Win", "paper": "Lose"},
    "scissor": {"rock": "Lose", "scissor": "Draw", "paper": "Win"},
    "paper": {"rock": "Win", "scissor": "Lose", "paper": "Draw"}
}

def play_game():
    # Get user choice
    user_choice = user_choice_var.get()
    if user_choice == "":
        messagebox.showerror("Error", "Please select an option.")
        return

    # Get computer choice
    computer_choice = random.choice(choices)

    # Update labels with choices
    computer_choice_label.config(text="Computer choice: " + computer_choice.capitalize())
    user_choice_label.config(text="Your choice: " + user_choice.capitalize())

    # Determine result and display message
    result = outcomes[user_choice][computer_choice]
    messagebox.showinfo("Result", f"You {result}!")

# Create main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")

# Label for game title
tk.Label(root, text="Rock Paper Scissors Game", font=("Helvetica", 16)).pack()

# Label for user prompt
tk.Label(root, text="Choose your option:", font=("Helvetica", 12)).pack()

# Radio buttons for user choices
user_choice_var = tk.StringVar()
for choice in choices:
    tk.Radiobutton(root, text=choice.capitalize(), variable=user_choice_var, value=choice, font=("Helvetica", 12)).pack()

# Label for possible outcomes
outcomes_text = "Rock vs Paper -> Paper Wins\nRock vs Scissor -> Rock Wins\nPaper vs Scissor -> Scissor Wins"
tk.Label(root, text=outcomes_text, font=("Helvetica", 12)).pack()

# Button to play the game
play_button = tk.Button(root, text="Play", command=play_game, font=("Helvetica", 12))
play_button.pack(pady=10)

# Labels to display computer and user choices
computer_choice_label = tk.Label(root, text="", font=("Helvetica", 12))
computer_choice_label.pack()

user_choice_label = tk.Label(root, text="", font=("Helvetica", 12))
user_choice_label.pack()

# Button to exit the game
exit_button = tk.Button(root, text="Exit", command=root.destroy, font=("Helvetica", 12))
exit_button.pack(pady=10)

# Run the application
root.mainloop()
