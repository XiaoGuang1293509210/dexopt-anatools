from datetime import datetime

def runrun(text_input,line):
    cb = 0
    cb = run_type(text_input,line)
    if cb == 0:
        return cb
    cb = run_key(text_input,line)
    return cb


def run_type(text_input,line):
    # 分割日志字符串
    parts = line.split()
    # 如果格式不正确则返回
    if len(parts) < 5:
        return 0
    # 提取各个部分
    date = parts[0]
    time = parts[1]
    process = parts[2]
    thread = parts[3]
    log_level = parts[4]
    #log_content = ' '.join(parts[5:])
    #output = f'日期：{date} 时间: {time}, 进程: {process}, 线程: {thread}, log等级: {log_level}, log内容: {log_content}'
    
    # 转换日期为元组格式
    date_tuple = tuple(map(int, date.split('-')))
    # 检查日期是否在范围内
    if text_input.datestart:
        if (date_tuple < text_input.datestart):
            return 0
    if text_input.dateend:
        if (date_tuple > text_input.dateend):
            return 0
    
    # 转换时间为 datetime 对象
    time = datetime.strptime(time, "%H:%M:%S.%f")
    # 检查 time 是否在时间范围内
    if text_input.timestart:
        if (time < text_input.timestart):
            return 0
    if text_input.timeend:
        if (time > text_input.timeend):
            return 0
    
    # # 根据 process_list 和 thread_list 的状态决定是否进行检查
    # if text_input.process_list and text_input.thread_list:
    #     # 如果 process_list 和 thread_list 都不为空，则同时检查 process 和 thread
    #     if process not in text_input.process_list or thread not in text_input.thread_list:
    #         return 0
    if text_input.process_list:
        # 如果只有 process_list 不为空，则只检查 process
        if process not in text_input.process_list:
            return 0
    
    if text_input.thread_list:
        # 如果只有 thread_list 不为空，则只检查 thread
        if thread not in text_input.thread_list:
            return 0

    # log_level不为空，则判断log_level是否对应
    if text_input.log_level != 'A':
        if not log_level == text_input.log_level:
            return 0
    
    return 1
    # #检查log中是否含有关键词
    # for value in values:
    #     if value not in log_content:
    #         return 0
    # #检查log是否包含nokey关键词
    # for key in text_input.nokey_list:
    #     if key in line:
    #         return 0
    # return 1


def run_key(text_input,line):
    # 分割日志字符串
    parts = line.split()
    
    # 提取各个部分
    log_content = ' '.join(parts[5:])
    rc = 1
    if not text_input.keys and not text_input.nokeys:
        return 1
    if text_input.keys:
        for value in text_input.keys:
            if value in log_content:
                rc = 1
                break
    if text_input.nokeys:
    #检查log是否包含nokey关键词
        for novalue in text_input.nokeys:
            if novalue in log_content:
                rc = 0
                break
    return rc