from tkinter import*
import tkinter.font as fnt
from tkinter import messagebox,Entry
import time

root = Tk()
root.geometry("500x500")



def sign():
    global root
    root.destroy()
    root=Tk()
    root.geometry("500x500")

    def coni1():
    
        value= entry.get()
        value2=passi.get()
        
        if value and value2:
            if len(value)>4:
                messagebox.showinfo("Info","Added")
                        
            elif len(value)<4:
                    messagebox.showerror("Error","password need to be more than 4 chracters")
                
        else:
            messagebox.showerror("Error","UserName or Password is empty")

    
    btn11 = Button(root,width=30,height=1,font=fnt.Font(size=10)
    ,text="Coniform",command = coni1)
    btn11.pack()
    btn11.place(x=230,y=200)
    

    
    label11=Label(root,text="username")
    label12=Label(root,text="password")

    
    label11.place(x=150,y=100)
    label12.place(x=150,y=150)

    
    entry = Entry(root,font=('Helevetica',12),width=20,bg='lightblue')
    entry.pack()
    entry.place(x=250,y=100)
    
    
    passi = Entry(root,font=('Helevetica',12),width=20,bg='lightblue')
    passi.place(x=250,y=150)

    
            

btn1 = Button(root,height=2,width=15,font=fnt.Font(size=10),text="sign in",command=sign)
btn2 = Button(root,height=2,width=15,font=fnt.Font(size=10),text="Log in")
btn1.place(x=150,y=250)
btn2.place(x=300,y=250)
