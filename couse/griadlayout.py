from tkinter import *
root=Tk()
label1=Label(root,text="Name")
label1.grid(row=0,column=0)
entrySpace=Entry(root)
entrySpace.grid(row=0,column=1)

label2=Label(root,text="I am the AIML Student ")
label2.grid(row=0,column=1)

label3=Label(root,text="like to python programing ")
label3.grid(row=1,column=0)

#entries


label11=Label(root,text="Name")
label11.grid(row=0,column=0)
entrySpace=Entry(root)
entrySpace.grid(row=0,column=1)
#check button
cbutton=Checkbutton(root,text="Remember the name ")
cbutton.grid(columnspan=2)


"""label21=Label(root,text="Roll no ")
label21.grid(row=0,column=1)
entrySpace1=Entry(root)
entrySpace1.grid(row=1,column=0)

label3=Label(root,text="education ")
label3.grid(row=2,column=0)
entrySpace3=Entry(root)
entrySpace3.grid(row=2,column=2)"""
root.mainloop()