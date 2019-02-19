# 2、 练习， 左右两种打印方式。要求数字必须对齐
# 两种打印在一行。

def left_nums(num):
    space = 2
    middle_space = 5
    num_len = len(str(num))
    length = 0
    for n in range(1, num_len+1):
        now_stage = 10 ** n
        last_stage = 10 ** (n - 1)
        if num >= now_stage:
            length += (now_stage - last_stage) * (n + space)
        else:
            length += (num - last_stage + 1) * (n + space)


    for i in range(1, num+1):
        format_str = ''
        total_len = 0
        for n in range(1, i + 1):
            start_len = len(str(n))
            total_len +=  start_len + 2
            format_str = ('{{:>{}}}'.format(start_len + 2)) + format_str
        format_str = ('{{:>{}}}'.format(length - total_len)) + format_str
        print(format_str.format('', *range(i,0,-1)), end='')

        print('{:{}}'.format('', middle_space), end='')

        format_str = ''
        total_len = 0
        two_point = num - i + 1
        for n in range(two_point, 0, -1):
            start_len = len(str(n))
            total_len += start_len + 2
            format_str += ('{{:>{}}}'.format(start_len + 2))
        format_str = ('{{:>{}}}'.format(length - total_len)) + format_str
        print(format_str.format('', *range(two_point,0,-1)))


left_nums(23)




