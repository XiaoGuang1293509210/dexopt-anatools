import analogr as ag
import os
import glob
import tkinter as tk
from tkinter import scrolledtext




# 逐行分析
def find_command_in_line(cmd, line):# 'key:err'
    keyword = {}
    positionStart = 0
    positionEnd = -1
    rc = 0
    while(positionStart != -1):
        positionStart = cmd.find('\'',positionEnd+1)
        if positionStart == -1:
            break
        positionCut = cmd.find(':', positionStart+1)
        positionEnd = cmd.find('\'', positionCut+1)
        keystring = cmd[positionStart+1:positionCut]
        valuestring =  cmd[positionCut+1:positionEnd]
        keyword[keystring] = valuestring

    for key in keyword:
        if key == 'key':
            rc = ag.run_key(keyword[key], line)
        else:
            text.insert(tk.END, 'error cmd')
    
    return rc

# 读取文件进行分析和输出
def run(file_path, cmd):
    with open(file_path, 'r', encoding='utf-8') as file:
        # 逐行读取文件
        for line in file:
            # 分析输出与否
            rc = find_command_in_line(cmd, line)
            # 分析完成后输出
            if(rc):
                text.insert(tk.END, line)
        return
    text.insert(tk.END, "error file address")

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
    # 清除之前的输出
    text.delete('1.0', tk.END)
    # 读取地址和cmd
    cmd = entry.get()
    address = loc.get()
    # 判断使用默认地址
    if not address:
        address = find_defult_txt_file()
        if not address:
            text.insert(tk.END, "no file to analog")
            return
    # 有文件地址的情况下运行输出
    run(address, cmd)
    


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

# 创建滚动的文本输出框(日志部分)
text = scrolledtext.ScrolledText(root, wrap=tk.NONE, width=80, height=25)
text.pack()
# 创建滚动的文本输出框(同类问题提示)


# 主循环
root.mainloop()