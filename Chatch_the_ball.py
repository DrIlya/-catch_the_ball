from tkinter import *
from random import randrange as rnd, choice
import time
import math

# привязывает главное окно к переменной root
root = Tk()
root.geometry('800x600')

# создает
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

colors = ['red', 'orange', 'yellow', 'green', 'blue']

n = 0


def new_ball():
    global x, y, r, ball, a, b
    canv.delete(ALL)
    x = rnd(100, 700)
    y = rnd(100, 500)
    r = rnd(30, 50)
    ball = canv.create_oval(x - r, y - r, x + r, y + r, fill=choice(colors), width=0)
    root.after(10000, new_ball)
    a = rnd(-10, 10)
    b = rnd(-10, 10)


def move_ball():
    canv.move(ball, a, b)
    root.after(60, move_ball)


def click(event):
    global n
    if ((x - event.x) ** 2) + ((y - event.y) ** 2) < r ** 2:
        n += 1
    print(n)


new_ball()
move_ball()
canv.bind('<Button-1>', click)
mainloop()
