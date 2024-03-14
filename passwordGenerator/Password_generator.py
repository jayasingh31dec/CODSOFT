import tkinter as tk
from tkinter import messagebox
import random
import string

class PlaceholderEntry(tk.Entry):
    def __init__(self, master=None, placeholder="", *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.placeholder = placeholder
        self.placeholder_color = "grey"
        self.normal_color = self["fg"]

        self.bind("<FocusIn>", self._focus_in_event)
        self.bind("<FocusOut>", self._focus_out_event)

        self.put_placeholder()

    def _focus_in_event(self, event):
        if self.get() == self.placeholder:
            self.delete(0, tk.END)
            self.config(fg=self.normal_color)

    def _focus_out_event(self, event):
        if not self.get():
            self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self.config(fg=self.placeholder_color)

    def clear_placeholder(self):
        if self.get() == self.placeholder:
            self.delete(0, tk.END)
            self.config(fg=self.normal_color)

# Global variables for entry widgets
letters_entry = None
symbols_entry = None
numbers_entry = None

# Function to generate password
def generate_password():
    global letters_entry, symbols_entry, numbers_entry  # Update global variables

    try:
        # Get the number of letters, symbols, and numbers from the input fields
        n_letters = int(letters_entry.get())
        n_symbols = int(symbols_entry.get())
        n_numbers = int(numbers_entry.get())

        # Check if input values are valid
        if n_letters <= 0 or n_symbols < 0 or n_numbers <= 0:
            messagebox.showerror("Error", "Please enter valid input.")
            return

        # Check if the total length of the password is at least 4 characters
        if n_letters + n_symbols + n_numbers < 4:
            messagebox.showerror("Error", "Password must be at least 4 characters long.")
            return

        # Define character sets for letters, numbers, and symbols
        letters = string.ascii_letters
        numbers = string.digits
        symbols = string.punctuation

        # Generate a password by randomly selecting characters from each set
        password_list = [random.choice(letters) for _ in range(n_letters)]
        password_list += [random.choice(symbols) for _ in range(n_symbols)]
        password_list += [random.choice(numbers) for _ in range(n_numbers)]

        # Shuffle the password characters for randomness
        random.shuffle(password_list)

        # Convert the password list to a string
        password = ''.join(password_list)

        # Display the generated password
        result_label.config(text="Your generated password is: " + password)

        # Add the password to the listbox for reference
        passwords_listbox.insert(tk.END, password)

        # Clear input fields after generating password
        clear_inputs()

        # Check password strength and display it
        strength_label.config(text="Password Strength: " + check_password_strength(password))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid input.")

# Function to clear input fields
def clear_inputs():
    global letters_entry, symbols_entry, numbers_entry  # Access global variables
    for entry in (letters_entry, symbols_entry, numbers_entry):
        entry.delete(0, tk.END)
        entry.put_placeholder()  # Restore placeholder text

# Function to check password strength
def check_password_strength(password):
    return "Weak" if len(password) < 8 else ("Medium" if len(password) < 12 else "Strong")

# Function to copy password to clipboard
def copy_to_clipboard():
    password = passwords_listbox.get(tk.ACTIVE)
    root.clipboard_clear()
    root.clipboard_append(password)

# GUI setup
root = tk.Tk()
root.title("Password Generator")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Labels and input fields for letters, symbols, and numbers
labels = ["Letters:", "Symbols:", "Numbers:"]
entries = [PlaceholderEntry(frame, placeholder="Enter number of letters", width=25) for _ in range(3)]


for i, label in enumerate(labels):
    tk.Label(frame, text=label).grid(row=i, column=0, sticky="e", padx=(0, 5))
    entries[i].grid(row=i, column=1, sticky="w")

# Assign entry widgets to global variables
letters_entry, symbols_entry, numbers_entry = entries

# Buttons for generating password, clearing inputs, and copying password to clipboard
buttons = [
    tk.Button(frame, text="Generate Password", command=generate_password),
    tk.Button(frame, text="Clear Inputs", command=clear_inputs),
    tk.Button(frame, text="Copy to Clipboard", command=copy_to_clipboard)
]

for i, button in enumerate(buttons):
    button.grid(row=i+3, columnspan=2, pady=5)

# Labels for displaying result, password strength, and generated passwords
result_label = tk.Label(frame, text="")
result_label.grid(row=6, columnspan=2)

strength_label = tk.Label(frame, text="")
strength_label.grid(row=7, columnspan=2)

passwords_label = tk.Label(frame, text="Generated Passwords:")
passwords_label.grid(row=8, column=0, columnspan=2, pady=(10, 5))

# Listbox to display generated passwords
passwords_listbox = tk.Listbox(frame, width=30, height=5)
passwords_listbox.grid(row=9, column=0, columnspan=2)

# Set focus on the first input field
letters_entry.focus()

root.mainloop()
