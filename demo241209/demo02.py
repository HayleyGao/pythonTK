import tkinter as tk
from tkinter import ttk
import threading
import time
from queue import Queue, Empty


def long_running_task(task_id, queue):
    # 模拟不同耗时的操作
    time.sleep(2 + task_id)
    # 将结果放入队列
    queue.put(f"任务 {task_id} 完成")


def check_queue():
    try:
        while True:
            # 从队列中获取消息
            msg = queue.get_nowait()
            # 更新标签的文本
            result_label.config(text=result_label.cget("text") + "\n" + msg)
    except Empty:
        pass
    # 每100毫秒检查一次队列
    root.after(100, check_queue)


def start_tasks():
    # 启动多个线程来执行耗时任务
    for i in range(3):  # 创建三个线程
        threading.Thread(target=long_running_task, args=(i, queue)).start()


# 创建主窗口
root = tk.Tk()
root.title("多线程示例")

# 创建一个标签显示任务结果
result_label = tk.Label(root, text="任务结果:")
result_label.pack(pady=10)

# 创建一个按钮，并绑定开始任务的事件
start_button = ttk.Button(root, text="开始任务", command=start_tasks)
start_button.pack(pady=10)

# 创建一个队列用于线程间通信
queue = Queue()

# 使用after方法定期检查队列
root.after(100, check_queue)

# 启动主事件循环
root.mainloop()
