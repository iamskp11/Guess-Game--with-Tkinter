from tkinter import *
import tkinter.messagebox as msg
import random
import time
win=Tk()
win.geometry("500x200")
win.title("Guess Game")
##### Guess Game GUI
l=Label(win,text="Guesses {}".format(""))
dec=Label(win,text="")
l.grid(row=0,column=0)
x=0
game=1
def pa():
    global x,game
    x=0
    game=1
    dec.config(text="")
    l.config(text="Guesses 0")

def change():
    global x
    x+=1
    l.config(text="Guesses {}".format(x))
def won():
    global x,game
    x+=1
    l.config(text="Guesses {}".format(x))
    dec.config(text="Wow! You won in {} guesses".format(x))
    dec.grid(row=3,column=1,columnspan=2)
    x=0
    game=0
    play=Button(win,text="Play Again",command=pa)
    play.grid(row=4,column=0)
    end=Button(win,text="Quit",command=quit)
    end.grid(row=5,column=0)
def response(event):
    global game
    if game==0:
        msg.showerror("ERROR","Please click on Play Again to Restart")
        return
    x=user.get()
    x=int(x)
    if x<1 or x>5:
        msg.showerror("Incorrect Response","Please submit integer in 1-5")
        return
    com=random.randint(1,5)
    print(x,com)
    if x==com:
        won()
    else :
        change()
user=IntVar()
game=1
user_input=Label(win,text="Input your guess , a number in range 1-5")
user_input.grid(row=1,column=0)
Entry(win,textvariable=user).grid(row=1,column=2)
b=Button(win,text="Submit")
b.grid(row=2,column=2)
b.bind("<Button-1>",response)



win.mainloop()
