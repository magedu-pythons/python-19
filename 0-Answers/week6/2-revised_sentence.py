# 输入一个英文句子,翻转句子中的单词顺序,但单词内字符的顺序不变

def revised_sentence(s: str) -> str:
    lst = s.split(' ')
    return ' '.join(reversed(lst))


# test
print(revised_sentence('you have 2 dream'))
