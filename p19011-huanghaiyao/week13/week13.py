#第一题
class Item:
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def append(self, value):
        item = Item(value)
        if self.__tail:
            last = self.__tail
            last.next = item
            item.prev = last
        else:
            self.__head = item
        self.__tail = item

    def pop(self):
        if self.__tail == None:
            print('No date')
            return

        ret = self.__tail
        if self.__tail == self.__head:
            self.__tail = None
            self.__head = None
        else:
            self.__tail = self.__tail.prev
            self.__tail.next = None

        return ret.value

# test = Stack()
# for i in range(10):
#     test.append(i)
# for i in range(10):
#     print(test.pop())


#第二题
def bracket_p(num):

    def check(item):   #过滤函数
        count = 0
        flag = False
        for bit in item:
            count += 1 if bit=='0' else -1
            if count < 0:
                break
        else:
             if not count:
                flag = True

        return flag

    lst = ['{:0{width}b}'.format(x, width=num * 2) for x in range(2 ** (num * 2))]  #列出所有可能并抽象成零和一
    lst = filter(check, lst)

    for item in lst:
        for ch in item:
            print('(' if ch == '0' else ')', end='')
        print()

# bracket_p(3)

#第三题
def make_sentence(string:str):  #想不到其他方法了
    dictionarie = ['this', 'is', 'that', 'these', 'those', 'an', 'the', 'example']
    sentence_words = []
    done = False

    while not done:
        for word in dictionarie:
            if string.find(word) == 0:     #找到第一个并加入sentence_words列表， 然后更新字符串
                sentence_words.append(word)
                string = string[len(word):]
                break

        if string == '':
            done = True

    print(' '.join(sentence_words)+'.')

make_sentence('thisisanexample')