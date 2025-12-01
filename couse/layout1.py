from tkinter import *
root=Tk()
topframe1=Frame(root,)
topframe1.pack()

buttomframe1=Frame(root)
buttomframe1.pack(side=BOTTOM)

theLabel=Label(root,text="This is kingdom of kohli ")
theLabel.pack(side=BOTTOM)

theLabel=Label(root,text="This is kingdom of shrinath ")
theLabel.pack(side=LEFT)

theLabel=Label(root,text="This is kingdom of virat ")
theLabel.pack(side=RIGHT)

thebutton=Button(topframe1,text="Click me ",fg="blue")
thebutton.pack(side=LEFT)

thebutton1=Button(topframe1,text="Start  ",fg="blue")
thebutton1.pack(side=LEFT)
thebutton2=Button(buttomframe1,text="Stop ",fg="blue")
thebutton2.pack(side=BOTTOM)
root.mainloop()