from tkinter import *

root = Tk()
root.geometry('400x300+400+200')
root.title('gird布局')


label1=Label(root,text='label1',bg='purple',fg='blue')
label2=Label(root,text='label2',bg='purple',fg='blue')
btn1=Button(root,text='btn1')
btn2=Button(root,text='btn2')
btn3=Button(root,text='btn3')

# 布局方式 gird()
btn1.grid(row=0,column=0,sticky='nsew')
btn2.grid(row=1,column=0,sticky='nsew')
btn3.grid(row=2,column=1,sticky='nsew')
label1.grid(row=3,column=2)
label2.grid(row=4,column=3)

root.mainloop()