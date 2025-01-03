import tkinter as tk
from tkinter import ttk
import asyncio
import threading
import random

# 创建一个新的事件循环
async_loop = asyncio.new_event_loop()


def start_async_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


async def long_running_task(task_id, result_var, task_done):
    # 显示任务开始的信息
    result_var.set(result_var.get() + f"\n任务 {task_id} 开始执行")
    # 随机模拟不同的异步耗时操作
    delay = random.uniform(1, 5)
    await asyncio.sleep(delay)
    # 更新结果
    result_var.set(result_var.get() + f"\n任务 {task_id} 完成 (耗时: {delay:.2f}秒)")
    task_done[task_id] = True
    # 检查所有任务是否完成
    if all(task_done):  # 检查 task_done 列表中的所有元素是否都为 True
        result_var.set(result_var.get() + "\n所有任务已完成。")


def start_tasks():
    # 仅在任务开始时添加新行提示
    result_var.set(result_var.get() + "\n\n开始新的任务组:")
    task_done[:] = [False] * 3  # 重置任务完成状态
    # 为每个任务创建一个异步任务
    for i in range(3):
        asyncio.run_coroutine_threadsafe(long_running_task(i, result_var, task_done), async_loop)


def clear_label():
    result_var.set("")


# 创建主窗口
root = tk.Tk()
root.title("异步编程示例")

# 创建一个StringVar用于显示任务结果
result_var = tk.StringVar(value="任务结果:")
result_label = tk.Label(root, textvariable=result_var, justify='left')
result_label.pack(pady=10)

# 创建一个按钮，并绑定开始任务的事件
start_button = ttk.Button(root, text="开始任务", command=start_tasks)
start_button.pack(pady=10)

# 创建一个清空按钮
clear_button = ttk.Button(root, text="清空", command=clear_label)
clear_button.pack(pady=10)

# 任务完成状态列表
task_done = [False] * 3

# 在一个单独的线程中启动异步事件循环
threading.Thread(target=start_async_loop, args=(async_loop,), daemon=True).start()

# 启动主事件循环
root.mainloop()
