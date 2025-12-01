from tkinter import *
import random
import time

root=Tk()
root.title("App Development")
root.resizable(0,0)
root.wm_attributes("-topmost",1)
canvas1=Canvas(root,width=500,height=500)
canvas1.pack()
root.update()


class Ball:
    def __init__(self,canvas1,color):
        self.canvas1=canvas1

        self.id=canvas1.create_oval(10,10,25,25,fill=color)
        self.canvas1.move(self.id,245,100)
        start=[-3,-2,-1,0,1,2,3]
        random.shuffle(start)

        self.x=start[0]
        self.y=-3
        self.canvas1_height=self.canvas1.winfo_height()
        self.canvas1_width=self.canvas1.winfo_width()

    def draw(self):

        self.canvas1.move(self.id,self.x,self.y)
        pos=self.canvas1.coords(self.id)
        print(pos)
        if pos[1]<=0:
            self.y=3
        if pos[3]>=self.canvas1_height:
            self.y=-3
        if pos[0]<=0:
            self.x=3
        if pos[2]>=self.canvas1_width:
            self.x=-3

class Paddle:
    def __init__(self,canvas1,color):
        self.canvas1=canvas1
        self.id=canvas1.create_rectangle(0,0,100,10,fill=color)
        self.canvas1.move(self.id,200,300)
        self.x=0
        self.canvas1_width=self.canvas1.winfo_width()
        self.canvas1.bind_all('<KeyPress-Left>',self.tum_left)
        self.canvas1.bind_all('<KeyPress-Right>',self.tum_right)


    def draw1(self):
        self.canvas1.move(self.id,self.x,0)
        pos=self.canvas1.coords(self.id)
        if pos[0]<=0:
            self.x=2
        if pos[2]>=self.canvas1_width:
            self.x=0
    def tum_left(self,evt):
        self.x=-2
    def tum_right(self,evt):
        self.x=2
ball=Ball(canvas1,'red')
Paddle=Paddle(canvas1,'blue')
while 1:
    ball.draw()
    Paddle.draw1()
    root.update_idletasks()
    root.update()
    time.sleep(0.1)

