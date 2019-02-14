# 1在列表中找数字x
lst = list(range(100))


def find(x):
    for item in lst:
        if x == item:
            return 1
    else:
        return 0


print("找到了") if find(10) else print("没有该数字")


# 2计算文件的英文单词个数
def finds():
    with open("123.txt", 'r') as file:
        strings = file.read()
    count = len(strings.split(sep=' '))
    print("这个文件的英文单词个数为", count)


finds()



"""
(0 + 0)

    第二题参考答案实现
"""