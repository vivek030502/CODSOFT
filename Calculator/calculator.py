import tkinter
from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.geometry("450x600+500+70")
root.resizable(False,False)
root.configure(bg="#17161b")

equation = ""

def show(value):
    global equation
    equation+=value
    lbl_result.config(text=equation)

def clear():
    global equation
    equation=""
    lbl_result.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result="error"
            equation = ""    
    lbl_result.config(text=result)


lbl_result = Label(root, width=25, height=2, text="", font=("arial", 30))
lbl_result.pack()

btn_clr = Button(root, width=4, height=1, text="C", font=("arial", 30, "bold"), bd=1, fg="#fff", bg="violet", command=lambda: clear())
btn_clr.place(x=10, y=100)

btn_div = Button(root, width=4, height=1, text="/", font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("/"))
btn_div.place(x=120, y=100)

btn_perc = Button(root, width=4, height=1, text="%", font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("%"))
btn_perc.place(x=230, y=100)

btn_mul = Button(root, width=4, height=1, text="*", font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("*"))
btn_mul.place(x=340, y=100)

btn_sev = Button(root, width=4, height=1, text="7", font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("7"))
btn_sev.place(x=10, y=200)

btn_eight = Button(root, width=4, height=1, text="8", font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("8"))
btn_eight.place(x=120, y=200)

btn_nine = Button(root, width=4, height=1, text="9", font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("9"))
btn_nine.place(x=230, y=200)

btn_sub = Button(root, width=4, height=1, text="-", font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("-"))
btn_sub.place(x=340, y=200)

btn_four = Button(root, width=4, height=1, text="4", font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("4"))
btn_four.place(x=10, y=300)

btn_five = Button(root, width=4, height=1, text="5", font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("5"))
btn_five.place(x=120, y=300)

btn_six = Button(root, width=4, height=1, text="6", font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("6"))
btn_six.place(x=230, y=300)

btn_add = Button(root, width=4, height=1, text="+", font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("+"))
btn_add.place(x=340, y=300)

btn_one = Button(root, width=4, height=1, text="1", font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("1"))
btn_one.place(x=10, y=400)

btn_two = Button(root, width=4, height=1, text="2", font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("2"))
btn_two.place(x=120, y=400)

btn_three = Button(root, width=4, height=1, text="3", font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("3"))
btn_three.place(x=230, y=400)

btn_zero = Button(root, width=8, height=1, text="0", font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("0"))
btn_zero.place(x=10, y=500)

btn_dot = Button(root, width=4, height=1, text=".", font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("."))
btn_dot.place(x=220, y=500)

btn_equal = Button(root, width=4, height=3, text="=", font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#fe9037", command=lambda: calculate())
btn_equal.place(x=340, y=410)




root.mainloop()