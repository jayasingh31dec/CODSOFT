import tkinter as tk
from tkinter import messagebox


# Function to add a new contact
def add_contact():
    # Retrieve information from entry fields
    name = name_entry.get()
    phone_number = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    # Check if all fields are filled
    if name == "" or phone_number == "" or email == "" or address == "":
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    # Add contact details to lists
    names.append(name)
    phone_numbers.append(phone_number)
    emails.append(email)
    addresses.append(address)

    # Update display, clear entry fields, and show success message
    update_display()
    clear_entries()
    messagebox.showinfo("Success", "Contact added successfully!")
    name_entry.focus()


# Function to search for a contact
def search_contact():
    # Retrieve search query
    search_name = search_entry.get()
    # Check if the name exists in the contacts list
    if search_name in names:
        # If found, display contact details
        index = names.index(search_name)
        result_label.config(
            text=f"Name: {names[index]}, Phone Number: {phone_numbers[index]}, Email: {emails[index]}, Address: {addresses[index]}")
    else:
        # If not found, display error message
        result_label.config(text="Contact not found.")
    search_entry.focus()


# Function to delete a contact
def delete_contact():
    # Retrieve the name to be deleted
    delete_name = delete_entry.get()
    # Check if the name exists in the contacts list
    if delete_name in names:
        # Confirm deletion with a dialog box
        confirmation = messagebox.askyesno("Confirmation", f"Are you sure you want to delete {delete_name}?")
        if confirmation:
            # If confirmed, delete the contact
            index = names.index(delete_name)
            del names[index]
            del phone_numbers[index]
            del emails[index]
            del addresses[index]
            # Update display, clear entry fields, and show success message
            update_display()
            clear_entries()
            messagebox.showinfo("Success", "Contact deleted successfully!")
    else:
        # If contact not found, display error message
        result_label.config(text="Contact not found.")
    delete_entry.focus()


# Function to update the display with the list of contacts
def update_display():
    # Clear the listbox
    display_listbox.delete(0, tk.END)
    # Iterate through the contacts and insert them into the listbox
    for i in range(len(names)):
        display_listbox.insert(tk.END, f"{names[i]} \t {phone_numbers[i]} \t {emails[i]} \t {addresses[i]}")


# Function to clear all entry fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    search_entry.delete(0, tk.END)
    delete_entry.delete(0, tk.END)


# Initialize empty lists to store contact details
names = []
phone_numbers = []
emails = []
addresses = []

# Create the main application window
root = tk.Tk()
root.title("Contact Management System")
root.resizable(True, True)

# Labels
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, sticky="e")
phone_label = tk.Label(root, text="Phone Number:")
phone_label.grid(row=1, column=0, sticky="e")
email_label = tk.Label(root, text="Email:")
email_label.grid(row=2, column=0, sticky="e")
address_label = tk.Label(root, text="Address:")
address_label.grid(row=3, column=0, sticky="e")
search_label = tk.Label(root, text="Search Contact:")
search_label.grid(row=5, column=0, sticky="e")
delete_label = tk.Label(root, text="Delete Contact:")
delete_label.grid(row=7, column=0, sticky="e")
result_label = tk.Label(root, text="")
result_label.grid(row=9, column=0, columnspan=2)

# Entry Fields
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1)
address_entry = tk.Entry(root)
address_entry.grid(row=3, column=1)
search_entry = tk.Entry(root)
search_entry.grid(row=5, column=1)
delete_entry = tk.Entry(root)
delete_entry.grid(row=7, column=1)

# Buttons
add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=4, column=0, columnspan=2, pady=5)
search_button = tk.Button(root, text="Search", command=search_contact)
search_button.grid(row=6, column=0, columnspan=2, pady=5)
delete_button = tk.Button(root, text="Delete", command=delete_contact)
delete_button.grid(row=8, column=0, columnspan=2, pady=5)

# Listbox
display_listbox = tk.Listbox(root)
display_listbox.grid(row=10, column=0, columnspan=2, sticky="nsew")
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=display_listbox.yview)
scrollbar.grid(row=10, column=2, sticky="ns")
display_listbox.config(yscrollcommand=scrollbar.set)

root.mainloop()
