#NEB1N
from tkinter import *           #importing
import random 


root = Tk()

#centering code
w = 700
h = 700
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x=(ws/2)-(w/2)
y=(hs/2)-(h/2)
root.geometry("%dx%d+%d+%d"%(w,h,x,y))

#configuring the window
root.title("prolly guessing")
root.configure(bg="slateblue2")

#configuring the variables
guess_da_number = "none"
points = 0
correct = True

#the main game window
def StartGame(correct, points):
    global guess_da_number
    for button in button_list:
        if correct == True:
            button.config(text=str(random.randint(0, 100)))
            randomButton = random.choice(button_list)
            guess_da_number = randomButton.cget("text")
        elif correct == False:
            randomButton = guess_da_number
    print(points)
    print("Secret Number is: ", guess_da_number)


#event for the buttons
def OnClick(event):
    global points
    global correct
    btn = event.widget
    buttonText = btn.cget("text")
    if guess_da_number == buttonText:
        answer_label.config(text="Yes it was " + guess_da_number)
        points += 5
        correct = True
        StartGame(correct, points)
    else:
        answer_label.config(text="No it wasn't that one")
        points -= 1
        correct = False
        StartGame(correct, points)


#top most label
title_label = Label(root, text="Guess the Secret Number", font=("Arial 12"), pady = 8, bg="slateblue2", justify="center")

#buttons for the game to be called upon
button_one = Button(root, text="00", font=("Arial 15"), width=20, pady=20, bg="mediumpurple1")
button_two = Button(root, text="00", font=("Arial 15"), width=20, pady=20, bg="mediumpurple2")
button_three = Button(root, text="00", font=("Arial 15"), width=20, pady=20, bg="mediumpurple3")
inputbox = Entry(root, width = 30, font = ("Arial 12 bold"), fg = "black", bg = "slateblue1", justify="center")

#justifying the functions of the labels
button_list = [button_one, button_two, button_three]
username_label = Label(root, text="Enter A Username", font=("Arial 15"), pady=9, fg="purple", bg="slateblue2", justify="center")
answer_label = Label(root, text="Answer", font=("Arial 15"), pady=9, fg="purple", bg="slateblue2", justify="center")

#grid
title_label.grid(row = 0, column=0, columnspan=3)

#justifying the location of the buttons
button_one.grid(row=1, column=0)
button_two.grid(row=1, column=1)
button_three.grid(row=1, column=2)

#justifying locations
answer_label.grid(row = 2, column=0, columnspan=3)
inputbox.grid(row=7, column=0, columnspan= 3)
username_label.grid(row=6, column=0, columnspan = 3)

#binding the buttons to actions
button_one.bind("<Button-1>", OnClick)
button_two.bind("<Button-1>", OnClick)
button_three.bind("<Button-1>", OnClick)

#starting the game
StartGame(correct, points)
root.mainloop()
 
