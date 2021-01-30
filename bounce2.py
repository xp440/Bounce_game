from tkinter import *
import random
import time

# initialization
root = Tk()
ab = 500
ac = 500

wnd = Canvas(root, width=ab, height=ac)
wnd.pack()
root.title('bounce game ')



class Ball:
    def __init__(self, x1, y1, p1):
        self.canvas = wnd
        self.score = 0
        self.id = wnd.create_oval(10, 10, 25, 25, fill='red', outline='black')
        self.canvas.move(self.id, 150, 100)
        self.x = 2
        self.y = -3
        self.ch = ac
        self.cw = ab
        self.paddle = p1

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:
            self.y = 6
        if pos[3] >= self.ch:
            self.y = -6
        if pos[0] <= 0:
            self.x = 5
        if pos[2] >= self.cw:
            self.x = -5
        paddlepos = self.paddle.get_pos()
        d1 = 0
        d2 = 0
        if pos[1] >= paddlepos[1]:
            d1 = pos[1] - paddlepos[1]
        elif paddlepos[1] >= pos[1]:
            d1 = paddlepos[1] - pos[1]
        # @ print(d2)
        if pos[0] >= paddlepos[0]:
            d2 = pos[0] - paddlepos[0]
        elif paddlepos[0] >= pos[0]:
            d2 = paddlepos[0] - pos[0]
        print(self.score)
        if pos[0] >= paddlepos[0] and pos[0] <= paddlepos[0] + 100:
            if d1 <= 5:
                self.y = -1 * self.y
                self.score = self.score + 1
                print(self.score)


# ball class ends
# class paddle starts


class Paddle:
    def __init__(self):
        self.canvas = wnd
        self.x = 1
        self.id = wnd.create_rectangle(0, 50, 100, 60, fill='blue', outline='black')
        self.canvas.move(self.id, 200, 300)
        self.canvas.bind_all('<KeyPress-Left>', self.move_left)
        self.canvas.bind_all('<KeyPress-Right>', self.move_right)

    #         self.canvas.bind_all('<KeyRelease-Left>', self.stop_moving)
    #         self.canvas.bind_all('<KeyRelease-Right>', self.stop_moving)

    def move_left(self, evt):
        self.x = -4

    def move_right(self, evt):
        self.x = 4

    def stop_moving(self, evt):
        self.x = 0

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)

    def get_pos(self):
        return self.canvas.coords(self.id)


P = Paddle()
b = Ball(1, -2, P)
btn = Button(wnd, text='quit', command=root.destroy)
btn.place(x=0, y=0)
while 1:
    True
    b.draw()
    P.draw()
    root.update_idletasks()
    root.update()
    time.sleep(0.01)

mainloop()
