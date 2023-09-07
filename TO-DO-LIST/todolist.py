from tkinter import *
from tkinter import ttk

class todolist:
    def __init__(self, root):
        self.root = root
        self.root.title('TO-DO-LIST')
        self.root.geometry('700x500+350+100')

        lbl_title=Label(self.root,text='TO-DO-LIST APP',font=('Times New Roman',30,'bold'),fg='darkblue',bg='orange')
        lbl_title.place(x=0,y=0,width=700,height=50)

        lbl_addtask=Label(self.root,text='ADD TASK',font=('Times New Roman',20,'bold'),fg='black',bg='orange')
        lbl_addtask.place(x=30,y=60,width=200,height=50)

        lbl_task=Label(self.root,text='LIST OF TASK',font=('Times New Roman',20,'bold'),fg='black',bg='orange')
        lbl_task.place(x=350,y=60,width=250,height=40)

        self.listbox=Listbox(self.root,height = 20,bd=7,
                  width = 15,
                  bg = 'grey',
                  activestyle = 'dotbox',
                  font = ('Helvetica', 26, 'bold'),
                  fg = 'yellow')
        self.listbox.place(x=300,y=110,width=400,height=400)

        self.txt=Text(self.root,bd=5,width=20,font=('arial',18,'bold'),bg='lightgrey')
        self.txt.place(x=30,y=150,width=200,height=50)

        self.load_tasks()  

        btn_add=Button(self.root,text='ADD',command=self.add_task,font=('arial',20,'bold'),width='13',bg='orange',fg='black')
        btn_add.place(x=30,y=260,width=200,height=40)

        btn_del=Button(self.root,text='DELETE',command=self.delete_task,font=('arial',20,'bold'),width='13',bg='orange',fg='black')
        btn_del.place(x=30,y=350,width=200,height=40)

    def add_task(self):
        task = self.txt.get("1.0", "end-1c")  
        if task.strip():  
            self.listbox.insert(END, task)  
            self.txt.delete("1.0", END)  
            self.save_tasks()

    def delete_task(self):
        selected_task_index = self.listbox.curselection()  
        if selected_task_index:  
            self.listbox.delete(selected_task_index)  
            self.save_tasks()

    def save_tasks(self):
        tasks = self.listbox.get(0, END)  
        with open('tasks.txt', 'w') as file:
            for task in tasks:
                file.write(task + '\n')  

    def load_tasks(self):
        try:
            with open('tasks.txt', 'r') as file:
                tasks = file.readlines()
                for task in tasks:
                    self.listbox.insert(END, task.strip())  
        except FileNotFoundError:
            pass

def main():
    root = Tk()
    u1 = todolist(root)
    root.mainloop()

if __name__ == "__main__":
    main()
