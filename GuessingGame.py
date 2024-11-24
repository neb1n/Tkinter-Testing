#NEB1N
from tkinter import *
import random 


root = Tk()
root.title("prolly guessing")
root.geometry("700x150")
root.configure(bg="slateblue2")
guess_da_number = "none"
points = 0


def StartGame(points):
    global guess_da_number
    for button in button_list:
            button.config(text=str(random.randint(0, 100)))
    randomButton = random.choice(button_list)
    guess_da_number = randomButton.cget("text")
    print(points)
    print("Secret Number is: ", guess_da_number)

def OnClick(event):
    global points
    btn = event.widget
    buttonText = btn.cget("text")
    if guess_da_number == buttonText:
        answer_label.config(text="Yes it was " + guess_da_number)
        StartGame(points)
        points += 5
    else:
        points -= 1
        StartGame(points)
        
title_label = Label(root, text="Guess the Secret Number", font=("Arial 12"), pady = 8, bg="slateblue2", justify="center")

button_one = Button(root, text="00", font=("Arial 15"), width=20, pady=20, bg="mediumpurple1")
button_two = Button(root, text="00", font=("Arial 15"), width=20, pady=20, bg="mediumpurple2")
button_three = Button(root, text="00", font=("Arial 15"), width=20, pady=20, bg="mediumpurple3")

button_list = [button_one, button_two, button_three]
answer_label = Label(root, text="Answer", font=("Arial 15"), pady=9, fg="purple", bg="slateblue2", justify="center")
title_label.grid(row = 0, column=0, columnspan=3)

button_one.grid(row=1, column=0)
button_two.grid(row=1, column=1)
button_three.grid(row=1, column=2)

answer_label.grid(row = 2, column=0, columnspan=3)

button_one.bind("<Button-1>", OnClick)
button_two.bind("<Button-1>", OnClick)
button_three.bind("<Button-1>", OnClick)

StartGame(points)
root.mainloop()
