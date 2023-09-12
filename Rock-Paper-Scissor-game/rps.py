#------------------------ROCK-PAPER-SCISSOR GAME--------------------------#

from tkinter import *
from PIL import Image, ImageTk
from random import randint
from tkinter import messagebox  


root = Tk()
root.title('Rock-Paper-Scissor')
root.geometry('1000x550+150+50')
root.config(bg='#AF33FF')

#update choices
choices=["rock","paper","scissor"]
def updatechoice(x):
    #for computer
    compChoice = choices[randint(0,2)]
    if compChoice =="rock":
        comp_lbl.configure(image=rock_img_comp)
    elif compChoice =="paper":
        comp_lbl.configure(image=paper_img_comp)
    else:
        comp_lbl.configure(image=scissor_img_comp)

    #for user
    if x=="rock":
        user_lbl.configure(image=rock_img_user)
    elif x=="paper":
        user_lbl.configure(image=paper_img_user)
    else:
        user_lbl.configure(image=scissor_img_user)

    checkwin(x,compChoice)

#update result
def updateresult(x):
    result['text'] = x

#update score
def updateuserscore():
    score = int(user_score["text"])
    score +=1
    user_score["text"] = str(score)
    check_game_over()

def updatecompscore():
    score = int(comp_score["text"])
    score +=1
    comp_score["text"] = str(score)
    check_game_over()

#check winner
def checkwin(user, computer):
    if user == computer:
        updateresult("It's a Tie!!!")
    elif user == "rock":
        if computer == "paper":
            updateresult("You Lose!!!")
            updatecompscore()
        else:
            updateresult("You WON!!!")
            updateuserscore()
    elif user == "paper":
        if computer == "scissor":
            updateresult("You Lose!!!")
            updatecompscore()
        else:
            updateresult("You WON!!!")
            updateuserscore()
    elif user == "scissor":
        if computer == "rock":
            updateresult("You Lose!!!")
            updatecompscore()
        else:
            updateresult("You WON!!!")
            updateuserscore()
    else:
        pass

#Replay or Exit
def check_game_over():
    user_score_value = int(user_score["text"])
    comp_score_value = int(comp_score["text"])
    
    if user_score_value == 3:
        result_msg = "Congratulations! You won the game!\nDo you want to play again?"
    elif comp_score_value == 3:
        result_msg = "Computer won the game!\nDo you want to play again?"
    else:
        return  #Continue the game 
    
    #Display message box
    replay = messagebox.askyesno("Game Over", result_msg)
    
    if replay:
        #Reset scores and images
        user_score["text"] = "0"
        comp_score["text"] = "0"
        user_lbl.configure(image=rock_img_user)
        comp_lbl.configure(image=rock_img_comp)
    else:
        root.destroy()  #To close the game 



lbl_title = Label(root, text='ROCK PAPER SCISSOR', font=('playfair display', 35, 'bold'), width=25, bg='#AF33FF', fg='yellow')
lbl_title.place(x=150, y=10)

#pictures
rock_img_comp = ImageTk.PhotoImage(Image.open("Images\Rock1.png"))
rock_img_user = ImageTk.PhotoImage(Image.open("Images\Rock2.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("Images\Paper1.png"))
paper_img_user = ImageTk.PhotoImage(Image.open("Images\Paper2.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("Images\Scissor1.png"))
scissor_img_user = ImageTk.PhotoImage(Image.open("Images\Scissor2.png"))


#insert picture
user_lbl = Label(root, image = rock_img_user, bg='#AF33FF', width=180, height=180)
user_lbl.place(x=700, y=100)
comp_lbl = Label(root, image = rock_img_comp, bg='#AF33FF', width=180, height=180)
comp_lbl.place(x=100, y=100)

#score
comp_score = Label(root, text=0, font=('arial',100,'bold'), bg='#AF33FF', fg='white')
comp_score.place(x=300, y=100)
user_score = Label(root, text=0, font=('arial',100,'bold'), bg='#AF33FF', fg='white')
user_score.place(x=600, y=100)

lbl_vs = Label(root, text="VS", font=('Italic',46,'bold'), bg='#AF33FF', fg='pink')
lbl_vs.place(x=450, y=140)


#player name
lbl_comp = Label(root, text="COMPUTER", font=('arial',16,'bold'), bg='#AF33FF', fg='white')
lbl_comp.place(x=120, y=300)
lbl_user = Label(root, text="USER", font=('arial',16,'bold'), bg='#AF33FF', fg='white')
lbl_user.place(x=750, y=300)

#Button
rock = Button(root, text="ROCK" ,width=20, height=1, command=lambda:updatechoice("rock"),font=('Railway', 14, 'bold'),fg='white', bg='blue')
rock.place(x=50, y=350)
paper = Button(root, text="PAPER", font=('Railway', 14, 'bold'),width=20, height=1, command=lambda:updatechoice("paper"),fg='white', bg='green')
paper.place(x=350, y=350)
scissor = Button(root, text="SCISSOR", font=('Railway', 14, 'bold'),width=20, height=1, command=lambda:updatechoice("scissor"),fg='white', bg='red')
scissor.place(x=650, y=350)

#result
result = Label(root, width=20, height=1, fg='white', bg='red', text='Result', font=("Helvetica",40, "bold"))
result.place(x=180, y=440)

root.mainloop()