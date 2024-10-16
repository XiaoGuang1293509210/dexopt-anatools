from datetime import datetime

def color_code(value):
    if value == '1':
        return 'R'
    elif value == '2':
        return 'G'
    elif value == '3':
        return 'B'
    else:
        return 'Invalid value'
    

def run_key(text_input, val,line):
     # 分割日志字符串
    parts = line.split()
    
    # 提取各个部分
    date = parts[0]
    time = parts[1]
    process = int(parts[2])
    thread = int(parts[3])
    log_level = parts[4]
    log_content = ' '.join(parts[5:])
    #output = f'日期：{date} 时间: {time}, 进程: {process}, 线程: {thread}, log等级: {log_level}, log内容: {log_content}'
    
    # 检查 日期 是否为空
    if not date:
        return 0
    # 转换日期为元组格式
    date_tuple = tuple(map(int, date.split('-')))
    # 检查日期是否在范围内
    if not (text_input.datestart <= date_tuple <= text_input.dateend):
        return 0
    
    # 转换时间为 datetime 对象
    time = datetime.strptime(time, "%H:%M:%S.%f")
    # 检查 time 是否在时间范围内
    if not (text_input.timestart <= time <= text_input.timeend):
        return 0
    
    # 根据 process_list 和 thread_list 的状态决定是否进行检查
    if text_input.process_list and text_input.thread_list:
        # 如果 process_list 和 thread_list 都不为空，则同时检查 process 和 thread
        if process not in text_input.process_list or thread not in text_input.thread_list:
            return 0
    elif text_input.process_list:
        # 如果只有 process_list 不为空，则只检查 process
        if process not in text_input.process_list:
            return 0
    elif text_input.thread_list:
        # 如果只有 thread_list 不为空，则只检查 thread
        if thread not in text_input.thread_list:
            return 0
    # 如果两个列表都为空，则不进行检查

    #检查log中是否含有关键词
    if val in log_content:
        return 1
    else:
        return 0
