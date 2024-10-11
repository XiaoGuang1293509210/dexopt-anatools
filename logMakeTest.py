# 打开文件，如果文件不存在，则创建新文件
with open('test_log.txt', 'w') as f:
    # 写入内容
    for i in range(50):
        if(i%2 == 0):
            f.write('2024/10/11: 17:%d : error \n' % i)
        else:
            f.write('2024/10/11: 17:%d : info \n' % i)