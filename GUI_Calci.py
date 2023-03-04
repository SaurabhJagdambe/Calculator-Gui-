from tkinter import *

base = Tk()
base.title("Calculator")
base.geometry("300x400+300+300")

f = ("Arial Black",20)

var=""

def back():
    global var
    var=var[0:-1]
    lbl1.config(text=var)
    return var

def Perform_addition():
    global var
    var=var + "+"
    lbl1.config(text=var)
    return var
    # a=int( txt1.get())
    # b=int ( txt2.get())
    # c=a+b
    # result.configure(text="addition is "+str(c))


def Perform_substraction():
    global var
    var = var + "-"
    lbl1.config(text=var)
    return var

    # a=int( txt1.get())
    # b=int ( txt2.get())
    # c=a-b
    # result.configure(text="Substraction is"+str(c))


def Perform_multiplication():
    global var
    var = var + "*"
    lbl1.config(text=var)
    return var
    # a=int( txt1.get())
    # b=int ( txt2.get())
    # c=a*b
    # result.configure(text="Multipication is "+str(c))

def Perform_Divide():
    global var
    var = var + "/"
    lbl1.config(text=var)
    return var
    # a=int( txt1.get())
    # b=int ( txt2.get())
    # c=a/b
    # result.configure(text="Division is"+str(c))


def clr_scr():
    global var
    var=""
    lbl1.config(text=var)
    return var
    # data.get()
    # data.delete(0,END)
    # b= txt2.get()
    # txt2.delete(0,END)
    # lbl1.configure(text="Result is")
#
def Ans():
    global var
    lbl1.config(text="Syntax Error")
    a=eval(var)
    var=str(a)
    lbl1.config(text=var)
    return var
    # if operator == "+":
    #     x=int(var2.split("+")[1])
    #     c=A+x
    #     data.set(c)
    #     var=str(c)
    #
    # elif operator == "-":
    #     x = int(var2.split("-")[1])
    #     c = A - x
    #     data.set(c)
    #     var = str(c)
    # elif operator == "*":
    #     x=int(var2.split("*")[1])
    #     c=A*x
    #     data.set(c)
    #     var=str(c)
    # elif operator == "/":
    #     x=int((var2.split("/")[1]))
    #     if x==0:
    #         messagebox.showerror("Error","invalid")
    #         A=""
    #         var=""
    #         data.set(var)
    #     else:
    #         c=int(A/x)
    #         data.set(c)
    #     x=int(var2.split("+")[1])
    #     c=A*x
    #     data.set(c)
    #     var=str(c)
def button1():
    global var
    var=var + "1"
    lbl1.config(text=var)
    return var

def button2():
    global var
    var = var + "2"
    lbl1.config(text=var)
    return var


def button3():
    global var
    var = var + "3"
    lbl1.config(text=var)
    return var

def button4():
    global var
    var = var + "4"
    lbl1.config(text=var)
    return var

def button5():
    global var
    var = var + "5"
    lbl1.config(text=var)
    return var

def button6():
    global var
    var = var + "6"
    lbl1.config(text=var)
    return var

def button7():
    global var
    var = var + "7"
    lbl1.config(text=var)
    return var

def button8():
    global var
    var = var + "8"
    lbl1.config(text=var)
    return var

def button9():
    global var
    var = var + "9"
    lbl1.config(text=var)
    return var

def button0():
    global var
    var = var + "0"
    lbl1.config(text=var)
    return var






# screen= Text(base,width="45",height="5")
# screen.pack()
# txt1=Entry(base,width="50")
# txt1.focus()
# txt1.pack()
# txt2= Entry(base,width="50")
# txt2.pack()


add= Button(base,text="+",command=Perform_addition,font=f)
add.place(x=170,y=100)


sub= Button(base,text=" -",command=Perform_substraction,font=f)
sub.place(x=170,y=180)


mul= Button(base,text="*",command=Perform_multiplication,font=f)
mul.place(x=170,y=260)

div= Button(base,text="/ ",command=Perform_Divide,font=f)
div.place(x=170,y=330)


clr= Button(base,text="C",command=clr_scr,font=f)
clr.place(x=67,y=330)


Ans= Button(base,text="=",command=Ans,font=f)
Ans.place(x=119,y=330)



lbl1=Label(base,text="",width="45",height="3",font= ("Arial Black",16),bg="white")
lbl1.pack()


bt1=Button(base,text="1",font=f,command=button1)
bt1.place(x=10,y=100)

bt2=Button(base,text="2",font=f,command=button2)
bt2.place(x=67,y=100)

bt3=Button(base,text="3",font=f,command=button3)
bt3.place(x=119,y=100)

bt4=Button(base,text="4",font=f,command=button4)
bt4.place(x=10,y=180)

bt5=Button(base,text="5",font=f,command=button5)
bt5.place(x=67,y=180)

bt6=Button(base,text="6",font=f,command=button6)
bt6.place(x=119,y=180)

bt7=Button(base,text="7",font=f,command=button7)
bt7.place(x=10,y=260)

bt8=Button(base,text="8",font=f,command=button8)
bt8.place(x=67,y=260)

bt9=Button(base,text="9",font=f,command=button9)
bt9.place(x=119,y=260)

bt0=Button(base,text="0",font=f,command=button0)
bt0.place(x=10,y=330)

bt10=Button(base,text="DEL",font=("Times new roman",14),command=back)
bt10.place(x=230,y=100)

base.mainloop()