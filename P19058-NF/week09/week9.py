import re


str1 = 'and would sing it with Dad when he would play and sing'
str2 = 'when'
str3 = 'abc'

def stringjuge(str1, str2, pattern):

    regex = re.compile(pattern)
    result = regex.search(str1)

    if result:
        print(result.span()[0])
    else:
        print('None')

pattern = str2
stringjuge(str1, str2, pattern)

#给定一个整型列表，请实现从其中找出2个数的和为某一个指定的值？
lst = [1,5,2,7,4,9]
sum = 11
class Summ:
    def summation(self, lst: list, summary):
        for num,i in enumerate(lst):
            first = num
            second = num + 1
            while True:
                if second < len(lst):
                    if lst[first] + lst[second] == summary:
                        yield lst[first], lst[second]
                    else:
                        second += 1
                else:
                    break

sum1 = Summ()
print(next(sum1.summation(lst, 10)))

