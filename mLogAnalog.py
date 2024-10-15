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
    process = parts[2]
    thread = parts[3]
    log_level = parts[4]
    log_content = ' '.join(parts[5:])
    #output = f'日期：{date} 时间: {time}, 进程: {process}, 线程: {thread}, log等级: {log_level}, log内容: {log_content}'
    # 检查 日期 是否为空
    if not date:
        return 0
    if not text_input.datestart:
        text_input.datestart = '1-1'
    if not text_input.dateend:
        text_input.dateend = '12-30'
    # 转换日期为元组格式
    date_tuple = tuple(map(int, date.split('-')))
    datestart_tuple = tuple(map(int, text_input.datestart.split('-')))
    dateend_tuple = tuple(map(int, text_input.dateend.split('-')))
    
    
    # 检查 time 是否为空
    if not time:
        return 0
    
    # 定义时间范围
    if not text_input.timestart:
        text_input.timestart = '00:00:00.000'
    if not text_input.timeend:
        text_input.timeend = '23:59:59.999'
        
    # 转换时间为 datetime 对象
    time = datetime.strptime(time, "%H:%M:%S.%f")
    timestart = datetime.strptime(text_input.timestart, "%H:%M:%S.%f")
    timeend = datetime.strptime(text_input.timeend, "%H:%M:%S.%f")
    
    # 检查 time 是否在时间范围内
    if not (timestart <= time <= timeend):
        return 0
    # 检查日期是否在范围内
    if not (datestart_tuple <= date_tuple <= dateend_tuple):
        return 0
    
    if val in log_content:
        return 1
    else:
        return 0
