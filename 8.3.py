from tkinter import *
from math import *

def onclick():
    read=open('1.txt','w')
    a1=int(a.get())
    b1=int(b.get())
    c1=int(c.get())
    denta=b1*b1-4*a1*c1
    if denta>0:
        x1=(-b1- sqrt(denta))/2*a1
        x2=(-b1+ sqrt(denta))/2*a1
        read.write(str(x1))
        read.write(',')
        read.write(str(x2))
    elif denta==0:
        x=(-b1/2*a1)
        read.write(str(x))
    else:
        read.write('phuong trinh vo nghiem')
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

lb=Label(root, text='nhap he so c')
lb.grid(row=2,column=0)
c=StringVar()
ent=Entry(root, textvariable=c)
ent.grid(row=2,column=1)


btn=Button(root,text='check!',command=onclick)
btn.grid(row=3,column=0)

root.mainloop()
