def color_code(value):
    if value == '1':
        return 'R'
    elif value == '2':
        return 'G'
    elif value == '3':
        return 'B'
    else:
        return 'Invalid value'
# 测试函数
# print(color_code(1))  # 输出: R
# print(color_code(2))  # 输出: G
# print(color_code(3))  # 输出: B
# print(color_code(4))  # 输出: Invalid value