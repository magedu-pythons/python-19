#1, 给定任意链表, 查找出x元素是否在列表里面, 存在返回1, 不存在返回0
def find_from( lst:list, target:int ) -> int:
    for i in lst:
        if i == target:
            return 1
    return 0

#test
lst = [1,4,3,6,6,7,8,19,30,40,34,2,3,4,5]
target = 5
find_from(lst,target)

#--------------------------------------------------------------

#2, 英文纯文本文件, 统计其中的单词出现的个数
#当前目录下有sample.txt文件,统计其中单词的总数

filename = 'sample.txt'

def count_words( filename:str ):
    '''
    输入一个纯英文文件名,得到单词数
    '''
    from pathlib import Path
    filepath = Path()/filename

    def line_words(line:str):
        num = 0
        word = 0
        for c in line:
            if c.isalpha():
                word = 1
                continue
            else:
                if word:
                    num += 1
                    word = 0
                else:
                    continue
        return num

    with open(filepath,'r') as file:
        number = 0
        for line in file:
            number += line_words(line)
    
    return number


print( 'File {} has {} words.'.format(filename,count_words(filename)) )







