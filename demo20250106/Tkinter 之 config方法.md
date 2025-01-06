Tkinter 之 config方法



在 Tkinter 中，`config` 方法（也可以使用 `configure`，它们是等价的）用于修改控件（如按钮、标签、框架等）的属性。通过 `config` 方法，你可以动态地改变控件的外观和行为。

### 使用说明

`config` 方法的基本用法如下：

```python
widget.config(option1=value1, option2=value2, ...)
```

或者：

```python
widget.configure(option1=value1, option2=value2, ...)
```

### 常见用法

1. **修改文本**：可以用来更新标签或按钮的文本。
   ```python
   label.config(text="新文本")
   ```

2. **修改颜色**：可以用来改变控件的背景色或前景色。
   ```python
   button.config(bg="blue", fg="white")
   ```

3. **修改字体**：可以用来改变文本的字体类型和大小。
   ```python
   label.config(font=("Helvetica", 16))
   ```

4. **修改尺寸**：可以用来调整控件的宽度和高度。
   ```python
   entry.config(width=40)
   ```

### 示例

以下是一个简单的示例，展示如何使用 `config` 方法动态更改标签的文本和颜色：

```python
import tkinter as tk

def change_label():
    label.config(text="文本已更新", bg="yellow", fg="red")

root = tk.Tk()
root.title("Config 示例")

label = tk.Label(root, text="初始文本", bg="white", fg="black")
label.pack(pady=10)

button = tk.Button(root, text="更新标签", command=change_label)
button.pack(pady=10)

root.mainloop()
```

在这个示例中，点击按钮后，`change_label` 函数会被调用，标签的文本和颜色会被更新。通过 `config` 方法，可以很方便地在程序运行时调整控件的属性。