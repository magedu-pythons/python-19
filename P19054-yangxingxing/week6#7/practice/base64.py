base64_rule = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

def base64_en(arg, argcode='utf-8'):
    bytes_data = bytes(arg, encoding=argcode)
    len_num = len(bytes_data)
    if len_num % 3:
        postfix = 3 - (len_num % 3)
    else:
        postfix = 0
    bin_num = ''
    for x in bytes_data:
        px = 8 - len(bin(x)[2:])
        if px:
            bin_num += '0' * px + bin(x)[2:]
        else:
            bin_num += bin(x)[2:]
    bin_num += '00' * postfix
    base64_str = ''
    for y in range(0, len(bin_num), 6):
        index = int(bin_num[y:y+6], 2)
        base64_str += base64_rule[index]
    return base64_str + postfix * '='

def base64_de(arg):
    '''不能解析汉字'''
    arg = arg.rstrip('=')
    bin_str = ''
    for i in arg:
        num = base64_rule.find(i)
        bin_local = bin(num)[2:]
        bin_str += bin_local if len(bin_local) == 6 else (6 - len(bin_local)) * '0' + bin_local
    data = ''
    num_len = len(bin_str) - len(bin_str) % 8
    for x in range(0, num_len, 8):
        data += chr(int(bin_str[x:x+8], 2))
    return data

print(base64_en('abcd123'))
print(base64_de(base64_en('a123')))

