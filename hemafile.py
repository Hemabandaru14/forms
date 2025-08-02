
import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError

        characters = ''
        if letters_var.get():
            characters += string.ascii_letters
        if digits_var.get():
            characters += string.digits
        if symbols_var.get():
            characters += string.punctuation
        if not characters:
            messagebox.showerror("Error", "Select at least one character type.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Password length must be a positive number.")

def copy_to_clipboard():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI Setup
root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Password Length:").grid(row=0, column=0, pady=5, sticky='w')
length_entry = tk.Entry(root)
length_entry.insert(0, "12")
length_entry.grid(row=0, column=1, pady=5)

letters_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Letters", variable=letters_var).grid(row=1, column=0, sticky='w')
tk.Checkbutton(root, text="Include Digits", variable=digits_var).grid(row=2, column=0, sticky='w')
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).grid(row=3, column=0, sticky='w')

tk.Button(root, text="Generate Password", command=generate_password).grid(row=4, column=0, columnspan=2, pady=10)

password_entry = tk.Entry(root, width=30)
password_entry.grid(row=5, column=0, columnspan=2, pady=5)

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).grid(row=6, column=0, columnspan=2, pady=5)

root.mainloop()
