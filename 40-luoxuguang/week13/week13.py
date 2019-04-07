#1、实现数据结构stack(栈)，并实现它的append，pop方法【动手查询相关资料理解stack特点以及与queue区别】

class Stack:
    def __init__(self):
        self.lst = []

    def append(self,object):
        self.lst.append(object)
        return self

    def pop(self):
        self.lst.pop()
        return self.lst[-1]

    def __repr__(self):
        return "{}".format(self.lst)

stk = Stack()
stk.append(3).append('abc').append(4)
print(stk)
stk.pop()
print(stk)

#栈是一种后进先出LIFO的结构，队列是FIFO先进先出的数据结构。考虑到这点，用列表来表示栈更合适

#2、打印出N对合理的括号组合。例如： 当N=3，输出：()()(),()(()),(())(),((()))

def brackets(n:int):
    lst = []
    if n == 1:
        return "()"
    else:
        lst.append("()"*n)
        lst.append("("*n+")"*n)
    for i in range(1,n):
        for j in range(i,n): #起点从i开始，避免重复
            if i+j == n:
                if i!=j:
                    lst.append("("*i+")"*i + "("*j+")"*j)
                    lst.append("("*j + ")" * j + "(" * i + ")" * i)
                else:
                    lst.append("(" * i + ")" * i + "(" * j + ")" * j)
    return lst

print(brackets(3)) #['()()()', '((()))', '()(())', '(())()']
print(brackets(5)) #['()()()()()', '((((()))))', '()(((())))', '(((())))()', '(())((()))', '((()))(())']


#3、根据字典，从一个抹去空格的字符串里面提取出全部单词组合，并且拼接成正常的句子:
#例如: 输入一个字符串："thisisanexample", 程序输出: "this is an example"

d = {"this":1,"is":2,"an":3,"example":4}

def sentence(string:str):
    lst = []
    i = 0
    for key,item in d.items():
        index = string.find(key)
        lst.append(string[index:len(key)+index])

    return " ".join(lst)

print(sentence("thisisanexample")) #this is an example
print(sentence("itisanapple")) # is an

#有点没太明白题意，应该是根据字典查找单词，然后拼接成句子



"""
(0 + 0)

    不要用关键字作为函数参数，最后一题指的是分词，参考答案
"""