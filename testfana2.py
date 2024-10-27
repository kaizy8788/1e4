from tkinter import*
from tkinter import messagebox,simpledialog
from tkinter import font




root = Tk()
root.geometry("500x500")

v = StringVar(root, "1")
 

values = {"هفتم " : "7",
          "هشتم " : "8",
          "نهم " : "9",}
 

##for (text, value) in values.items():
##    Radiobutton(root, text = text, variable = v, 
##                value = value, indicator = 0,
##                background = "light blue").pack(fill = Y, ipady = 5)

label1=Label(root,font=(15),text="name")
label1.place(x=100,y=100)


##label2=Label(root,font=(15),text="paye")
##label2.place(x=100,y=200)

label3=Label(root,font=(15),text="nomre")
label3.place(x=100,y=300)



name=Entry(root,width=10,font=(10))
name.place(x=200,y=100)

##btn1=Radiobutton(root,text="haftom")
##btn1.place(x=200,y=200)
##
##
##btn2=Radiobutton(root,text="hashtom")
##btn2.place(x=270,y=200)
##
##
##
##btn3=Radiobutton(root,text="nohom")
##btn3.place(x=350,y=200)






nomre=Entry(root,width=10,font=(10))
nomre.place(x=200,y=300)
