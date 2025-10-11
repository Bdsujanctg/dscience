import tkinter as tk
from tkinter import messagebox
import random

def play(user_choice):
    options = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(options)
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "You Win!"
    else:
        result = "Computer Wins!"
    messagebox.showinfo("Result", f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n\n{result}")

root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("350x200")

label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Helvetica", 14))
label.pack(pady=20)

btn_rock = tk.Button(root, text="Rock", width=10, command=lambda: play("Rock"))
btn_rock.pack(pady=5)

btn_paper = tk.Button(root, text="Paper", width=10, command=lambda: play("Paper"))
btn_paper.pack(pady=5)

btn_scissors = tk.Button(root, text="Scissors", width=10, command=lambda: play("Scissors"))
btn_scissors.pack(pady=5)

root.mainloop()
