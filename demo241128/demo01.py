import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk


class SimpleEditor:
    def __init__(self):
        # 创建主窗口
        self.root = tk.Tk()
        self.root.title("简单编辑器")
        self.root.geometry("800x600")

        # 设置全局主题
        self.root.tk_setPalette(background='#f0f0f0', foreground='black')

        # 创建当前文件名变量
        self.current_file = None

        # 创建主界面
        self.create_gui()

        # 创建菜单
        self.create_menu()

        # 创建快捷键绑定
        self.create_shortcuts()

        # 创建状态栏
        self.create_status_bar()

    def create_gui(self):
        # 创建文本区域
        self.text_area = tk.Text(
            self.root,
            wrap="word",
            undo=True,
            bg="white",  # 设置背景色为白色
            fg="black"  # 设置文字颜色为黑色
        )
        self.text_area.pack(expand=True, fill="both")

        # 创建滚动条
        scrollbar = ttk.Scrollbar(self.text_area)
        scrollbar.pack(side="right", fill="y")
        self.text_area.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.text_area.yview)

    def create_menu(self):
        # 创建菜单栏
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        # 文件菜单
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="文件", menu=file_menu)
        file_menu.add_command(label="新建", command=self.new_file, accelerator="Ctrl+N")
        file_menu.add_command(label="打开", command=self.open_file, accelerator="Ctrl+O")
        file_menu.add_command(label="保存", command=self.save_file, accelerator="Ctrl+S")
        file_menu.add_command(label="另存为", command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="退出", command=self.quit_application)

        # 编辑菜单
        edit_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="编辑", menu=edit_menu)
        edit_menu.add_command(label="撤销", command=self.text_area.edit_undo, accelerator="Ctrl+Z")
        edit_menu.add_command(label="重做", command=self.text_area.edit_redo, accelerator="Ctrl+Y")
        edit_menu.add_separator()
        edit_menu.add_command(label="剪切", command=lambda: self.text_area.event_generate("<<Cut>>"))
        edit_menu.add_command(label="复制", command=lambda: self.text_area.event_generate("<<Copy>>"))
        edit_menu.add_command(label="粘贴", command=lambda: self.text_area.event_generate("<<Paste>>"))

    def create_shortcuts(self):
        # 绑定快捷键
        self.root.bind('<Control-n>', lambda e: self.new_file())
        self.root.bind('<Control-o>', lambda e: self.open_file())
        self.root.bind('<Control-s>', lambda e: self.save_file())

    def create_status_bar(self):
        # 创建状态栏
        self.status_bar = ttk.Label(self.root, text="就绪", anchor="w")
        self.status_bar.pack(side="bottom", fill="x")

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.current_file = None
        self.status_bar.config(text="新文件")

    def open_file(self):
        file = filedialog.askopenfile(
            defaultextension=".txt",
            filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")]
        )
        if file:
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(1.0, file.read())
            self.current_file = file.name
            self.status_bar.config(text=f"已打开: {self.current_file}")
            file.close()

    def save_file(self):
        if self.current_file:
            try:
                content = self.text_area.get(1.0, tk.END)
                with open(self.current_file, 'w', encoding='utf-8') as file:
                    file.write(content)
                self.status_bar.config(text=f"已保存: {self.current_file}")
            except Exception as e:
                messagebox.showerror("保存错误", str(e))
        else:
            self.save_as_file()

    def save_as_file(self):
        file = filedialog.asksaveasfile(
            defaultextension=".txt",
            filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")]
        )
        if file:
            content = self.text_area.get(1.0, tk.END)
            file.write(content)
            self.current_file = file.name
            self.status_bar.config(text=f"已保存: {self.current_file}")
            file.close()

    def quit_application(self):
        if messagebox.askokcancel("退出", "确定要退出吗？"):
            self.root.quit()

    def run(self):
        self.root.mainloop()


# 创建并运行应用
if __name__ == "__main__":
    editor = SimpleEditor()
    editor.run()
