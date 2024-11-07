import sqlite3
import tkinter as tk
from tkinter import scrolledtext
import os
import glob

def mqsl_create_database():
    # 连接到SQLite数据库
    db_path = entry_file.get()
    if not db_path:
        text_output.insert(tk.END, "false")
        return
    conn = sqlite3.connect(db_path)
    # 创建一个Cursor对象并调用其execute()方法来执行SQL命令
    c = conn.cursor()
    # 创建表
    c.execute('''CREATE TABLE IF NOT EXISTS items
(id INTEGER PRIMARY KEY AUTOINCREMENT,
keys TEXT NOT NULL,
note TEXT)'''
)
    # 提交事务
    conn.commit()
    # 关闭连接
    conn.close()

# 添加一个新的项目
def mqsl_add_item():
    text_output.delete(1.0, tk.END)  # 清除原有的输出内容
    keys = entry_key.get()
    note = entry_note.get()
    db_path = entry_file.get()
    if not db_path:
        db_path = find_defult_db_file()
    # 建立数据库链接
    conn = sqlite3.connect(db_path)
    # 创建一个Cursor对象并调用其execute()方法来执行SQL命令
    c = conn.cursor()
    # 插入一条记录
    c.execute("INSERT INTO items (keys, note) VALUES (?, ?)", (keys, note))
    # 检查插入是否成功
    if c.rowcount > 0:
        text_output.insert(tk.END, "success")
    else:
        text_output.insert(tk.END, "false")
    # 提交事务
    conn.commit()
    # 关闭连接
    conn.close()

# 删除数据
def mqsl_delete_data():
    text_output.delete(1.0, tk.END)  # 清除原有的输出内容
    keys = entry_key.get()
    db_path = entry_file.get()
    if not db_path:
        db_path = find_defult_db_file()
    # 连接到SQLite数据库
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    # 执行删除操作
    c.execute("DELETE FROM items WHERE keys=?", (keys,))
    # 检查是否成功
    if c.rowcount > 0:
        text_output.insert(tk.END, "success")
    else:
        text_output.insert(tk.END, "false")
    # 提交事务
    conn.commit()
    # 关闭数据库连接
    conn.close()

# 从数据库查找项目
def mqsl_find_note():
    text_output.delete(1.0, tk.END)
    keys = entry_key.get()
    db_path = entry_file.get()
    if not db_path:
        db_path = find_defult_db_file()
    # 连接到SQLite数据库
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('SELECT note FROM items WHERE keys = ?', (keys,))
    # 获取查询结果
    result = c.fetchone()
    # 关闭连接
    conn.close()
    # 检查结果是否存在
    if result:
        text_output.insert(tk.END, result)
    else:
        text_output.insert(tk.END, "no such keys")

# 主函数调用查找
def mqsl_find_note_by_main(keys, db_path):
    if not db_path:
        db_path = find_defult_db_file()
    # 连接到SQLite数据库
    print(db_path)
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('SELECT note FROM items WHERE keys = ?', (keys,))
    # 获取查询结果
    result = c.fetchone()
    # 关闭连接
    conn.close()
    # 检查结果是否存在
    if result:
        return result
    else:
        return None

# 主函数调用获取所有数据
def mqsl_get_all_by_main(db_path):
    if not db_path:
        db_path = find_defult_db_file()
    print(db_path)
    # 连接到SQLite数据库
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    # 查询所有数据
    c.execute("SELECT keys, note FROM items")
    rows = c.fetchall()
    # 关闭连接
    conn.close()
    return rows
    
# 检索全部的数据
def msql_find_all_data():
    text_output.delete(1.0, tk.END)
    db_path = entry_file.get()
    if not db_path:
        db_path = find_defult_db_file()
    # 连接到SQLite数据库
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    # 查询所有数据
    c.execute("SELECT keys, note FROM items")
    rows = c.fetchall()
    # 打印查询结果
    for keys, note in rows:
        text_output.insert(tk.END, f"Keys: {keys}, Note: {note}\n")
    # 关闭数据库连接
    conn.close()

# 使用默认地址
def find_defult_db_file():
    # 使用glob模块搜索当前目录下的.db文件
    current_dir = os.getcwd() + '/sqlite'
    db_files = glob.glob(os.path.join(current_dir, "*.db"))
    # 检查是否找到了.db文件
    if db_files:
        # 返回第一个.db文件的路径
        return db_files[0]
    else:
        text_output.insert(tk.END, "No SQL File") 
        return None

if __name__ == "__main__":
    # 创建主窗口
    root = tk.Tk()
    root.geometry("800x500")  # 设置窗口初始大小
    root.configure(bg="#FFFAF0")  # 设置窗口的背景色
    root.title("Edit SQL")

    # 创建输入框
    label_file = tk.Label(root, text="数据库地址", width=50)
    entry_file = tk.Entry(root, width=100)
    label_file.pack()
    entry_file.pack()
    label_key = tk.Label(root, text="关键词", width=50)
    entry_key = tk.Entry(root, width=100)
    label_key.pack()
    entry_key.pack()
    label_note = tk.Label(root, text="同类问题记录", width=50)
    entry_note = tk.Entry(root, width=100)
    label_note.pack()
    entry_note.pack()

    # 创建按钮
    button_frame = tk.Frame(root)
    button_frame.pack(side='top')
    # 在Frame中创建按钮并使用pack布局管理器
    button1 = tk.Button(button_frame, text="查找", width=15, command=mqsl_find_note)
    button1.pack(side='left', padx=10)
    button2 = tk.Button(button_frame, text="存入", width=15, command=mqsl_add_item)
    button2.pack(side='left', padx=10)
    button3 = tk.Button(button_frame, text="删除", width=15, command=mqsl_delete_data)
    button3.pack(side='left', padx=10)
    button4 = tk.Button(button_frame, text="全览", width=15, command=msql_find_all_data)
    button4.pack(side='left', padx=10)
    button5 = tk.Button(button_frame, text="新建", width=15, command=mqsl_create_database)
    button5.pack(side='left', padx=10)

    # 创建输出框
    text_output = scrolledtext.ScrolledText(root, wrap=tk.NONE, width=100, height=20)
    text_output.pack(pady=10)

    # 运行主循环
    root.mainloop()