import tkinter
import datetime



root = tkinter.Tk()
root.title("Countdown GUI")
root.geometry("640x480")

str_var = tkinter.StringVar()
str_var.set(str(datetime.datetime.now()))  # 默认为当前时间

def countdown(seconds=10):
    if seconds <= 0:
        str_var.set("时间到!")
    else:
        str_var.set(str(seconds))
        root.after(1000, countdown, seconds - 1) # after()非阻塞

label = tkinter.Label(root, textvariable=str_var)
label.pack()

btn = tkinter.Button(root, text="开始倒计时", command=lambda: countdown(10))
btn.pack()

root.mainloop()