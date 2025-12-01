from tkinter import *
import tkinter.messagebox
root=Tk()
tkinter.messagebox.showinfo("Did you know that the world  just bwlow up?")
answer=tkinter.messagebox.askquestion("Question 1","Are you Human")
if answer=="yes":
    tkinter.messagebox.showinfo("Congrajulation you are pass")
elif answer=="no":
    tkinter.messagebox.showinfo("Sorry you are go now ")

root.mainloop()