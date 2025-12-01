from tkinter import *
root=Tk()
equal=""
equation=StringVar()
cal=Label(root,textvariable=equation)
equation.set("Enter your Equcation")
cal.grid(columnspan=4)
def press(num):
    global equal
    equal=equal+str(num)
    equation.set(equal)
def equalPress():
    total=str(eval(equal))
    equation.set(total)
def clear():
    equal=""
    equation.set("")


button1=Button(root,text="1",command=lambda:press(1))
button1.grid(row=1,column=0)

button2=Button(root,text="2",command=lambda:press(2))
button2.grid(row=1,column=1)

button3=Button(root,text="3",command=lambda:press(3))
button3.grid(row=1,column=2)

button4=Button(root,text="4",command=lambda:press(4))
button4.grid(row=3,column=0)

button5=Button(root,text="5",command=lambda:press(5))
button5.grid(row=3,column=1)

button6=Button(root,text="6",command=lambda:press(6))
button6.grid(row=3,column=2)

button7=Button(root,text="7",command=lambda:press(7))
button7.grid(row=5,column=0)

button8=Button(root,text="8",command=lambda:press(8))
button8.grid(row=5,column=1)

button9=Button(root,text="9",command=lambda:press(9))
button9.grid(row=5,column=2)

button10=Button(root,text="0",command=lambda:press(0))
button10.grid(row=7,column=1)

add=Button(root,text="+",command=lambda:press("+"))
add.grid(row=1,column=4)

sub=Button(root,text="-",command=lambda:press("-"))
sub.grid(row=3,column=4)

mul=Button(root,text="*",command=lambda:press("*"))
mul.grid(row=5,column=4)

div=Button(root,text="/",command=lambda:press("/"))
div.grid(row=7,column=4)

equal1=Button(root,text="=",command=equalPress)
equal1.grid(row=7,column=2,)

clear=Button(root,text="C",command=clear)
clear.grid(row=7,column=0)



root.mainloop()