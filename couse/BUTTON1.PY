from tkinter import *
root=Tk()
theLabel=Label(root,text="This is kingdom of kohli ")
theLabel.pack()

theLabel=Label(root,text="This is kingdom of shrinath ")
theLabel.pack()

theLabel=Label(root,text="This is kingdom of virat ")
theLabel.pack(side=LEFT,fill=X)

def printname():
    print("Hello ,Click to Start Button ")
thebutton=Button(None,text="Click me ",fg="blue",bg="Yellow",command=printname)
thebutton.pack(side=RIGHT,fill=Y,)

def Start():
    print("Hello Every_One ,How r u")
thebutton1=Button(None,text="Start  ",fg="blue",command=Start)
thebutton1.pack()

thebutton2=Button(None,text="Stop ",fg="blue")
thebutton2.pack()
root.mainloop()

#action on Button

