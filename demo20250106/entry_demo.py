from tkinter import *

root = Tk()
root.geometry('500x500+400+200')

# 创建一个StringVar对象
text_var = StringVar()

# 将StringVar对象与Entry小部件关联
entry = Entry(root, textvariable=text_var, width=30, show="*")
entry.pack()

def get_text():
    text = text_var.get()
    print("用户输入的文本是:", text)
    label1.config(text=text)  # config()方法更新label1的文本内容
    return text

button = Button(root, text="获取文本", command=get_text)
button.pack()

label1 = Label(root, bg="yellow", width=30)
label1.pack()

root.mainloop()