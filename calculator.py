from tkinter import *
#setting the global variable expression
expression=" "
#function to input and storing it into expression
def input_number(number,equation):
    global expression
    expression=expression+str(number)
    equation.set(expression)
#function for clear field
def clear_field(equation):
    global expression
    expression=" "
    equation.set(expression)
#function to evaluate expression
def evaluate(equation):
    global expression
    result=str(eval(expression))
    equation.set(result)
#main function
def main():
#setting window and it's properties
    window=Tk()
    window.geometry("400x400")
    window.title('calculator')
    window.configure(bg="#E6F1F3")
#setting stringvariable equation
    equation = StringVar()
    equation.set("enter the expression:")
#setting entry label and it's properties
    display=Entry(window,textvariable=equation,fg="#36648B",bg="#E6E6FA",width=40,font=14)
    display.place(height=14)
    display.grid(row=0,columnspan=4)

#buttons with properties
    button7=Button(window,text="7",width=10,height=3,bg="white",command=lambda: input_number("7",equation))
    button8=Button(window,text="8",width=10,height=3,bg="white",command=lambda: input_number("8",equation))
    button9=Button(window,text="9",width=10,height=3,bg="white",command=lambda: input_number("9",equation))
    button4=Button(window,text="4",width=10,height=3,bg="white",command=lambda: input_number("4",equation))
    button5=Button(window,text="5",width=10,height=3,bg="white",command=lambda: input_number("5",equation))
    button6=Button(window,text="6",width=10,height=3,bg="white",command=lambda: input_number("6",equation))
    button1=Button(window,text="1",width=10,height=3,bg="white",command=lambda: input_number("1",equation))
    button2=Button(window,text="2",width=10,height=3,bg="white",command=lambda: input_number("2",equation))
    button3=Button(window,text="3",width=10,height=3,bg="white",command=lambda: input_number("3",equation))
    buttondot=Button(window,text=".",width=10,height=3,bg="white",command=lambda: input_number(".",equation))
    buttonzero=Button(window,text="0",width=10,height=3,bg="white",command=lambda: input_number("0",equation))
    buttonequal=Button(window,text="=",width=10,height=3,bg="white",command=lambda: evaluate(equation))
    buttondiv=Button(window,text="/",width=10,height=3,bg="white",command=lambda: input_number("/",equation))
    buttonmul=Button(window,text="x",width=10,height=3,bg="white",command=lambda: input_number("*",equation))
    buttonsub=Button(window,text="-",width=10,height=3,bg="white",command=lambda: input_number("-",equation))
    buttonadd=Button(window,text="+",width=10,height=3,bg="white",command=lambda: input_number("+",equation))
    buttonclear=Button(window,text="clear",width=23,height=3,bg="white",command=lambda: clear_field(equation))
    buttonbrace1=Button(window,text="(",width=10,height=3,bg="white",command=lambda: input_number("(",equation))
    buttonbrace2=Button(window,text=")",width=10,height=3,bg="white",command=lambda: input_number(")",equation))
#setting button positions
    button7.grid(row=1,column=0)
    button8.grid(row=1,column=1)
    button9.grid(row=1,column=2)
    button4.grid(row=2,column=0)
    button5.grid(row=2,column=1)
    button6.grid(row=2,column=2)
    button1.grid(row=3,column=0)
    button2.grid(row=3,column=1)
    button3.grid(row=3,column=2)
    buttondot.grid(row=4,column=0)
    buttonzero.grid(row=4,column=1)
    buttonequal.grid(row=4,column=2)
    buttondiv.grid(row=1,column=3)
    buttonmul.grid(row=2,column=3)
    buttonsub.grid(row=3,column=3)
    buttonadd.grid(row=4,column=3)
    buttonclear.grid(row=5,columnspan=2)
    buttonbrace1.grid(row=5,column=2)
    buttonbrace2.grid(row=5,column=3)


    window.mainloop()

if __name__ == '__main__':
    main()



