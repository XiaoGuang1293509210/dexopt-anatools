def color_code(value):
    if value == '1':
        return 'R'
    elif value == '2':
        return 'G'
    elif value == '3':
        return 'B'
    else:
        return 'Invalid value'
    

def main(file_path, cmd):
    with open(file_path, 'r', encoding='utf-8') as file:
        # 逐行读取文件
        for line in file:
            # 去除行尾的换行符
            text.insert(tk.END, output + '\n')
            
            # 在这里进行你需要的操作，例如打印每一行
            print(line)
            
            # 更多操作...
            # 例如，你可以分割行中的单词，进行条件判断，等等。
            # words = line.split()
            # if condition:
            #     # do something
