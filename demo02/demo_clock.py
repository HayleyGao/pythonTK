import tkinter as tk
import time

# 创建主窗口
root = tk.Tk()
root.title("Tkinter after 示例")

# 设置窗口大小
root.geometry("300x200")


# 定义显示时间的函数
def showtime():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    # 每隔1000毫秒（1秒）调用一次showtime函数
    label.after(1000, showtime)


# 创建一个Label控件
label = tk.Label(root, text="", width=50, height=30)
label.pack(pady=10)

# 初始化显示时间
showtime()

# 运行主循环
root.mainloop()
