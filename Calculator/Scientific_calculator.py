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

def calculate_trig(func):
    try:
        angle = float(entry_result.get())
        result = func(math.radians(angle))
        entry_result.delete(0, tk.END)
        entry_result.insert(tk.END, result)
    except ValueError:
        messagebox.showerror("Error", "Invalid Input")

def add_constant(constant):
    entry_result.insert(tk.END, constant)

def add_percentage():
    try:
        number = float(entry_result.get())
        result = number / 100
        entry_result.delete(0, tk.END)
        entry_result.insert(tk.END, result)
    except ValueError:
        messagebox.showerror("Error", "Invalid Input")

root = tk.Tk()
root.title("Scientific Calculator")

# Entry field
entry_result = tk.Entry(root, width=20, borderwidth=5, font=("Arial", 14), justify="right")
entry_result.grid(row=0, column=0, columnspan=6, padx=10, pady=10, ipady=10, sticky="ew")

# Buttons
buttons = [
    ('C', '⌫', '%', 'sin', 'cos', 'tan'),
    ('7', '8', '9', '/', '(', ')'),
    ('4', '5', '6', '*', 'x²', '√'),
    ('1', '2', '3', '-', '1/x', 'π'),
    ('0', '.', '=', '+', 'e', '^'),
]

for i, row in enumerate(buttons):
    for j, label in enumerate(row):
        button = tk.Button(root, text=label, padx=20, pady=15, font=("Arial", 12))
        if label.isdigit() or label in ['.', '+', '-', '*', '/', '(', ')', '^', 'x²', '1/x', 'π', 'e']:
            button.config(command=lambda num=label: button_click(num))
        elif label == '=':
            button.config(command=calculate)
        elif label == 'C':
            button.config(command=clear)
        elif label == '⌫':
            button.config(command=backspace)
        elif label == '%':
            button.config(command=add_percentage)
        elif label == 'sin':
            button.config(command=lambda: calculate_trig(math.sin))
        elif label == 'cos':
            button.config(command=lambda: calculate_trig(math.cos))
        elif label == 'tan':
            button.config(command=lambda: calculate_trig(math.tan))
        elif label == 'x²':
            button.config(command=lambda: button_click('^2'))
        elif label == '√':
            button.config(command=calculate_root)
        elif label == '1/x':
            button.config(command=lambda: button_click('1/'))
        elif label == '^':
            button.config(command=lambda: button_click('^'))
        elif label == 'π':
            button.config(command=lambda: add_constant(math.pi))
        elif label == 'e':
            button.config(command=lambda: add_constant(math.e))
        button.grid(row=i+1, column=j, padx=5, pady=5, sticky="ew")

root.mainloop()
