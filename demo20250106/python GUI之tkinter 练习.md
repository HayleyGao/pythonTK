# python tkinter 练习



## Part1:记事本实现案例

记事本的实现：

https://zhuanlan.zhihu.com/p/491088128

https://zhuanlan.zhihu.com/p/491088128





实现思路：

1、确定GUI上实现的功能：新建、打开、保存、复制剪切粘贴

2、实现思路：

	- 创建窗口
	- 设定记事本的菜单项
	- 配置菜单项的功能选项
	- 运行记事本

3、实现代码

 - 创建窗口

   ```text
   root=Tk() #创建窗口
   TextArea:文本区域
   MenuBar:菜单栏
   
   FileMenu:文件菜单
   EditMenu:编辑菜单
   HelpMenu:帮助菜单
   ScrollBat:滚动条
   ```

 - 设定菜单项

   ```text
   self.FileMenu.add_command(label="新建", command=self.__newFile) # 新建、打开、保存
   ```

- 构建功能函数

  ```text
  def __newFile(self):
      '''
      新文件：默认是一个未命名文件
      '''
      self.root.title("未命名文件")
      self.file = None
      self.TextArea.delete(1.0, END)
  ```



---





```
def __saveFile(self): 
        ''' 
        用于保存文件，不存在的文件进行新建，存在的文件在原文件基础上覆盖保存 
        ''' 
        if self.file == None: 
            self.file = asksaveasfilename(initialfile='Untitled.txt', 
                                          defaultextension=".txt", 
                                          filetypes=[("All Files", "*.*"), 
                                                     ("Text Documents", 
                                                      "*.txt")]) 
            if self.file == "": 
                self.file = None 
            else: 
                file = open(self.file, "w") 
                file.write(self.TextArea.get(1.0, END)) 
                file.close() 
                # 更改title名字为文件名 
                self.root.title(os.path.basename(self.file)) 
        else: 
            file = open(self.file, "w") 
            file.write(self.TextArea.get(1.0, END)) 
            file.close() 

```

解释上述这段代码



这段代码定义了一个名为`__saveFile`的方法，用于保存文本文件。以下是代码的详细解释：

1. **方法定义**: `__saveFile(self)` 是一个实例方法，通常用于保存用户在文本编辑器中输入的内容。

2. **检查文件是否存在**:
   - `if self.file == None:` 检查当前文件是否未定义（即尚未保存到一个文件中）。
   
3. **文件保存对话框**:
   - `self.file = asksaveasfilename(...)` 调用文件保存对话框，允许用户选择保存文件的路径和名称。
   - `initialfile='Untitled.txt'` 设置默认文件名为 "Untitled.txt"。
   - `defaultextension=".txt"` 设置默认文件扩展名为 ".txt"。
   - `filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")]` 指定文件类型过滤器，允许用户选择所有文件或仅限文本文件。

4. **检查用户输入**:
   - `if self.file == "":` 检查用户是否取消了保存操作。如果取消，`self.file` 将被设置为 `None`。
   
5. **保存文件**:
   - `file = open(self.file, "w")` 打开用户指定的文件路径，以写入模式（"w"）打开文件。
   - `file.write(self.TextArea.get(1.0, END))` 将文本区域中的内容写入文件。`self.TextArea.get(1.0, END)` 获取文本区域从第一个字符到结尾的所有文本。
   - `file.close()` 关闭文件，确保所有数据写入磁盘。

6. **更新窗口标题**:
   - `self.root.title(os.path.basename(self.file))` 将窗口标题更新为保存的文件名。

7. **覆盖保存**:
   - 如果文件已经存在（即 `self.file` 不为 `None`），则直接打开文件并覆盖保存。

这段代码通常用于简单的文本编辑器应用中，提供了基本的文件保存功能。



---



```
# 添加功能项 
    def __cut(self): 
        self.TextArea.event_generate("<<Cut>>") 
    def __copy(self): 
        self.TextArea.event_generate("<<Copy>>") 
    def __paste(self): 
        self.TextArea.event_generate("<<Paste>>") 
解释上述这段代码
```



这段代码定义了三个方法，分别用于实现剪切、复制和粘贴功能，通常在文本编辑器应用中使用。这些方法利用了 Tkinter 库中的事件生成机制。以下是对每个方法的详细解释：

1. **剪切功能**: `__cut(self)`
   - `self.TextArea.event_generate("<<Cut>>")` 生成一个剪切事件，作用于 `TextArea` 组件。
   - 这个方法会将用户选中的文本剪切到剪贴板中，并从文本区域中删除该文本。

2. **复制功能**: `__copy(self)`
   - `self.TextArea.event_generate("<<Copy>>")` 生成一个复制事件，作用于 `TextArea` 组件。
   - 这个方法会将用户选中的文本复制到剪贴板中，但不会从文本区域中删除该文本。

3. **粘贴功能**: `__paste(self)`
   - `self.TextArea.event_generate("<<Paste>>")` 生成一个粘贴事件，作用于 `TextArea` 组件。
   - 这个方法会从剪贴板中获取文本，并将其插入到文本区域的当前光标位置。

这些方法通过调用 Tkinter 的内置事件来实现基本的编辑操作，简化了对文本的处理，并提供了用户熟悉的编辑体验。



## Part2:事件机制案例



### Part2.1 tk如何指定事件处理程序

事件发生机制：

https://blog.csdn.net/cnds123/article/details/127411016

https://blog.csdn.net/cnds123/article/details/127411016



控件（widget：组件、小部件、控件）



Tkinter如何指定事件处理程序

一、在创建控件对象时，可以使用控件中的command参数指定事件处理程序：command=函数，那么点击控件的时候将会触发函数。

二、还可以使用绑定（binding）方法指定事件处理程序，Tkinter可以在以下三个级别将事件处理程序绑定（binding）到事件
原文链接：https://blog.csdn.net/cnds123/article/details/127411016

在 Tkinter 中，可以使用 `bind` 方法来实现事件绑定，主要有以下几种方式：

1. **直接绑定事件类型**：可以将事件类型（如鼠标点击、键盘按键等）直接绑定到某个控件上。使用 `bind` 方法时，需要指定事件类型字符串和回调函数。例如：
   
   ```python
   widget.bind("<Button-1>", callback_function)
   ```
   
2. **使用事件序列**：事件序列可以定义更复杂的事件组合，例如 `<Control-Shift-KeyPress-A>` 表示同时按下 Control、Shift 和 A 键。绑定方式与直接绑定类似：
   
   ```python
   widget.bind("<Control-Shift-KeyPress-A>", callback_function)
   ```
   
3. **绑定到事件的类**：可以将事件绑定到某个控件类的所有实例上，这样所有该类的实例都会响应事件。例如，绑定所有按钮的点击事件：
   
   ```python
   tk.Button.bind_class("Button", "<Button-1>", callback_function)
   ```
   
4. **绑定到顶层窗口**：可以将事件绑定到顶层窗口，这样窗口中的所有控件都会响应该事件。例如，绑定键盘按键事件：
   ```python
   root.bind_all("<KeyPress>", callback_function)
   ```

5. **使用 lambda 表达式**：为了在回调函数中传递额外参数，可以使用 lambda 表达式：
   ```python
   widget.bind("<Button-1>", lambda event: callback_function(event, extra_param))
   ```

这些方法可以根据具体的需求选择使用，以实现灵活的事件处理。



### Part2.2 事件处理方法的比较

在 Tkinter 中，指定事件处理有两种常用的方法：`command` 方法和 `bind` 方法。它们用于不同的场景和控件类型。

#### `command` 方法

`command` 方法主要用于按钮（`Button`）、菜单项（`Menu`）等控件。它用于绑定控件的默认动作，例如按钮的点击。使用 `command` 方法时，你只需要指定一个回调函数，当控件被激活时，这个函数会被调用。

```python
import tkinter as tk

def on_button_click():
    print("Button clicked!")

root = tk.Tk()
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack()

root.mainloop()
```

在这个例子中，当按钮被点击时，`on_button_click` 函数会被调用。

#### `bind` 方法

`bind` 方法用于绑定更广泛的事件类型，例如键盘输入、鼠标移动、鼠标点击等。通过 `bind` 方法，你可以指定事件类型和相应的处理函数。

```python
import tkinter as tk

def on_key_press(event):
    print(f"Key pressed: {event.char}")

root = tk.Tk()
root.bind("<KeyPress>", on_key_press)

root.mainloop()
```

在这个例子中，当用户在窗口中按下任意键时，`on_key_press` 函数会被调用，并输出按下的键。

### 区别

- `command` 方法更简单，通常用于处理控件的主要动作，比如按钮点击。
- `bind` 方法更灵活，可以处理各种事件类型，不仅限于控件的默认动作。

选择使用哪种方法取决于具体的需求。如果只是处理按钮点击等简单事件，使用 `command` 方法更为方便；如果需要处理更复杂的事件，如键盘和鼠标事件，则需要使用 `bind` 方法。