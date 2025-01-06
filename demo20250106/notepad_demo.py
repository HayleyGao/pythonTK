import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

# example from:
# https://zhuanlan.zhihu.com/p/491088128

class Notepad:
    root = Tk()
    '''
    Width:宽度
    Heith:高度
    TextArea:文本区域
    MenuBar:菜单栏
    FileMenu:文件菜单
    EditMenu:编辑菜单
    HelpMenu:帮助菜单
    ScrollBat:滚动条
    '''
    Width = 300
    Height = 300
    TextArea = Text(root)
    MenuBar = Menu(root)
    FileMenu = Menu(MenuBar, tearoff=0)
    EditMenu = Menu(MenuBar, tearoff=0)
    HelpMenu = Menu(MenuBar, tearoff=0)
    ScrollBar = Scrollbar(TextArea)
    file = None
    def __init__(self, **kwargs):
        # 设置文本框的大小
        try:
            self.Width = kwargs['width']
        except KeyError:
            pass
        try:
            self.Height = kwargs['height']
        except KeyError:
            pass
        # 设置窗口标题
        self.root.title("Python记事本")
        # 将窗口居中显示
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()
        left = (screenWidth / 2) - (self.Width / 2)
        top = (screenHeight / 2) - (self.Height / 2)
        self.root.geometry('%dx%d+%d+%d' %
                           (self.Width, self.Height, left, top))
        # 文本区域大小调整
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        # Add controls (widget)
        self.TextArea.grid(sticky=N + E + S + W)
        # 增加新建配置
        self.FileMenu.add_command(label="新建", command=self.__newFile)
        # 增加打开配置
        self.FileMenu.add_command(label="打开", command=self.__openFile)
        # 增加保存配置
        self.FileMenu.add_command(label="保存", command=self.__saveFile)
        # 增加退出配置
        self.FileMenu.add_separator()
        self.FileMenu.add_command(label="退出", command=self.__quitApplication)
        # 菜单中设置文件按钮
        self.MenuBar.add_cascade(label="文件", menu=self.FileMenu)
        # 增加剪切功能
        self.EditMenu.add_command(label="剪切", command=self.__cut)
        # 增加复制功能
        self.EditMenu.add_command(label="复制", command=self.__copy)
        # 增加粘贴功能
        self.EditMenu.add_command(label="粘贴", command=self.__paste)
        # 菜单中设置编辑按钮
        self.MenuBar.add_cascade(label="编辑", menu=self.EditMenu)
        # 增加关于记事本选项
        self.HelpMenu.add_command(label="关于记事本", command=self.__showAbout)
        # 菜单中射者帮助按钮
        self.MenuBar.add_cascade(label="帮助", menu=self.HelpMenu)
        self.root.config(menu=self.MenuBar)
        self.ScrollBar.pack(side=RIGHT, fill=Y)
        # 滚动条根据内容进行调整
        self.ScrollBar.config(command=self.TextArea.yview)
        self.TextArea.config(yscrollcommand=self.ScrollBar.set)
    def __quitApplication(self):
        '''
        用于退出程序（关了就消失）
        '''
        self.root.destroy()
    def __showAbout(self):
        '''
        添加帮助菜单中的信息
        '''
        showinfo("关于记事本", "来自:二哥不像程序员")
    def __openFile(self):
        '''
        打开文件
        '''
        self.file = askopenfilename(defaultextension=".txt",
                                    filetypes=[("All Files", "*.*"),
                                               ("Text Documents", "*.txt")])
        if self.file == "":
            self.file = None
        else:
            self.root.title(os.path.basename(self.file))
            self.TextArea.delete(1.0, END)
            file = open(self.file, "r")
            self.TextArea.insert(1.0, file.read())
            file.close()
    def __newFile(self):
        '''
        新文件：默认是一个未命名文件
        '''
        self.root.title("未命名文件")
        self.file = None
        self.TextArea.delete(1.0, END)
    def __saveFile(self):
        '''
        用于保存文件，不存在的文件进行新建，存在的文件在原文件基础上覆盖保存
        '''
        if self.file == None:
            self.file = asksaveasfilename(initialfile='Untitled.txt',
                                          defaultextension=".txt",
                                          filetypes=[("All Files", "*.*"),
                                                     ("Text Documents",
                                                      "*.txt")])
            if self.file == "":
                self.file = None
            else:
                file = open(self.file, "w")
                file.write(self.TextArea.get(1.0, END))
                file.close()
                # 更改title名字为文件名
                self.root.title(os.path.basename(self.file))
        else:
            file = open(self.file, "w")
            file.write(self.TextArea.get(1.0, END))
            file.close()
    # 添加功能项
    def __cut(self):
        self.TextArea.event_generate("<<Cut>>")
    def __copy(self):
        self.TextArea.event_generate("<<Copy>>")
    def __paste(self):
        self.TextArea.event_generate("<<Paste>>")
    def run(self):
        # 使用mainloop()使得窗口一直存在
        self.root.mainloop()

notepad = Notepad(width=600, height=400)
notepad.run()