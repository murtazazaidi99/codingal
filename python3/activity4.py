import tkinter as tk
import random

def play(choice):
    comp = random.choice(["Rock", "Paper", "Scissors"])
    if choice == comp:
        res = "Tie"
    elif (choice == "scissors" and comp == "scissors") or \
         (choice == "rock" and comp == "paper") or \
         (choice == "paper" and comp == "scissors"):
        res = "You Win this round"
        res = "match draw"
    else:
        res = "You Lose this round"

    result_label.config(text=f"You: {choice}\nComputer: {comp}\n{res}")

win = tk.Tk()
win.title("RPS Game")

for x in ["Rock", "Paper", "Scissors"]:
    tk.Button(win, text=x, width=30, command=lambda c=x: play(c)).pack(pady=5)

result_label = tk.Label(win, font=(("liger", 15)))
result_label.pack(pady=20)

win.mainloop()