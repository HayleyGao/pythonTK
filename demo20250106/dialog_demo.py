import tkinter as tk
from tkinter import simpledialog

def get_user_input():
    # 弹出输入框，要求用户输入一个字符串
    user_input = simpledialog.askstring("输入", "请输入一些文本：")
    if user_input is not None:
        print("用户输入：", user_input)
    else:
        print("用户取消输入")


root = tk.Tk()
root.title("输入框示例")
root.geometry("300x200")

# 创建一个按钮，点击时弹出输入框
button = tk.Button(root, text="弹出输入框", command=get_user_input)
button.pack(pady=20)

root.mainloop()