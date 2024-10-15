import sqlite3

def create_database():
    # 连接到SQLite数据库
    # 数据库文件是example.db
    # 如果数据库不存在，会自动创建
    conn = sqlite3.connect('mLogSQL.db')
    # 创建一个Cursor对象并调用其execute()方法来执行SQL命令
    c = conn.cursor()
    # 创建表
    c.execute('''CREATE TABLE IF NOT EXISTS items
(id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
description TEXT)'''
)
    # 提交事务
    conn.commit()
    # 关闭连接
    conn.close()

# 添加一个新的项目到数据库
def add_item(name, description):
    # 连接到SQLite数据库
    conn = sqlite3.connect('example.db')
    # 创建一个Cursor对象并调用其execute()方法来执行SQL命令
    c = conn.cursor()
    # 插入一条记录
    c.execute("INSERT INTO items (name, description) VALUES (?, ?)", (name, description))
    # 提交事务
    conn.commit()
    # 关闭连接
    conn.close()


# 创建数据库和表
# create_database()
# 添加新元素
# add_item("Example Item", "This is an example item description.")
print("Item added successfully.")