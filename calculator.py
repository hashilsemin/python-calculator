from tkinter import *

window = Tk()
window.geometry('500x500')
window.title('Calculator')
labelarea = Label( window, relief=RAISED)


labelarea.config(height=3, width=40)
labelarea.grid(row=0,column=0)
button7=Button(window,text=7,command='7')

labelarea.pack()
button7.pack()
window.mainloop()