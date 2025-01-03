from tkinter import *

root = Tk()
root.geometry('400x300+400+200')
root.title('place布局')


label1=Label(root,text='label1',bg='purple',fg='blue')
label2=Label(root,text='label2',bg='purple',fg='blue')
btn1=Button(root,text='btn1')
btn2=Button(root,text='btn2')


# 布局方式 place()
label1.place(x=10,y=10)
label2.place(x=50,y=50)
btn1.place(x=90,y=90)
btn2.place(x=120,y=120)



root.mainloop()