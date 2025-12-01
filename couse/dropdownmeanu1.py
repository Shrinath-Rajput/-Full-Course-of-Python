from tkinter import *
root=Tk()

def goodboy():
    print("this is  dropdown menu")

def random():
    print("I AM SHRINATH")
mainMenu=Menu(root)
root.configure(menu=mainMenu)
subMenu=Menu(mainMenu)
mainMenu.add_cascade(label="file",menu=subMenu)
subMenu.add_command(label="Random fun",command= goodboy)
subMenu.add_command(label="New file ",command= random)

#supertor file
subMenu.add_separator()
subMenu.add_command(label="Store  ",command= random)

root.mainloop()