from tkinter import *
root=Tk()

label11=Label(root,text="Name")
label11.grid(row=0,column=0)
entrySpace=Entry(root)
entrySpace.grid(row=0,column=1)
#check button
cbutton=Checkbutton(root,text="Remember the name ")
cbutton.grid(columnspan=2)


label21=Label(root,text="Password ")
label21.grid(row=1,column=0)
entrySpace1=Entry(root)
entrySpace1.grid(row=1,column=1)
check1=Checkbutton(root,text="Remember the password")
check1.grid(columnspan=4)





label3=Label(root,text="education ")
label3.grid(row=4,column=0)
entrySpace3=Entry(root)
entrySpace3.grid(row=4,column=1)
root.mainloop()