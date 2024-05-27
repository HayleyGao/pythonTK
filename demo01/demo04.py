import tkinter as tk

# 定义窗口
window = tk.Tk()
window.title('c语言中文网')
window.geometry('300x300')
window.iconbitmap('C:/Users/Administrator/Desktop/favicon.ico')


# 定义回调函数
def callback():
    print("执行回调函数", "C语言中文网欢迎您")


# 点击执行按钮
button = tk.Button(window, text="执行", command=callback)
button.pack()
window.mainloop()
