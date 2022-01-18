from tkinter import *
import random
import time
from tkinter import messagebox
from threading import Thread

def pick_random_word_and_color(a):
    word = random.choice(a)
    color = random.choice(a)
    return [word.upper(),color]


def timer():
    global seconds,tim,basic,seconds,root
    while (seconds > -1):
        time.sleep(1)
        tim.config(text=basic+str(seconds)+"s")
        seconds -= 1
    messagebox.showinfo("ColorGame","Your score is "+str(score))
    root.destroy()

def check(word,word1):
    return word == word1
def onStartCheck(event):
    global colors,repeat,wordx,sc,score,user,color1
    if (color1 == user.get()):
        score += 1
        sc.config(text="Your Score : " + str(score))
    user.set("")
    word1,color = pick_random_word_and_color(colors)
    wordx.config(text=word1,fg=color)
    color1 = color
    repeat -= 1

def main(event):
    en.config(state=NORMAL)
    t1 = Thread(target=timer)
    t1.start()
    root.bind("<Return>",onStartCheck)

root = Tk()
repeat = 10
seconds = 60
basic = "Game Ends in : "
root.config(bg="pink")
score = 0
user = StringVar()
root.geometry("500x300")
root.title("Color Game")
label = Label(root,text="Enter the color of the given word not the text in the word.",bg="pink",fg="black",font=("helvetica",13,"bold"))
label.pack()
enter = Label(root,text="Hit enter to start.",bg="pink",fg="black",font=("helvetica",13,"bold"))
enter.pack(pady=10)
colors = ["red","yellow","blue","green","orange","violet","black","purple","brown","white"]
sc = Label(root,text="Your score : "+str(score),bg="pink",fg="green",font=("helvetica",15,"bold"))
sc.pack(pady=15)
tim = Label(text=basic+str(seconds)+"s",font=("Helvetica",15,"bold"),fg="green",bg="pink")
tim.pack(pady=15)
word1,color1 = pick_random_word_and_color(colors)
wordx = Label(root,text=word1,fg=color1,bg="pink",font=("helvetica",15,"bold"))
wordx.pack()
en = Entry(root,textvariable=user)
en.pack()
en.config(state=DISABLED)
root.bind("<Return>",main)
root.mainloop()
