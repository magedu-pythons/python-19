'''输入一个英文句子,翻转句子中的单词顺序,但单词内字符的顺序不变  '''


def reverse_sentence():
	src = input('input sentence:')
	_src = src[:]  #不就地修改
	return ' '.join(_src.split()[::-1])



print(reverse_sentence())