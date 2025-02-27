from tkinter import *
root=Tk()
root.geometry("733x434")
def hello():
    print("hello")

def name():
    n=input("enter your name")
    print("hello",n)

f1=Frame(root,bg="grey",borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT,fill="y")
b1=Button(f1,text="print now", command=hello)
b1.pack(side=LEFT,padx=5,pady=5)

f2=Frame(root,bg="grey",borderwidth=8,relief=SUNKEN)
f2.pack(side=TOP,fill="x")
b2=Button(f2,text="your command", command=name)
b2.pack(side=RIGHT,padx=5,pady=5)
lab1=Label(f2,text="title",font="Helvetica 16 bold",fg="red",pady=2)
lab1.pack(padx=20)
f3=Frame(root,bg="grey",borderwidth=8,relief=SUNKEN)
f3.pack(side=BOTTOM)
lab2=Label(f3,text="body of loop",font="Helvetica 16 bold",fg="red",pady=1,anchor=CENTER)
lab2.pack(pady=700,padx=500)

lab=Label(f1,text="Project Tkinter - Pycharm",font="Helvetica 16 bold",fg="red",pady=1)
lab.pack(pady=1)
root.mainloop()
