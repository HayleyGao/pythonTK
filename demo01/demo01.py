import tkinter as tk

# 创建主窗口
root = tk.Tk()
root.title("Tkinter 示例")

# 设置窗口大小
root.geometry("300x200")


# 定义按钮点击事件处理函数
def on_button_click():
    label.config(text="按钮已点击！")


# 创建一个标签
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=10)

# 创建一个按钮
button = tk.Button(root, text="点击我", command=on_button_click)
button.pack(pady=10)

# 运行主循环
root.mainloop()


