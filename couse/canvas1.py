"""from tkinter import *
root=Tk()
canvas=Canvas(root,width=300,height=300)
canvas.pack()
canvas.create_rectangle(20,20,100, 270)
canvas.create_line(20,20,200,200)
canvas.create_polygon(0,0,5,20,50,30,40,15)
root.mainloop()"""

from tkinter import *
root=Tk()
canvas=Canvas(root,width=400,height=400)
canvas.pack()
def area(x1,y1,x2,y2):
    canvas.create_rectangle(x1,y1,x2,y2,fil="red")
area(20,30,200,400)
area(40,60,300,70)
root.mainloop()

