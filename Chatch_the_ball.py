from tkinter import *
from random import randrange as rnd, choice


class Ball:

    def __init__(self, canvas):
        self.canvas = canvas

        self.x = rnd(100, 700)
        self.y = rnd(100, 500)
        self.r = rnd(30, 50)

        self.a = rnd(-3, 3)
        self.b = rnd(-3, 3)

        self.n = n

        self.ball = self.canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r,
                                            fill=choice(colors),
                                            width=0)

    def move(self):
        if self.r < self.x < 800 - self.r and self.r < self.y < 580 - self.r:
            self.canvas.move(self.ball, self.a, self.b)
        elif self.x < self.r or self.x > 800 - self.r:
            self.a = (-self.a) * rnd(1, 2)
            self.b = rnd(-2, 2)
            self.canvas.move(self.ball, self.a, self.b)
        elif self.y < self.r or self.y > 580 - self.r:
            self.b = (-self.b) * rnd(1, 2)
            self.a = rnd(-2, 2)
            self.canvas.move(self.ball, self.a, self.b)

        self.x = self.x + self.a
        self.y = self.y + self.b

        root.after(10, self.move)

    def score(self, event):
        if ((self.x - event.x) ** 2) + ((self.y - event.y) ** 2) < self.r ** 2:
            self.n += 1
        Label_1["text"] = str(self.n)


root = Tk()
root.geometry('800x600')

root.title('Поймай шарик')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

colors = ['red', 'orange', 'yellow', 'green', 'blue']
n = 0

Label_1 = Label(root, text=str(n))
Label_1.pack()

ball_1 = Ball(canv)
ball_1.move()
canv.bind('<Button-1>', ball_1.score)

mainloop()
