from tkinter import *

def onclick():
    ent.configure(bg=v.get())
    
a=Tk()
a.geometry("500x250")
a.title('using tkinter')

s=StringVar()
s.set("hello Python!")
lb=Label(a, textvariable=s)
lb.place(x=50,y=50)

v=StringVar()
ent=Entry(a, textvariable=v)
ent.place(x=150,y=100)

btn=Button(a,text='click!',command=onclick)
btn.place(x=50,y=100)

a.mainloop()
