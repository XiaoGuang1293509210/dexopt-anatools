import sqlite3
import tkinter as tk
import os

def mqsl_create_database():
    # 连接到SQLite数据库
    # 数据库文件是example.db
    # 如果数据库不存在，会自动创建
    conn = sqlite3.connect('./mLogSQL.db')
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

# 添加一个新的项目到数据库
def mqsl_add_item(keys, note):
    current_dir = os.getcwd() + '\\mLogSQL.db'
    print(current_dir)
    # 连接到SQLite数据库
    conn = sqlite3.connect(current_dir)
    # 创建一个Cursor对象并调用其execute()方法来执行SQL命令
    c = conn.cursor()
    # 插入一条记录
    c.execute("INSERT INTO items (keys, note) VALUES (?, ?)", (keys, note))
    # 检查插入是否成功
    if c.rowcount > 0:
        res = "sucess"
    else:
        res = "false"
    # 提交事务
    conn.commit()
    # 关闭连接
    conn.close()
    return res

# 从数据库查找项目
def mqsl_find_note(keys_value):
    # 连接到SQLite数据库
    conn = sqlite3.connect('./mLogSQL.db')
    c = conn.cursor()
    # 执行查询语句
    c.execute('SELECT note FROM items WHERE keys = ?', (keys_value,))
    # 获取查询结果
    result = c.fetchone()
    # 关闭连接
    conn.close()
    # 检查结果是否存在
    if result:
        return result[0]  # 返回note值
    else:
        return None  # 如果没有找到匹配的记录，返回None

# 输入按键操作
def edit_sql():
    text_output.delete(1.0, tk.END)  # 清除原有的输出内容

    key_text = entry_key.get()  # 获取输入框的内容
    note_text = entry_note.get()  # 获取输入框的内容
    try:
        rc = mqsl_add_item(key_text, note_text)
        text_output.insert(tk.END, rc)  # 在输出框中显示结果
    except TypeError as e:
        text_output.insert(tk.END, "error input") 



# # 创建主窗口
# root = tk.Tk()
# root.title("Edit SQL")

# # 创建输入框
# entry_key = tk.Entry(root, width=50)
# entry_key.pack(pady=10)
# entry_note = tk.Entry(root, width=50)
# entry_note.pack(pady=10)

# # 创建按钮，绑定到edit_sql函数
# button = tk.Button(root, text="加入历史日志分析", command = edit_sql)
# button.pack(pady=10)

# # 创建输出框
# text_output = tk.Text(root, height=5, width=50)
# text_output.pack(pady=10)


# # 运行主循环
# root.mainloop()