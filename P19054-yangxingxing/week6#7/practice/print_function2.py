# 2、练习， 左右两种打印方式。要求数字必须对齐
# 单数字打印， 拼出来格式。
def left_nums(num):
    for i in range(1, num+1):
        for y in range(num, 0, -1):
            if y > i:
                print('{:<{}}'.format('', len(str(y)) + 2), end='')
            else:
                print('{:<{}}'.format(y, len(str(y)) + 2), end='')
        print()

# 先算出来，最后的总字符串， 然后从总字符串里面截出来要用的字符串。正好可以从总字符串里面拿出总的长度， 截出来的字符串以总长度靠右对齐。
def left_nums(num):
    tail = ' '.join([str(i) for i in range(num, 0, -1)])
    length = len(tail)
    for i in range(1, length):
        if tail[-i] == ' ':
            print('{:>{}}'.format(tail[-i:], length))
    print(tail)
    print(tail)
    for i in range(length):
        if tail[i] == ' ':
            print('{:>{}}'.format(tail[i:], length))


# 也是先算出来最长的字符串，和字符串长度。然后在用列表拼字符串， 以长度对齐。
def left_nums(num):
    tail = ' '.join([str(i) for i in range(num, 0, -1)])
    length = len(tail)
    for i in range(1, num):
        print('{:>{}}'.format(' '.join([str(i) for i in range(i, 0, -1)]), length))
    print(tail)
    print(tail)
    for i in range(num-1, 0, -1):
        print('{:>{}}'.format(' '.join([str(i) for i in range(i, 0, -1)]), length))



left_nums(13)