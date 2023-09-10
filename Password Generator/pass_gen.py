from tkinter import *
import string
import random       #for random value
import pyperclip    #for copy

def generator():
    small_alphabets = string.ascii_lowercase
    capital_alphabets = string.ascii_uppercase
    numbers = string.digits
    special_character = string.punctuation

    all = small_alphabets+capital_alphabets+numbers+special_character
    password_length = int(box_len.get())

    if choice.get()==1:  #for weak password
        pass_field.insert(0,random.sample(small_alphabets+numbers,password_length))

    if choice.get()==2:  #for medium password
        pass_field.insert(0,random.sample(small_alphabets+capital_alphabets+numbers,password_length))

    if choice.get()==3:  #for strong password
        pass_field.insert(0,random.sample(all,password_length))


    
def copy():
    random_password = pass_field.get()
    pyperclip.copy(random_password)

def clear():
    pass_field.delete(0, 'end')
    


root = Tk()
root.title("Password Generator")
root.geometry('350x400+500+100')
root.config(bg="grey20")
choice = IntVar()
Font = ("arial", 14, "bold")

lbl_title = Label(root, text=" Password Generator App", font=("Railway", 20, "bold"), bg="grey20", fg="yellow")
lbl_title.grid(pady=5) 

radio_weak = Radiobutton(root, text="Weak", value=1, variable=choice, font=Font, bg="grey20", fg="pink")
radio_weak.grid(pady=5)

radio_medium = Radiobutton(root, text="Medium", value=2, variable=choice, font=Font, bg="grey20", fg="pink")
radio_medium.grid(pady=5)

radio_strong = Radiobutton(root, text="Strong", value=3, variable=choice, font=Font, bg="grey20", fg="pink")
radio_strong.grid(pady=5)

lbl_pass_len = Label(root, text=" Password Length", font=("Railway", 16, "bold"), bg="grey20", fg="#ff03a5")
lbl_pass_len.grid(pady=5)

box_len = Spinbox(root, from_=6, to=15, width=6, font=Font)
box_len.grid(pady=5)

btn_gen = Button(root, text='Generate', font=Font, bg='orange', command=generator)
btn_gen.grid(pady=5)

pass_field = Entry(root, width=20, bd=2, font=Font)
pass_field.grid(pady=5)

btn_copy = Button(root, text='Copy', font=Font, bg='silver', command=copy)
btn_copy.place(x=190, y=350)

btn_clr = Button(root, text="Clear", font=Font, bg="silver", command=clear)
btn_clr.place(x=80, y=350)



root.mainloop()