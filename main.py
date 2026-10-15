import random
import tkinter
root = tkinter.Tk()
root.geometry("400x300")
root.title("Number_Guessing_Game")
label = tkinter.Label(root, text ="Welcome to Number game")
label2 = tkinter.Label(root, text = "Add number between 1 and 100")
entry = tkinter.Entry(root,width = 50)
entry.pack()
sec_num = random.randint(1,100)
label.pack()
label2.pack()
game_over = False
def guessing():
    global game_over
    if game_over:
        return
    try:
        guessed_text = entry.get()
        guess = int(guessed_text)
        if guess < 1 or guess > 100:
            label2.configure(text = "enter a number which lies between 1 and 100 :)")
            return
    except ValueError:
        label2.configure(text = "enter a valid number between 1 and 100")
        return
    if guess > sec_num:
        label2.configure(text = "Too High!")
    elif guess < sec_num:
        label2.configure(text = "Too Low!")
    else:
        label.configure(text = "Your Guess is right")
        game_over = True
button = tkinter.Button(root, text ="Guess", command= guessing)
button.pack()
root.mainloop()
