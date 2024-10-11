import analog
import tkinter as tk
from tkinter import scrolledtext

# 按钮控制
def on_button_click():
    cmd = entry.get()
    output = analog.color_code(cmd)
    text.insert(tk.END, output + '\n')
    #entry.delete(0, tk.END)


# main window
root = tk.Tk()
# 创建标签输入框
entry = tk.Entry(root)
entry.pack()
# 创建按钮
button = tk.Button(root, text="Submit", command=on_button_click)
button.pack()
# 创建滚动的文本输出框
text = scrolledtext.ScrolledText(root, wrap=tk.NONE, width=40, height=10)
text.pack()
root.mainloop()