from tkinter import *

root = Tk()
root.geometry('400x300+400+200')
root.title('pack布局')

menubar=Menu(root) # Menu()是用于创建菜单的小部件。
filemenu=Menu(menubar,tearoff=0,bg='#2a2d30', fg='#bbbbbb')


menubar.add_cascade(label='文件',menu=filemenu)  ## 添加一个级联菜单，label为显示的文本，menu为级联的子菜单
filemenu.add_command(label='打开',activebackground='red', activeforeground='#323233')
filemenu.add_separator() # 添加一个分割线
filemenu.add_command(label='保存') # 添加一个普通菜单项


root.config(menu=menubar)
# 在Python的Tkinter库中，config()方法是用于配置或更新小部件（widget）属性的方法。
# root.config(menu=menubar)这行代码的作用是将一个菜单栏（menubar）配置到主窗口（root）上。

root.mainloop()