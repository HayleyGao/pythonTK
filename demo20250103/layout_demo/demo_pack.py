from tkinter import *

root = Tk()
root.geometry('400x300+400+200')
root.title('pack布局')

"""
此处写tk框架组件
"""


label1=Label(root,text='label1',bg='purple',fg='blue')
label2=Label(root,text='label2',bg='purple',fg='blue')
btn1=Button(root,text='btn1')
btn2=Button(root,text='btn2')

# 布局方式 pack()
label1.pack(side='left')
label2.pack(side='right')
btn1.pack(side='top')
btn2.pack(side='bottom')


root.mainloop()