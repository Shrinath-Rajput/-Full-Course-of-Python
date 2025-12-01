from tkinter import *
root=Tk()
def evalute(event):
    data=e.get()
    ans.configure(text="Answer"+str(eval(data)))

    e=Entry(root)
    e.pack()
    ans=Label(root)
    ans.pack()
    root.mainloop()
