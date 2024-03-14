import tkinter as tk
from tkinter import messagebox
import math

def button_click(number):
    entry_result.insert(tk.END, number)

def clear():
    entry_result.delete(0, tk.END)

def backspace():
    current = entry_result.get()[:-1]
    entry_result.delete(0, tk.END)
    entry_result.insert(tk.END, current)

def calculate():
    try:
        expression = entry_result.get()
        result = eval(expression)
        entry_result.delete(0, tk.END)
        entry_result.insert(tk.END, result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

def calculate_root():
    try:
        number = float(entry_result.get())
        result = math.sqrt(number)
        entry_result.delete(0, tk.END)
        entry_result.insert(tk.END, result)
    except ValueError:
        messagebox.showerror("Error", "Invalid Input")

root = tk.Tk()
root.title("Simple Calculator")

# Styling
root.configure(bg="#f0f0f0")
button_bg = "#d9d9d9"
button_fg = "#333333"

# Entry field
entry_result = tk.Entry(root, width=20, borderwidth=5, font=("Arial", 14), justify="right")
entry_result.grid(row=0, column=0, columnspan=5, padx=10, pady=10, ipady=10, sticky="ew")

# Buttons
buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('+', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('*', 4, 3),
    ('C', 1, 0), ('0', 5, 1), ('⌫', 1, 1), ('/', 5, 3),
    ('=', 5, 0), ('.', 5, 2), ('√', 1, 2)  # Added square root button
]

for label, row, col in buttons:
    if label == '=':
        button = tk.Button(root, text=label, padx=20, pady=15, command=calculate, font=("Arial", 12), bg=button_bg, fg=button_fg)
    elif label == 'C':
        button = tk.Button(root, text=label, padx=20, pady=15, command=clear, font=("Arial", 12), bg=button_bg, fg=button_fg)
    elif label == '⌫':
        button = tk.Button(root, text=label, padx=20, pady=15, command=backspace, font=("Arial", 12), bg=button_bg, fg=button_fg)
    elif label == '√':  # Added condition for square root button
        button = tk.Button(root, text=label, padx=20, pady=15, command=calculate_root, font=("Arial", 12), bg=button_bg, fg=button_fg)
    else:
        button = tk.Button(root, text=label, padx=20, pady=15, command=lambda num=label: button_click(num), font=("Arial", 12), bg=button_bg, fg=button_fg)
    button.grid(row=row, column=col, padx=5, pady=5, sticky="ew")

root.mainloop()



