from tkinter import *
root=Tk()
def leftclick(event):
    print("Left")

def rightClick(event):
    print("Right")

def Scroll(event):
    print("SCroll")

root.geometry("500x500")
root.bind("<Button-1>",leftclick)

root.bind("<Button-2>",rightClick)

root.bind("<Button-3>",Scroll)
root.mainloop()