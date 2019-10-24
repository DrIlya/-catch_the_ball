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
        """Move ball with random speed and repel ball from the walls."""
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
        """Check if you catch the ball by Left Button Mouse.
        Return True if you catch"""
        if ((self.x - event.x) ** 2) + ((self.y - event.y) ** 2) < self.r ** 2:
            return True

    def new(self):
        """Create new ball"""
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
        """Check if you catch the square by Left Button Mouse.
        Return True if you catch"""
        if self.x - self.r <= event.x <= self.x + self.r and self.y - self.r <= event.y <= self.y + self.r:
            return True

    def new(self):
        """Create a new square"""
        self.canvas.delete(self.square)

        self.x = rnd(100, 700)
        self.y = rnd(100, 500)
        self.r = rnd(5, 7)

        self.square = self.canvas.create_rectangle(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r,
                                                   fill='purple',
                                                   width=0)

    def newNew(self):
        """create a new square every second"""
        self.new()
        root.after(rnd(1000, 2000), self.newNew)


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
    elif square_2.catch(event):
        n += 2
        square_2.new()

    Label_1["text"] = str(n)


def newGame(event):
    global n
    n = 0
    Label_1["text"] = str(n)
    ball_1.new()
    ball_2.new()
    ball_3.new()
    square_1.new()


def putYourName(event):
    label_01.grid_forget()
    button_01.grid_forget()
    button_02.grid_forget()

    label_02.grid(row=0, column=0)
    entry_01.grid(row=1, column=0)
    button_03.grid(row=2, column=0)


def theGame(event):
    global pName, temp
    if len(entry_01.get()) == 0:
        label_03.grid(row=3, column=0)
    else:
        pName = entry_01.get()

        label_02.grid_forget()
        button_03.grid_forget()
        entry_01.grid_forget()
        label_03.grid_forget()

        root.geometry('800x620')

        canv.pack(fill=BOTH, expand=1)
        Label_1.pack()
        Label_2.pack()
        ball_1.move()
        ball_2.move()
        ball_3.move()
        square_1.newNew()
        square_2.newNew()

        timer()


def exitGame_1(event):
    root.destroy()


def exitGame_2():
    global n, pName

    try:
        scores = open("scores.txt")
    except (OSError, IOError):
        scores = open('scores.txt', 'w')
        scores.write('1. A 5\n2. B 3\n3. C 2')
        scores.close()
        scores = open("scores.txt")

    content = ['{} {}'.format(s.split()[1],
                              s.split()[2]) for s in scores.read().split('\n')]
    scores.close()

    content.append('{} {}'.format(pName, n))
    content.sort(key=get_key, reverse=True)
    text = '\n'.join(['{}. {}'.format(i, item) for i, item in enumerate(content[:10], start=1)])

    scores = open("scores.txt", 'w')
    scores.write(text)
    scores.close()


def timer():
    global temp
    if temp <= 15:
        root.after(1000, timer)
        Label_2.configure(text='Timer:' + '  ' + str(temp))
        temp += 1
    else:
        exitGame_2()
        root.destroy()


def get_key(item):
    return int(item.split()[1])


root = Tk()

root.title('Поймай шарик')

canv = Canvas(root, bg='white')

colors = ['red', 'orange', 'yellow', 'green', 'blue']
n = 0
pName = ''
temp = 0

Label_1 = Label(root, text=str(n))
Label_2 = Label(root, text='')

ball_1 = Ball(canv)
ball_2 = Ball(canv)
ball_3 = Ball(canv)
square_1 = Square(canv)
square_2 = Square(canv)

label_01 = Label(root, text='Меню', font=2, width=70, bg='yellow')
button_01 = Button(root, text='Начать игру', font=2, width=70, height=5, fg='green')
button_02 = Button(root, text='Выход из игры', font=2, width=70, height=5, fg='red')

label_01.grid(row=0, column=0)
button_01.grid(row=1, column=0)
button_02.grid(row=2, column=0)

entry_01 = Entry(root, width=70, font=2)
label_02 = Label(root, text='Введите ваше имя', font=2, width=70)
button_03 = Button(root, text='Играть', font=2, width=70, height=5, fg='green')
label_03 = Label(root, text='Пожалуйста, введите ваше имя!', font=2, width=70, fg='red')

button_01.bind('<Button-1>', putYourName)
button_03.bind('<Button-1>', theGame)
button_02.bind('<Button-1>', exitGame_1)

canv.bind('<Button-1>', score)
canv.bind('<Button-3>', newGame)

mainloop()
