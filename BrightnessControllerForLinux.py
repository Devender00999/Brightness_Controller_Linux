import os
from tkinter import *

#Code for taking input from command line
os.system('rm a.txt')
a = os.system('xrandr | grep " connected primary" |cut -f1 -d " ">>a.txt')
file = open("a.txt", 'r')
a = file.read()
a = a[:len(a)-1]
os.system('rm a.txt')

#Code For GUI
win = Tk()
win.resizable(False, False)
win.title("Brightness Controller")
win.geometry("250x100")
name = Label(win, text="Brightness Controller")
name.pack()
scale = Scale(win, orient=HORIZONTAL, length=200, sliderlength=35)
scale.pack()

#Actual Code for Changing Brightness
def set():
    os.system('xrandr --output {0} --brightness {1}'.format(a, scale.get()/100))
    scale.set(scale.get())


btn = Button(win, text="Set", command=set)
btn.pack()
win.mainloop()
