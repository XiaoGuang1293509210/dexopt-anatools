# -*- coding: utf-8 -*-
import datetime
import random
import os
#生成的日志文件名
generated_logs='generated_logs.txt'
#生成的log行数
num_logs_to_generate = 100

def generate_log(log_level, log_content):
    # 获取当前时间
    now = datetime.datetime.now()
    # 格式化日期和时间
    date_str = now.strftime("%m-%d")
    time_str = now.strftime("%H:%M:%S.%f")[:-3]  # 保留毫秒部分
    # 随机生成进程和子进程ID
    process_id = random.randint(1000, 9999)
    child_process_id = random.randint(1000, 9999)
    # 生成日志字符串
    log_entry = f"{date_str} {time_str} {process_id} {child_process_id} {log_level} {log_content}"
    return log_entry

def get_random_log_content(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return random.choice(lines).strip()  # 随机选择一行并去除首尾空白

# 示例使用
def generate_multiple_logs(num_logs, filename):
    logs = []
    for _ in range(num_logs):
        log_level = random.choice(['V', 'D', 'I', 'W', 'E'])  # 随机选择日志级别
        log_content = get_random_log_content(filename)  # 从文件中读取日志内容
        log = generate_log(log_level, log_content)  # 生成日志
        logs.append(log)
    return logs

# 生成日志示例并写入文件
logs = generate_multiple_logs(num_logs_to_generate, 'log_content.txt')

#删除旧的的log
if os.path.exists(generated_logs):
    os.remove(generated_logs)
# 将日志写入文件并打印
with open(generated_logs, 'w', encoding='utf-8') as log_file:
    for log in logs:
        print(log)  # 打印日志
        log_file.write(log + '\n')  # 写入日志到文件
