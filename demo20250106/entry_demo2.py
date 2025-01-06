from tkinter import *

root = Tk()
root.geometry('500x500+400+200')
root.title('胖兔always')

entry = Entry(root)
entry.pack()


def configure_entry():
    entry.config(bg="yellow", fg="blue", font=("Arial", 12)) # 按下button触发事件，config设置


button = Button(root, text="配置Entry", command=configure_entry)
button.pack()

root.mainloop()