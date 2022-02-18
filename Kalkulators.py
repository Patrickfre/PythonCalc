from tkinter import*
calcWind=Tk()
calcWind.title("Pitona kalkulators")

button0=Button(calcWind,text="0",padx="40",pady="20", bg="lightgrey",fg="black")
button1=Button(calcWind,text="1",padx="40",pady="20", bg="lightgrey",fg="black")
button2=Button(calcWind,text="2",padx="40",pady="20", bg="lightgrey",fg="black")
button3=Button(calcWind,text="3",padx="40",pady="20", bg="lightgrey",fg="black")
button4=Button(calcWind,text="4",padx="40",pady="20", bg="lightgrey",fg="black")
button5=Button(calcWind,text="5",padx="40",pady="20", bg="lightgrey",fg="black")
button6=Button(calcWind,text="6",padx="40",pady="20", bg="lightgrey",fg="black")
button7=Button(calcWind,text="7",padx="40",pady="20", bg="lightgrey",fg="black")
button8=Button(calcWind,text="8",padx="40",pady="20", bg="lightgrey",fg="black")
button9=Button(calcWind,text="9",padx="40",pady="20", bg="lightgrey",fg="black")

button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)

calcWind.mainloop()