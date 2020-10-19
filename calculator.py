from tkinter import *

window = Tk()
window.geometry('330x300')
window.title('Calculator')
def clicked(num):
    first_num=e.get()
    e.delete(0,END)
    e.insert(0,str(first_num)+str(num))
def add():

    first_number=e.get()
    global old_value
    old_value=int(first_number)
    global math
    math="addition"
    e.delete(0,END)
def minus():

    first_number=e.get()
    global old_value
    old_value=int(first_number)
    global math
    math="minus"
    e.delete(0,END)
def div():

    first_number=e.get()
    global old_value
    old_value=int(first_number)
    global math
    math="division"
    e.delete(0,END)
def mul():

    first_number=e.get()
    global old_value
    old_value=int(first_number)
    global math
    math="multiplication"
    e.delete(0,END)
def equal():
    if math=="addition":
            new_value=e.get()
            e.delete(0,END)
            e.insert(0,int(old_value)+int(new_value))
    if math=="minus":
            new_value=e.get()
            e.delete(0,END)
            e.insert(0,int(old_value)-int(new_value))
    if math=="division":
            new_value=e.get()
            e.delete(0,END)
            e.insert(0,int(old_value)/int(new_value))
    if math=="multiplication":
            new_value=e.get()
            e.delete(0,END)
            e.insert(0,int(old_value)*int(new_value))
def clear():
    e.delete(0,END)

e=Entry(window,bg="white")
e.grid(row=0,column=0,columnspan=10,sticky=W+E,padx=10,pady=5,ipady=15)
b1=Button(window,text="1",height=2,width=2,command=lambda:clicked(1))
b2=Button(window,text="2",height=2,width=2,command=lambda:clicked(2))
b3=Button(window,text="3",height=2,width=2,command=lambda:clicked(3))
b4=Button(window,text="4",height=2,width=2,command=lambda:clicked(4))
b5=Button(window,text="5",height=2,width=2,command=lambda:clicked(5))
b6=Button(window,text="6",height=2,width=2,command=lambda:clicked(6))
b7=Button(window,text="7",height=2,width=2,command=lambda:clicked(7))
b8=Button(window,text="8",height=2,width=2,command=lambda:clicked(8))
b9=Button(window,text="9",height=2,width=2,command=lambda:clicked(9))
bdot=Button(window,text=".",height=2,width=2,command=lambda:clicked('.'))
bzero=Button(window,text="0",height=2,width=2,command=lambda:clicked(0))
bequal=Button(window,text="=",height=2,width=2,bg='#eb641c',command=equal)
badd=Button(window,text="+",height=2,width=2,command=add)
bminus=Button(window,text="-",height=2,width=2,command=minus)
bmul=Button(window,text="x",height=2,width=2,command=mul)
bdiv=Button(window,text="/",height=2,width=2,command=div)
bclear=Button(window,text="clr",height=2,width=2,bg='#eb641c',command=clear)
b1.grid(row=1,column=0,padx=10,pady=5)
b2.grid(row=1,column=1,padx=10,pady=5)
b3.grid(row=1,column=2,padx=10,pady=5)
b4.grid(row=2,column=0,padx=10,pady=5)
b5.grid(row=2,column=1,padx=10,pady=5)
b6.grid(row=2,column=2,padx=10,pady=5)
b7.grid(row=3,column=0,padx=10,pady=5)
b8.grid(row=3,column=1,padx=10,pady=5)
b9.grid(row=3,column=2,padx=10,pady=5)
bdot.grid(row=4,column=0,padx=10,pady=5)
bzero.grid(row=4,column=1,padx=10,pady=5)
bequal.grid(row=4,column=2,padx=10,pady=5)
badd.grid(row=1,column=4,padx=10,pady=5)
bminus.grid(row=2,column=4,padx=10,pady=5)
bmul.grid(row=3,column=4,padx=10,pady=5)
bdiv.grid(row=4,column=4,padx=10,pady=5)
bclear.grid(row=1,column=5,padx=10,pady=5)

window.mainloop()