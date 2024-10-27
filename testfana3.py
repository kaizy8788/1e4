from tkinter import*
from tkinter import messagebox,simpledialog
from tkinter import font as fnt


root = Tk()
root.geometry("300x200")
root.title("کدام پايه؟")

values = {"هفتم " : "7",
          "هشتم " : "8",
          "نهم " : "9",}


v = StringVar(root, "1")

for (text, value) in values.items():
   Radiobutton(root, text = text, variable = v,
               value = value, indicator = 0,
               background = "light blue").pack(fill = X, ipady = 5)

def rdbtnc():
    v12=v.get()
    print(v12)
    if v12==7:
        pass
    elif v12==8:
        pass
    elif v12 == 9:
        pass
    else:
        messagebox.showerror("خطا","انتخاب نکرديد")

btn1=Button(root,font=fnt.Font(size=20),bg="black",fg="white",height=2,width=20,text="تاييد",command=rdbtnc)
btn1.place(x=-10,y=106)
