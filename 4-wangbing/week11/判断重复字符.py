'''实现一个函数，输入字符串，判断该字符串是否不含有重复字符 '''


def repeat_str(src: str):
	ori_length = len(src)
	norepeat_length = len(set(src))
	return 'repeat' if ori_length > norepeat_length else 'no repeat'

print(repeat_str('wear'))
print(repeat_str('sss'))