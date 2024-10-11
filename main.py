import os
import glob
import tkinter as tk
from tkinter import scrolledtext

# 逐行分析
def find_command_in_line(cmd, line):
    if cmd in line:
        return 1
    else:
        return 0

# 命令行分析
def run(file_path, cmd):
    with open(file_path, 'r', encoding='utf-8') as file:
        # 逐行读取文件
        for line in file:
            rc = find_command_in_line(cmd, line)
            if(rc):
                text.insert(tk.END, line)

# 默认地址检索
def find_defult_txt_file():
    # 获取当前工作目录
    current_dir = os.getcwd()
    # 使用glob模块查找当前目录下的所有.txt文件
    txt_files = glob.glob(os.path.join(current_dir, "*.txt"))
    # 如果找到了.txt文件
    if txt_files:
        # 返回第一个.txt文件的完整路径
        return txt_files[0]
    else:
        # 如果没有找到.txt文件，返回None或适当的提示信息
        return None

# 按钮控制
def on_button_click():
    cmd = entry.get()
    address = loc.get()
    if not address:
        address = find_defult_txt_file()
        if not address:
            text.insert(tk.END, "no file to analog")
            return
    run(address, cmd)
    # output = analog.color_code(cmd)
    # text.insert(tk.END, output + '\n')
    entry.delete(0, tk.END)


# main window
root = tk.Tk()
root.title("My Tkinter App")
root.geometry("800x600")  # 设置窗口初始大小
# root.minsize(200, 200)  # 设置窗口的最小尺寸
# root.maxsize(1000, 800)  # 设置窗口的最大尺寸
root.configure(bg="white")  # 设置窗口的背景色

# 创建标签输入框
loc_text = tk.Label(root, text = "输入文件地址", width=40)
loc = tk.Entry(root, width=80)
entry_text = tk.Label(root, text = "输入命令", width=40)
entry = tk.Entry(root, width=80)

loc_text.pack()
loc.pack()
entry_text.pack()
entry.pack()

# 创建按钮
button = tk.Button(root, text="Submit", command=on_button_click)
button.pack()

# 创建滚动的文本输出框
text = scrolledtext.ScrolledText(root, wrap=tk.NONE, width=80, height=25)
text.pack()

# 主循环
root.mainloop()