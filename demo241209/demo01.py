import tkinter as tk
from tkinter import ttk
import threading
import time
from queue import Queue, Empty


def long_running_task(queue):
    # 模拟耗时操作
    time.sleep(5)
    # 将结果放入队列
    queue.put("任务完成")


def check_queue():
    try:
        # 从队列中获取消息
        msg = queue.get_nowait()
        # 更新标签的文本
        label.config(text=msg)
    except Empty:
        pass
    # 每100毫秒检查一次队列
    root.after(100, check_queue)


def start_task():
    # 启动一个新线程来执行耗时任务
    threading.Thread(target=long_running_task, args=(queue,)).start()


# 创建主窗口
root = tk.Tk()
root.title("多线程示例")

# 创建一个标签
label = tk.Label(root, text="等待任务完成...")
label.pack(pady=10)

# 创建一个按钮，并绑定开始任务的事件
start_button = ttk.Button(root, text="开始任务", command=start_task)
start_button.pack(pady=10)

# 创建一个队列用于线程间通信
queue = Queue()

# 使用after方法定期检查队列
root.after(100, check_queue)

# 启动主事件循环
root.mainloop()
