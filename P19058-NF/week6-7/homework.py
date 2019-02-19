alist=[1,2,3,4,5]
import random

def ran_lst(lst):
    length = len(lst)
    for _ in range(0,5):
        x1 = random.randint(0,length-1)
        x2 = random.randint(0,length-1)
        lst[x1],lst[x2] = lst[x2],lst[x1]
        print(lst)
        return  lst

ran_lst(alist)
print('asignment1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


def store():
    sockt = ['socket']*10
    shoes = ['shoese']*20
    slippers = ['slippers']*30
    necklace = ['necklace']*40
    total_goods = sockt+shoes+slippers+necklace
    return total_goods[random.randint(0,100)]

print(store())
print('asignment2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


a = (('a'),('b'))
b = (('c'),('d'))


def team(first,second,dit=None):
    if dit == None:
        dit = {}

    for x,y in zip(first,second):
        dit[x] = y
    return dit

print(team(a,b))
print('asignment3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


sentence = 'I am a superman'


def rever_order(sentence:str):
    new_sentence = sentence.split(' ')
    print('sentence is',new_sentence)
    length = len(sentence)
    s = new_sentence[::-1]
    #print(new_sentence[1])
    #print(s)
    return s



print(rever_order(sentence))