import tkinter as tk
from tkinter import messagebox


def check_strength():
    password = entry.get()
    if len(password) == 0:
        messagebox.showinfo("Password Strength", "Please enter a password!")
    elif len(password) < 5:
        messagebox.showinfo("Password Strength", "Weak Password")
    elif len(password) < 10:
        messagebox.showinfo("Password Strength", "Moderate Password")
    else:
        messagebox.showinfo("Password Strength", "Strong Password")

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("300x150")

label = tk.Label(root, text="Enter your password:")
label.pack(pady=10)

entry = tk.Entry(root, show="*")
entry.pack(pady=5)

btn = tk.Button(root, text="Check Strength", command=check_strength)
btn.pack(pady=10)
root.mainloop()
