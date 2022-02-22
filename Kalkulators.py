import numbers
from tkinter import*
from turtle import width
calcWind=Tk()
calcWind.title("Pitona kalkulators")

def btnClick(number):
    current=e.get()
    e.delete(0,END)
    newNumber=str(current)+str(number)
    e.insert(0,newNumber)
    return 0

def btnCommand(command):
    global number#iegaumē skaitli
    global mathOp#iegaumē darbību
    global num1
    mathOp=command#+,-,*,/
    num1=int(e.get())
    e.delete(0,END)
    return 0

def Equals():
    num2=int(e.get())
    result=0
    if mathOp=="+":
        result=num1+num2
    elif mathOp=="-":
        result=num1-num2
    elif mathOp=="*":
        result=num1*num2
    elif mathOp=="/":
        result=num1/num2
    else:
        result=0
    e.delete(0,END)
    e.insert(0,str(result))
    return 0

def Clear():
    e.delete(0,END)
    num1=0
    mathOp=""
    return 0

e=Entry(calcWind,width=25,font=("Arial",18))
button0=Button(calcWind,text="0",padx="40",pady="20", bg="lightgrey",fg="black",command=lambda:btnClick(0))
button1=Button(calcWind,text="1",padx="40",pady="20", bg="lightgrey",fg="black",command=lambda:btnClick(1))
button2=Button(calcWind,text="2",padx="40",pady="20", bg="lightgrey",fg="black",command=lambda:btnClick(2))
button3=Button(calcWind,text="3",padx="40",pady="20", bg="lightgrey",fg="black",command=lambda:btnClick(3))
button4=Button(calcWind,text="4",padx="40",pady="20", bg="lightgrey",fg="black",command=lambda:btnClick(4))
button5=Button(calcWind,text="5",padx="40",pady="20", bg="lightgrey",fg="black",command=lambda:btnClick(5))
button6=Button(calcWind,text="6",padx="40",pady="20", bg="lightgrey",fg="black",command=lambda:btnClick(6))
button7=Button(calcWind,text="7",padx="40",pady="20", bg="lightgrey",fg="black",command=lambda:btnClick(7))
button8=Button(calcWind,text="8",padx="40",pady="20", bg="lightgrey",fg="black",command=lambda:btnClick(8))
button9=Button(calcWind,text="9",padx="40",pady="20", bg="lightgrey",fg="black",command=lambda:btnClick(9))
buttonComa=Button(calcWind,text=",",padx="40",pady="20", bg="lightgrey",fg="black")
buttonEaq=Button(calcWind,text="=",padx="40",pady="20", bg="lightgrey",fg="black",command=Equals)
buttonPlus=Button(calcWind,text="+",padx="40",pady="20", bg="lightgrey",fg="black",command=lambda:btnCommand("+"))
buttonMinus=Button(calcWind,text="-",padx="40",pady="20", bg="lightgrey",fg="black",command=lambda:btnCommand("-"))
buttonDivide=Button(calcWind,text="/",padx="40",pady="20", bg="lightgrey",fg="black",command=lambda:btnCommand("/"))
buttonTimes=Button(calcWind,text="*",padx="40",pady="20", bg="lightgrey",fg="black",command=lambda:btnCommand("*"))
buttonDel=Button(calcWind,text="C",padx="40",pady="20", bg="lightgrey",fg="black",command=Clear)

e.grid(row=0,column=0,columnspan=4)

buttonDel.grid(row=1,column=3)

button7.grid(row=2,column=0)
button8.grid(row=2,column=1)
button9.grid(row=2,column=2)
buttonPlus.grid(row=2,column=3)

button4.grid(row=3,column=0)
button5.grid(row=3,column=1)
button6.grid(row=3,column=2)
buttonMinus.grid(row=3,column=3)

button1.grid(row=4,column=0)
button2.grid(row=4,column=1)
button3.grid(row=4,column=2)
buttonDivide.grid(row=4,column=3)

button0.grid(row=5,column=0)
buttonComa.grid(row=5,column=1)
buttonEaq.grid(row=5,column=2)
buttonTimes.grid(row=5,column=3)

calcWind.mainloop()