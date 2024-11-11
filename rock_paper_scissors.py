import random as rand
import tkinter as tk
from tkinter import messagebox
import os

# Specify the paths to the Tcl/Tk libraries
os.environ['TCL_LIBRARY'] = r'C:\Users\ajban\AppData\Local\Programs\Python\Python313\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\ajban\AppData\Local\Programs\Python\Python313\tcl\tk8.6'

def play(player):
    cpu = rand.randint(1, 5)
    choices = {1: "✊", 2: "✋", 3: "✌️", 4: "🦎", 5: "🖖"}
    player_choice = choices[player]
    cpu_choice = choices[cpu]
    
    result = ""
    if player == cpu:
        result = "It's a tie!"
    elif (player == 1 and (cpu == 2 or cpu == 5)) or \
         (player == 2 and (cpu == 3 or cpu == 5)) or \
         (player == 3 and (cpu == 1 or cpu == 4)) or \
         (player == 4 and (cpu == 1 or cpu == 3)) or \
         (player == 5 and (cpu == 2 or cpu == 4)):
        result = "You lose!"
    else:
        result = "You win!"
    
    messagebox.showinfo("Result", f"You chose: {player_choice}\nCPU chose: {cpu_choice}\n{result}")

root = tk.Tk()
root.title("Rock Paper Scissors Lizard Spock")

tk.Label(root, text="Rock Paper Scissors Lizard Spock", font=("Helvetica", 16)).pack(pady=10)
tk.Label(root, text="Choose one:", font=("Helvetica", 14)).pack(pady=5)

buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=10)

choices = [("✊", 1), ("✋", 2), ("✌️", 3), ("🦎", 4), ("🖖", 5)]
for (text, value) in choices:
    tk.Button(buttons_frame, text=text, font=("Helvetica", 14), command=lambda v=value: play(v)).pack(side=tk.LEFT, padx=5)

root.mainloop()