from tkinter import *

root = Tk()
root.geometry('500x500+400+200')
root.title('Canvas 绘画 demo')

canvas = Canvas(root, bg="#f2e0dc", width=400, height=400)
canvas.pack()

# 创建一条直线
line = canvas.create_line(160, 50, 50, 40, fill="#23407b")

# 创建一个矩形
rectangle = canvas.create_rectangle(80, 100, 250, 200, fill="#aa4926")

# 创建一个椭圆
oval = canvas.create_oval(50, 250, 150, 350, fill="#578933")

# 创建文本
text = canvas.create_text(200, 280, text="Hello World!", fill="#813f09")

# 创建图像
image = PhotoImage(file="HappyDuck.png")
image = image.subsample(4)  # 缩小为原来的1/4

canvas.create_image(340, 300, image=image)

root.mainloop()