# coding=utf-8
#题目1：给出任意一个列表，请查找出x元素是否在列表里面，如果存在返回1，不存在返回0
lst=['a','d','3','bb','h','q',1,5,6,77,3,5,7,7,2,'gg']
def find_ele(id,lst):
    if id in lst:
        return 1
    else:
        return 0

while True:
    id=input('please input an element:')  #这种方式返回的是string，TODO 字符串的问题
    if id=='quit':
        break
    print(find_ele(id,lst))
#题目2：任一个英文的纯文本文件，统计其中的单词出现的个数。
text="""A laser differs from other sources of light in that it emits
 light coherently. Spatial coherence allows a laser to be focused
 to a tight spot, enabling applications such as laser cutting and
  lithography."""
def count():
    # print(text.count('a'))#字符串统计的是字符，不是单词
    text1=text.replace('\n','')
    lst=text1.split(' ')
    cou_list=dict()
    for i in lst:
        if i not in cou_list.keys():
            cou_list[i]=1
        else:
            cou_list[i] +=1

    print(cou_list)
count()