# 1、实现数据结构stack(栈)，并实现它的append，pop方法【动手查询相关资料理解stack特点以及与queue区别】
# 用数组实现


class Stack:
    def __init__(self, length: int):
        self.length = length
        self.stack = [None] * length
        self.index = -1

    def append(self, item):
        if self.index + 1 >= self.length:
            print('overflow!')
            return
        self.index += 1
        self.stack[self.index] = item

    def pop(self):
        if self.index == -1:
            print("stack is empty, can't pop")
            return
        self.stack[self.index], temp = None, self.stack[self.index]
        self.index -= 1
        return temp

    def __repr__(self):
        return 'STACK:{}, length:{}'.format(self.stack, self.index + 1)


# test
s = Stack(3)
s.pop()
print(s)
s.append(1)
print(s)
s.append(1)
s.append(1)
print(s)
s.append(1)
s.pop()
print(s)


# 2、打印出N对合理的括号组合。
# 例如： 当N=3，输出：()()(),()(()),(())(),((()))
# 这题有意思
def prinar(char, pos, left, right):
    if left < 0 or right < 0:
        return
    if left == 0 and right == 0:
        print(''.join(char))
        return
    if left > 0:
        char[pos] = '('
        prinar(char, pos + 1, left - 1, right)
    if right > left:
        char[pos] = ')'
        prinar(char, pos + 1, left, right - 1)


def res(n):
    char = [0] * (2 * n)
    prinar(char, 0, n, n)


# test
res(3)

# 3、根据字典，从一个抹去空格的字符串里面提取出全部单词组合，并且拼接成正常的句子:
# 例如: 输入一个字符串："thisisanexample", 程序输出: "this is an example"
dictionary = {
     'b', 'example', 'c', 'an', 'am', 'this', 'is', 'are'
}

string = "thisisanexample"
res = []
offset = 0
for i,_ in enumerate(string):
    if string[offset:i+1] in dictionary:
        res.append(string[offset:i+1])
        offset = i+1
        print(string[offset:i+1])

print(' '.join(res))




"""
(0 + 0)

    最后2题参考答案
"""