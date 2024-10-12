def color_code(value):
    if value == '1':
        return 'R'
    elif value == '2':
        return 'G'
    elif value == '3':
        return 'B'
    else:
        return 'Invalid value'
    

def run_key(val,line):
    if val in line:
        return 1
    else:
        return 0
