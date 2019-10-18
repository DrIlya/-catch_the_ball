from tkinter import *
from random import randrange as rnd, choice


class Ball:
    """Create ball with random size and color."""

    def __init__(self, canvas):
        self.canvas = canvas

        self.x = rnd(100, 700)
        self.y = rnd(100, 500)
        self.r = rnd(20, 30)

        self.a = rnd(-3, 3)
        self.b = rnd(-3, 3)

        self.ball = self.canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r,
                                            fill=choice(colors),
                                            width=0)

    def move(self):
        if self.r < self.x < 800 - self.r and self.r < self.y < 575 - self.r:
            self.canvas.move(self.ball, self.a, self.b)
        elif self.x < self.r or self.x > 800 - self.r:
            self.a = (-self.a) * rnd(1, 2)
            self.b = rnd(-2, 2)
            self.canvas.move(self.ball, self.a, self.b)
        elif self.y < self.r or self.y > 575 - self.r:
            self.b = (-self.b) * rnd(1, 2)
            self.a = rnd(-2, 2)
            self.canvas.move(self.ball, self.a, self.b)

        self.x = self.x + self.a
        self.y = self.y + self.b

        root.after(10, self.move)

    def catch(self, event):
        if ((self.x - event.x) ** 2) + ((self.y - event.y) ** 2) < self.r ** 2:
            return True

    def new(self):
        self.canvas.delete(self.ball)

        self.x = rnd(100, 700)
        self.y = rnd(100, 500)
        self.r = rnd(20, 30)

        self.a = rnd(-3, 3)
        self.b = rnd(-3, 3)

        self.ball = self.canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r,
                                            fill=choice(colors),
                                            width=0)


class Square:
    """Create purple square with random size."""

    def __init__(self, canvas):
        self.canvas = canvas

        self.x = rnd(100, 700)
        self.y = rnd(100, 500)
        self.r = rnd(5, 7)

        self.square = self.canvas.create_rectangle(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r,
                                                   fill='purple',
                                                   width=0)

    def catch(self, event):
        if self.x - self.r <= event.x <= self.x + self.r and self.y - self.r <= event.y <= self.y + self.r:
            return True

    def new(self):
        self.canvas.delete(self.square)

        self.x = rnd(100, 700)
        self.y = rnd(100, 500)
        self.r = rnd(5, 7)

        self.square = self.canvas.create_rectangle(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r,
                                                   fill='purple',
                                                   width=0)

    def newNew(self):
        self.new()
        root.after(1000, self.newNew)


def score(event):
    global n
    if ball_1.catch(event):
        n += 1
        ball_1.new()

    elif ball_2.catch(event):
        n += 1
        ball_2.new()

    elif ball_3.catch(event):
        n += 1
        ball_3.new()

    elif square_1.catch(event):
        n += 2
        square_1.new()

    Label_1["text"] = str(n)


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

ball_2 = Ball(canv)
ball_2.move()

ball_3 = Ball(canv)
ball_3.move()

square_1 = Square(canv)
square_1.newNew()

canv.bind('<Button-1>', score)

mainloop()