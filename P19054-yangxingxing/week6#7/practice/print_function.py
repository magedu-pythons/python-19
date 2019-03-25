# 1、  编写一个函数，能够接受至少2个参数，返回最小值和最大值

#def nums(*args):
#    return max(args), min(args)
def nums(*args):
    max_num = args[0]
    min_num = args[0]
    for num in args:
        if max_num < num:
            max_num = num
        elif min_num > num:
            min_num = num
    return max_num, min_num


# 2、 练习, 左右两种打印方式。要求数字必须对齐
# 两种方式，分开打印。
def left_nums(num):
    space = 2
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
        print(format_str.format('', *range(i,0,-1)))

    for i in range(num, 0, -1):
        format_str = ''
        total_len = 0
        for n in range(i, 0, -1):
            start_len = len(str(n))
            total_len += start_len + 2
            format_str += ('{{:>{}}}'.format(start_len + 2))
        format_str = ('{{:>{}}}'.format(length - total_len)) + format_str
        print(format_str.format('', *range(i,0,-1)))

left_nums(12)





