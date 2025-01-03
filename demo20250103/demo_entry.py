from tkinter import *

root = Tk()
root.geometry('400x300+400+200')
root.title('pack布局')



# 创建一个StringVar对象
text_var=StringVar()

# 将StringVar对象于Entry对象关联
entry1=Entry(root,textvariable=text_var,width=35,show='*')  # Entry单行文本框
entry1.pack()


def get_text():
    text=text_var.get()
    print("用户输入的文本是："+text)


btn=Button(root,text='获取文本',command=get_text) #

label1=Label(root,text='label1',bg='purple',fg='blue')
label2=Label(root,text='label2',bg='purple',fg='blue')
btn1=Button(root,text='btn1')
btn2=Button(root,text='btn2')



# 布局方式 pack()
btn.pack()
label1.pack(side='left')
label2.pack(side='right')
btn1.pack(side='top')
btn2.pack(side='bottom')



root.mainloop()