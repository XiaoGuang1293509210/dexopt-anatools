import tkinter as tk
from tkinter import scrolledtext
def on_button_click():
    input_text = entry.get()
    text.insert(tk.END, input_text + '\n')
    entry.delete(0, tk.END)
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