
'方法1 字符串'
# def palindrome(src : int):
# 	_src = str(src)
# 	return '{} is palindrome number.'.format(src) if _src == _src[::-1] else 'not palindrome number'
#
# print(palindrome(12345))
# print(palindrome(121))

'方法2 整数'
def palindrome(src :int ):
	if src < 0:
		return  '{} is not palindrome number'.format(src)
	else:
		ret, ori = [] ,src
		while src > 0:
			src ,n = divmod(src, 10)
			ret.append(n)

		_sum = sum(10 ** (len(ret)-i)*c for i,c in enumerate(ret,1))
		return  'yes' if _sum == ori else 'no'

print(palindrome(121))
print(palindrome(0))
print(palindrome(55))
