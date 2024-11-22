import mLogAnalog as ag
import mLogSqlite as sq
import os
import glob
import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
from tkinter import ttk
from tkinter import filedialog

class MyInput:
    address = ''
    keys = []
    nokeys = []
    datestart = ''
    dateend = ''
    timestart = ''
    timeend = ''
    process_list = []
    thread_list = []
    log_level = ''
    analysis_type = ""
    find_dexopt_key = 0
    dexopt_start = "starting PostinstallRunnerAction"
    dexopt_end = "finished last action PostinstallRunnerAction with code ErrorCode::kSuccess"
    apk_dexopt_start = ""
    apk_dexopt_end = ""
    # 初始化函数
    def __init__(self, address='', keys = "", nokeys = "", datestart='', dateend='', timestart='', timeend='',process='',thread='',log_level='',analysis_type=""):
        self.address = address
        self.keys = self.split_string_to_key(keys)
        self.nokeys = self.split_string_to_key(nokeys)
        self.process = process
        self.thread = thread
        self.log_level = log_level
        # 转换日期为元组格式
        self.datestart = tuple(map(int, (datestart or '1-1').split('-')))
        self.dateend = tuple(map(int, (dateend or '12-30').split('-')))
        # 定义时间范围 # 将 timestart 和 timeend 转换为 datetime 对象
        self.timestart = datetime.strptime(timestart or '00:00:00.000', "%H:%M:%S.%f")
        self.timeend = datetime.strptime(timeend or '23:59:59.999', "%H:%M:%S.%f")
        # 将 process 和 thread 字符串转换为整数列表
        self.process_list = self.split_string_to_key(process)
        self.thread_list = self.split_string_to_key(thread)
        if log_level:  # 检查log_level是否非空
            self.log_level = log_level[0]  # 只有在log_level非空时才截取首个字符
        else:
            self.log_level = 'A'  # 如果log_level为空，设置self.log_level为空字符串或默认值
        if analysis_type:# 检查analysis_type是否非空
            self.analysis_type = analysis_type  # 只有在analysis_type非空时才截取首个字符
        else:
            self.analysis_type = " "  # 如果analysis_type为空，设置self.analysis_type为空字符串或默认值
    # 显示info信息
    def display(self):
        print(f"Address: {self.address}")
        print(f"Keys: {self.keys}")
        print(f"Nokeys: {self.nokeys}")
        print(f"Start Date: {self.datestart}")
        print(f"End Date: {self.dateend}")
        print(f"Start Time: {self.timestart}")
        print(f"End Time: {self.timeend}")
        print(f"Process: {self.process}")
        print(f"Thread: {self.thread}")
        print(f"log_level: {self.log_level}")
        print(f"analysis_type: {self.analysis_type}")

    # 将输入字符串按照逗号分隔，但忽略被反斜杠转义的逗号。
    def split_string_to_key(self, input_string):
        result = []
        buffer = ""
        escape_next = False
        for char in input_string:
            if escape_next:
                # 如果上一个字符是反斜杠，那么当前字符被视为转义字符
                buffer += char
                escape_next = False
            elif char == '\\':
                # 如果遇到反斜杠，下一个字符将被视为转义字符
                escape_next = True
            elif char == ',' and not escape_next:
                # 如果当前不在转义状态且遇到逗号，则分割
                result.append(buffer)
                buffer = ""
            else:
                # 否则，将字符添加到缓冲区
                buffer += char
        # 添加最后的缓冲区内容（如果有）
        if buffer:
            result.append(buffer)
        return result


# 逐行分析
def find_command_in_line(input_info, line):
    rc = 0
    rc = ag.runrun(input_info, line)
    return rc

def dexopt_analysis(input_info,line):
    rc = 0 
    #static find_APK_dexopt_key = 0
    # 分割日志字符串
    parts = line.split()
    # 如果格式不正确则返回
    if len(parts) < 5:
        return 0
    # 提取各个部分
    #date = parts[0]
    #time = parts[1]
    #process = parts[2]
    #thread = parts[3]
    log_level = parts[4]
    log_content = ' '.join(parts[5:])
    
    if not input_info.find_dexopt_key and input_info.dexopt_start in log_content:
        input_info.find_dexopt_key = 1
    elif input_info.find_dexopt_key and input_info.dexopt_end in log_content:
        input_info.find_dexopt_key = 0
        return -1
    if input_info.find_dexopt_key and log_level == "E" :
        rc = 1
    #rc = ag.find_dexopt_err(input_info, line)
    return rc

# 读取文件进行分析和输出
def run(input_info,sqlpath):
    try:
        # 获取数据库所有的错误信息
        rows = sq.mqsl_get_all_by_main(sqlpath)
        # 根据分析类型进行不同的处理
        if input_info.analysis_type == "dexopt":
            with open(input_info.address, 'r', encoding='utf-8') as file:
                for line in file:
                    rc = dexopt_analysis(input_info, line)
                    if(rc == -1):
                        break
                    elif(rc == 1):
                        output_text.insert(tk.END, line)
                    else:
                        continue
                    #检索常见错误
                    for key,note in rows:
                        err_rc = ag.find_err_in_line(key ,line)
                        if (err_rc):
                            sql_text.insert(tk.END, line)
                            sql_text.insert(tk.END, "log分析:" + note + "\n")
                return
        else:
            with open(input_info.address, 'r', encoding='utf-8') as file:
                for line in file:
                    rc = find_command_in_line(input_info, line)
                    if(rc):
                        output_text.insert(tk.END, line)
                    #检索常见错误
                    for key,note in rows:
                        err_rc = ag.find_err_in_line(key ,line)
                        if (err_rc):
                            sql_text.insert(tk.END, line)
                            sql_text.insert(tk.END, "log分析:" + note + "\n")
                return
    except FileNotFoundError as e:
        output_text.insert(tk.END, "error file address")

# 空地址时使用默认地址检索
def find_defult_txt_file():
    current_dir = os.getcwd()
    txt_files = glob.glob(os.path.join(current_dir, "*.txt"))
    if txt_files:
        return txt_files[0]
    else:
        return None

# 按钮控制
def on_button_click():
    # 清除之前的输出
    output_text.delete('1.0', tk.END)
    sql_text.delete('1.0', tk.END)
    # 读取地址和cmd
    input_info = MyInput(
        address = filepath_entry.get(),
        keys = key_entry.get(),
        nokeys = nokey_entry.get(),
        datestart = StartDate_entry.get(),
        dateend = EndDate_entry.get(),
        timestart = StartTime_entry.get(),
        timeend = EndTime_entry.get(),
        process = process_entry.get(),
        thread = thread_entry.get(),
        log_level = log_level_combobox.get(),
        analysis_type = analysis_type_combobox.get()
    )
    # 检索同类型问题
    sqlpath = sqlpath_entry.get()
    # for item in input_info.keys:
    #     cb_note = sq.mqsl_find_note_by_main(item, sqlpath)
    #     if cb_note:
    #         sql_text.insert(tk.END, item + ' : ' + cb_note[0])
    input_info.display()
    # 判断使用默认地址
    if not input_info.address:
        input_info.address = find_defult_txt_file()
        if not input_info.address:
            output_text.insert(tk.END, "no file to analog")
            return
    # 有文件地址的情况下运行输出
    run(input_info,sqlpath)
#文件选择按钮
def file_path_browse_file():
    filename = filedialog.askopenfilename(title="Select file",
                                          filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    filepath_entry.delete(0, tk.END)
    filepath_entry.insert(0, filename)
def sql_browse_file():
    filename = filedialog.askopenfilename(title="Select file",
                                          filetypes=(("Db files", "*.db"), ("All files", "*.*")))
    sqlpath_entry.delete(0, tk.END)
    sqlpath_entry.insert(0, filename)
# 输出保存按钮
def save_output_to_file():
    #"""Save the content of the output_text widget to a file."""
    # Use file dialog to let user choose where to save the file
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    
    # Ensure the file path is not empty
    if file_path:
        # Get the content from the output_text widget
        content = output_text.get("1.0", tk.END)
        
        # Write the content to the selected file
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

# 主程序窗口
root = tk.Tk()
root.title("My Tkinter App")
root.geometry("1200x900")  # 设置窗口初始大小
root.configure(bg="white")  # 设置窗口的背景色

# 输入框: 地址&关键词&反选关键词
sqlpath_label = tk.Label(root, text = "输入数据库地址(不填的话为数据库目录下第一个db文件),例如:./sqlite/example.db", width=80)
sqlpath_entry_frame = tk.Frame(root)
sqlpath_entry = tk.Entry(sqlpath_entry_frame, width=80-7)
sqlpath_entry.pack(side=tk.LEFT)
sql_browse_button = tk.Button(sqlpath_entry_frame, text="浏览", command=sql_browse_file)
sql_browse_button.pack(side=tk.LEFT)
filepath_label = tk.Label(root, text = "输入文件地址(不填的话为同目录下第一个txt文件),例如:./generated_logs.txt", width=80)
filepath_entry_frame = tk.Frame(root)
filepath_entry = tk.Entry(filepath_entry_frame, width=80-7)
filepath_entry.pack(side=tk.LEFT)
browse_button = tk.Button(filepath_entry_frame, text="浏览", command=file_path_browse_file)
browse_button.pack(side=tk.LEFT)
key_label = tk.Label(root, text = "输入需要查找的关键词,用逗号分开,例如: info,error", width=80)
key_entry = tk.Entry(root, width=80)
nokey_label = tk.Label(root, text = "输入无需查找的关键词,例如：Error,update", width=80)
nokey_entry = tk.Entry(root, width=80)
# 输入框: 日期
date_frame = tk.Frame(root)
StartDate_label = tk.Label(date_frame, text="起始日期", width=30)
StartDate_entry = tk.Entry(date_frame, width=30)
EndDate_label = tk.Label(date_frame, text="截止日期", width=30)
EndDate_entry = tk.Entry(date_frame, width=30)

StartDate_label.pack(side=tk.LEFT)
StartDate_entry.pack(side=tk.LEFT)
EndDate_label.pack(side=tk.LEFT)
EndDate_entry.pack(side=tk.LEFT)

# 输入框: 时间
time_frame = tk.Frame(root)
StartTime_label = tk.Label(time_frame, text="起始时间", width=30)
StartTime_entry = tk.Entry(time_frame, width=30)
EndTime_label = tk.Label(time_frame, text="截止时间", width=30)
EndTime_entry = tk.Entry(time_frame, width=30)

StartTime_label.pack(side=tk.LEFT)
StartTime_entry.pack(side=tk.LEFT)
EndTime_label.pack(side=tk.LEFT)
EndTime_entry.pack(side=tk.LEFT)

# 输入框: 进程和线程
process_thread_frame = tk.Frame(root)
process_label = tk.Label(process_thread_frame, text="进程", width=30)
process_entry = tk.Entry(process_thread_frame, width=30)
thread_label = tk.Label(process_thread_frame, text="线程", width=30)
thread_entry = tk.Entry(process_thread_frame, width=30)

process_label.pack(side=tk.LEFT)
process_entry.pack(side=tk.LEFT)
thread_label.pack(side=tk.LEFT)
thread_entry.pack(side=tk.LEFT)

# 选择框: 日志等级 和 分析类型
Select_frame = tk.Frame(root)
log_level_combobox = ttk.Combobox(Select_frame, width=20, values=['ALL','V:Verbose,调试信息', 'D:Debug,调试信息', 'I:Info,一般信息', 'W:Warn', 'E:ERROR'])
log_level_combobox.set(' 请选择日志级别')  # 设置默认显示的值
# 新增选择框: 请选择分析类型
analysis_type_combobox = ttk.Combobox(Select_frame, width=20, values=[' ', 'FOTA', 'dexopt'])
analysis_type_combobox.set(' 请选择分析类型')  # 设置默认显示的值
# 将两个组合框添加到combined_frame中，并使用side参数来控制它们的水平排列
log_level_combobox.pack(side=tk.LEFT)
analysis_type_combobox.pack(side=tk.LEFT)

# log_level_frame = tk.Frame(root)
# log_level_combobox = ttk.Combobox(log_level_frame, width=20, values=['ALL','V:Verbose,调试信息', 'D:Debug,调试信息', 'I:Info,一般信息', 'W:Warn', 'E:ERROR'])
# log_level_combobox.set(' 请选择日志级别')  # 设置默认显示的值
# log_level_combobox.pack(side=tk.LEFT)

# 提交按钮
button_frame = tk.Frame(root)
analysis_button = tk.Button(button_frame, text="开始分析", command=on_button_click, width=40)
analysis_button.pack(side=tk.LEFT)
# 保存按钮
save_button = tk.Button(button_frame, text="输出保存到文件", command=save_output_to_file, width=20)
save_button.pack(side=tk.LEFT)

# 输出框(日志部分)
output_text = scrolledtext.ScrolledText(root, wrap=tk.NONE, width=150, height=30)

# 输出框(同类问题提示)
sql_text = scrolledtext.ScrolledText(root, wrap=tk.NONE, width=150, height=10)

# 布局
sqlpath_label.pack()
sqlpath_entry_frame.pack()
filepath_label.pack()
filepath_entry_frame.pack()
key_label.pack()
key_entry.pack()
nokey_label.pack()
nokey_entry.pack()
date_frame.pack()
time_frame.pack()
process_thread_frame.pack()
#log_level_frame.pack()
Select_frame.pack()
button_frame.pack()
output_text.pack()
sql_text.pack()

# 主循环
root.mainloop()
