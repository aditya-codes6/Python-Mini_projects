
import tkinter as tk
from tkinter import messagebox

def check_winner():
    global winner

    combos = [ [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6] ]

    for combo in combos:
        if (buttons[combo[0]]["text"] ==
            buttons[combo[1]]["text"] ==
            buttons[combo[2]]["text"] != ""):

            for i in combo:
                buttons[i].config(bg="green")

            winner = True
            label.config(text=f"Player {current_player} wins!")
            messagebox.showinfo(
                "Tic-Tac-Toe",
                f"Player {current_player} wins!"
            )

            for button in buttons:
                button.config(state="disabled")

            return True

    return False


def button_click(index):
    global current_player, winner

    if buttons[index]["text"] == "" and not winner:
        buttons[index].config(text=current_player)

        if check_winner():
            return

        if all(button["text"] != "" for button in buttons):
            winner = True
            label.config(text="It's a draw!")
            messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            return

        current_player = "O" if current_player == "X" else "X"
        label.config(text=f"Player {current_player}'s turn")


root = tk.Tk()
root.title("Tic-Tac-Toe")
root.resizable(False, False)

current_player = "X"
winner = False

buttons = [
    tk.Button(
        root,
        text="",
        font=("Arial", 25),
        width=6,
        height=2,
        command=lambda i=i: button_click(i)
    )
    for i in range(9)
]

for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

label = tk.Label(
    root,
    text=f"Player {current_player}'s turn",
    font=("Arial", 16)
)
label.grid(row=3, column=0, columnspan=3)

root.mainloop()
