import math
from ast import operator
from distutils import command
import numbers
from tkinter import*
from turtle import width
calcWind=Tk()
calcWind.title("Pitona kalkulators")
calcWind.configure(bg="pink")

def btnClick(number):
    current=e.get()
    e.delete(0,END)
    newNumber=str(current)+str(number)
    e.insert(0,newNumber)
    return 0

def point():
    if e.get()==".":
        pass
    else:
        e.insert(END,".")

def correct(inp):
    if inp== '':
        return True
    if ' ' in inp:
        return False
    try:
        float(inp)
    except ValueError:
        return False
    else:
        return True

def Sqrt():
    global operator
    global num1
    global mathOp
    mathOp=command
    num1=float(e.get())
    num1=math.sqrt(num1)
    e.delete(0,END)
    e.insert(0,num1)

def Square():
    global num1
    global mathOp
    num1=float(e.get())
    num2=num1*num1
    e.delete(0,END)
    e.insert(0,num2)

def Log():
    global num1
    global mathOp
    num1=float(e.get())
    num2=math.log10(num1)
    e.delete(0,END)
    e.insert(0,num2)

def btnCommand(command):
    global number#iegaumē skaitli
    global mathOp#iegaumē darbību
    global num1
    mathOp=command#+,-,*,/
    num1=float(e.get())
    e.delete(0,END)
    return 0

def Equals():
    num2=float(e.get())
    result=0
    if mathOp=="+":
        result=num1+num2
    elif mathOp=="-":
        result=num1-num2
    elif mathOp=="*":
        result=num1*num2
    elif mathOp=="/":
        result=num1/num2
    elif mathOp=="%":
        result=num1*0.01*num2
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

reg = calcWind.register(correct)

e=Entry(calcWind,width=20,bd=2,bg="cyan",font=("Arial",20),validate="key",validatecommand=(reg,"%P"))
button0=Button(calcWind,text="0",padx="40",pady="20",bd=2,font=("Arial",15), bg="cyan",fg="black",command=lambda:btnClick(0))
button1=Button(calcWind,text="1",padx="40",pady="20",bd=2,font=("Arial",15), bg="cyan",fg="black",command=lambda:btnClick(1))
button2=Button(calcWind,text="2",padx="40",pady="20",bd=2,font=("Arial",15), bg="cyan",fg="black",command=lambda:btnClick(2))
button3=Button(calcWind,text="3",padx="40",pady="20",bd=2,font=("Arial",15), bg="cyan",fg="black",command=lambda:btnClick(3))
button4=Button(calcWind,text="4",padx="40",pady="20",bd=2,font=("Arial",15), bg="cyan",fg="black",command=lambda:btnClick(4))
button5=Button(calcWind,text="5",padx="40",pady="20",bd=2,font=("Arial",15), bg="cyan",fg="black",command=lambda:btnClick(5))
button6=Button(calcWind,text="6",padx="40",pady="20",bd=2,font=("Arial",15), bg="cyan",fg="black",command=lambda:btnClick(6))
button7=Button(calcWind,text="7",padx="40",pady="20",bd=2,font=("Arial",15), bg="cyan",fg="black",command=lambda:btnClick(7))
button8=Button(calcWind,text="8",padx="40",pady="20",bd=2,font=("Arial",15), bg="cyan",fg="black",command=lambda:btnClick(8))
button9=Button(calcWind,text="9",padx="40",pady="20",bd=2,font=("Arial",15), bg="cyan",fg="black",command=lambda:btnClick(9))
buttonpercent=Button(calcWind,text="%",padx="36.5",pady="20",bd=2,font=("Arial",15), bg="purple",fg="white",command=lambda:btnCommand("%"))
buttonEaq=Button(calcWind,text="=",padx="39.5",pady="20",bd=2,font=("Arial",15), bg="purple",fg="white",command=Equals)
buttonPlus=Button(calcWind,text="+",padx="38",pady="20",bd=2,font=("Arial",15), bg="purple",fg="white",command=lambda:btnCommand("+"))
buttonMinus=Button(calcWind,text="-",padx="40.5",pady="20",bd=2,font=("Arial",15), bg="purple",fg="white",command=lambda:btnCommand("-"))
buttonDivide=Button(calcWind,text="/",padx="40.5",pady="20",bd=2,font=("Arial",15), bg="purple",fg="white",command=lambda:btnCommand("/"))
buttonTimes=Button(calcWind,text="*",padx="40",pady="20",bd=2,font=("Arial",15), bg="purple",fg="white",command=lambda:btnCommand("*"))
buttonDel=Button(calcWind,text="C",padx="38",pady="20",bd=2,font=("Arial",15), bg="purple",fg="white",command=Clear)
buttonSqrt=Button(calcWind,text="√",padx="40",pady="20",bd=2,font=("Arial",15), bg="purple",fg="white",command=Sqrt)
buttonSquare=Button(calcWind,text="^2",padx="37",pady="20",bd=2,font=("Arial",15), bg="purple",fg="white",command=Square)
buttonLog=Button(calcWind,text="Log",padx="29",pady="20",bd=2,font=("Arial",15), bg="purple",fg="white",command=Log)
buttonPoint=Button(calcWind,text=".",padx="42",pady="20",bd=2,font=("Arial",15), bg="purple",fg="white",command=point)

e.grid(row=0,column=0,columnspan=3)

buttonDel.grid(row=0,column=3)

button7.grid(row=2,column=0)
button8.grid(row=2,column=1)
button9.grid(row=2,column=2)
buttonPlus.grid(row=4,column=3)

button4.grid(row=3,column=0)
button5.grid(row=3,column=1)
button6.grid(row=3,column=2)
buttonMinus.grid(row=3,column=3)

button1.grid(row=4,column=0)
button2.grid(row=4,column=1)
button3.grid(row=4,column=2)
buttonDivide.grid(row=2,column=3)

button0.grid(row=5,column=0)
buttonpercent.grid(row=5,column=1)
buttonEaq.grid(row=5,column=2)
buttonTimes.grid(row=5,column=3)

buttonSqrt.grid(row=6,column=0)
buttonSquare.grid(row=6,column=1)
buttonLog.grid(row=6,column=2)
buttonPoint.grid(row=6,column=3)

calcWind.mainloop()