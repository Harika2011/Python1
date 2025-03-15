#Write a Python program to create an application to play a rock paper scissor game between a user and the computer,
#  using the Python Tkinter library.

import tkinter as tk
from tkinter import messagebox
import random

def check_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        return "You win!"
    else:
        return "Computer wins!"

def user_choice_made(choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    result = check_winner(choice, computer_choice)
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

root = tk.Tk()
root.title("Rock Paper Scissors Game")

title_label = tk.Label(root, text="Rock Paper Scissors Game", font=("Helvetica", 18))
title_label.pack(pady=10)

info_label = tk.Label(root, text="Choose your move:", font=("Helvetica", 14))
info_label.pack(pady=5)

rock_button = tk.Button(root, text="Rock", width=20, height=2, command=lambda: user_choice_made("Rock"))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", width=20, height=2, command=lambda: user_choice_made("Paper"))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", width=20, height=2, command=lambda: user_choice_made("Scissors"))
scissors_button.pack(pady=5)

result_label = tk.Label(root, text="Your result will appear here", font=("Helvetica", 14))
result_label.pack(pady=20)

root.mainloop()
