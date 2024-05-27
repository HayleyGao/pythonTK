from tkinter import *
# 定义事件函数，必须用event参数
def show_key(event):
    # 查看触发事件的按钮
    s=event.keysym
    # 将其显示在按钮控件上
    lb.config(text=s)

root=Tk()
root.config(bg='#87CEEB')
root.title("C语言中文网")
root.geometry('450x350+300+200')
root.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
# 添加一个按钮控件
lb=Label(root,text='请按键',fg='blue',font=('微软雅黑',15))
# 给按钮控件绑定事件，按下任意键，然后调用事件处理函数。注意，此处需要在英文状态下进行输入
lb.bind('<Key>',show_key)
# 设置按钮获取焦点
lb.focus_set()
lb.pack()
# 显示窗口
root.mainloop()

