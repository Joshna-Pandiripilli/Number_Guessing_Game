import random
import tkinter
root = tkinter.Tk()
root.title("Number_Guessing_Game")
label = tkinter.Label(root, text ="Welcome to NUmber game")
label2 = tkinter.Label(root, text = "Add number between 1 and 100")
entry = tkinter.Entry(root)
entry.pack()
sec_num = random.randint(1,100)
label.pack()
label2.pack()
def guessing():
    try:
        guessed_text = entry.get()
        guess = int(guessed_text)
    except ValueError:
        label2.configure(text = "enter a valid number between 1 and 100")
        return
    if guess > sec_num:
        label2.configure(text = "Too High!")
    elif guess < sec_num:
        label2.configure(text = "Too Low!")
    else:
        label.configure(text = "Your Guess is right")
button = tkinter.Button(root, text ="Guess", command= guessing)
button.pack()
root.mainloop()

