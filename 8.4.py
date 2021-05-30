from tkinter import *

def onclick():
    read=open('2.txt','w')
    a1=int(a.get())
    b1=int(b.get())
    read.write(str(-b1/(2*a1)))
    read.close()
    
root=Tk()
root.geometry("500x250")
root.title('using tkinter')

lb=Label(root, text='nhap he so a')
lb.grid(row=0,column=0)
a=StringVar()
ent=Entry(root, textvariable=a)
ent.grid(row=0,column=1)


lb=Label(root, text='nhap he so b')
lb.grid(row=1,column=0)
b=StringVar()
ent=Entry(root, textvariable=b)
ent.grid(row=1,column=1)

btn=Button(root,text='check!',command=onclick)
btn.grid(row=2,column=0)

root.mainloop()
