import tkinter
import datetime
from tkinter import messagebox
from tkinter import simpledialog

def start_countdown():
    msg = messagebox.askquestion(title="提示", message="是否使用默认10s的倒计时？")

    if msg == "yes":
        print("使用默认倒计时")
        seconds = 10
    else:
        print("使用用户自定义倒计时")
        seconds = simpledialog.askinteger(title="提示", prompt="请输入倒计时时间")
    countdown(seconds)


def countdown(seconds):
    if seconds <= 0:
        str_var.set("时间到!")
    else:
        str_var.set(str(seconds))
        root.after(1000, countdown, seconds - 1)  # after()非阻塞

root = tkinter.Tk()
root.title("Countdown GUI")
root.geometry("640x480")

str_var = tkinter.StringVar()
str_var.set(str(datetime.datetime.now()))  # 默认为当前时间

label = tkinter.Label(root, textvariable=str_var)
label.pack()

btn = tkinter.Button(root, text="开始倒计时", command=lambda: start_countdown())
btn.pack()

root.mainloop()