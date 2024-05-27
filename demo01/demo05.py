import tkinter as tk

window = tk.Tk()
window.title('c语言中文网')
window.iconbitmap('C:/Users/Administrator/Desktop/favicon.ico')
# 设置窗口大小变量
width = 300
height = 300
# 窗口居中，获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
size_geo = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)
window.geometry(size_geo)
window.mainloop()