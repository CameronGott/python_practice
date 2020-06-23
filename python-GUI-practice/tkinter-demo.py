#https://docs.python.org/3/library/tk.html
from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("800x600")
def helloCallBack():
    msg = messagebox.showinfo("Hello Python", "Hello World")
#Stats frame
statsFrame = Frame(top, height = "200", width = "100", bg = "black")
statsFrame.place(x = 0, y = 0)
B = Button(statsFrame, text="Hello", command=helloCallBack)
B.place(x=0, y=0)



top.mainloop()