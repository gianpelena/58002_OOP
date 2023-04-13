from tkinter import *


class MyWindow:
    def __init__(self, win):
        self.lbl1 = Label(win, text="My Full Name")
        self.lbl1.place(x=200, y=150)
        self.lbl2 = Label(win, text="Enter Given Name: ")
        self.lbl2.place(x=100, y=50)
        self.lbl3 = Label(win, text="Enter Middle Name: ")
        self.lbl3.place(x=100, y=100)
        self.lbl4 = Label(win, text="Enter Last Name: ")
        self.lbl4.place(x=100, y=150)
        self.lbl5 = Label(win, text="My Fullname is: ")
        self.lbl5.place(x=100, y=200)
        self.txt2 = Entry(win, bd=1)
        self.txt2.place(x=300, y=50)
        self.txt3 = Entry(win, bd=1)
        self.txt3.place(x=300, y=100)
        self.txt4 = Entry(win, bd=3)
        self.txt4.place(x=300, y=150)
        self.txt5 = Entry(win, bd=3)
        self.txt5.place(x=200, y=150)
        self.btnadd = Button(win, text="Show Full Name")
        self.btnadd.place(x=100, y=200)
        self.btnadd.bind('<Button-1>', self.add)

    def add(self, add):
        self.txt5.delete(0, 'end')
        name2 = str(self.txt2.get())
        name3 = str(self.txt3.get())
        name4 = str(self.txt4.get())
        name5 = str(self.txt5.get())
        result = name2 + name3 + name4 + name5
        self.txt5.insert(END, str(result))


window = Tk()
mywin = MyWindow(window)
window.geometry("600x400+10+10")
window.title("MIDTERM EXAM PROBLEM 2")
window.mainloop()
