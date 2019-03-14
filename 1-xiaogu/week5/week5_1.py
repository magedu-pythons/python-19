# x = input("给一个5位数 >>> ")
# if x[0] == x[4]:
	# if x[1] == x[3]:
		# print("{}是回文数".format(int(x)))
	# else:
		# print("{}不是回文数".format(int(x)))
# else:
	# print("{}不是回文数".format(int(x)))
	
	
x = input("任意给一个数 >>> ")
x_list = list(x)
y = list(reversed(x))
if x_list == y:
	print("{}是回文数".format(x))
else:
	print("{}不是回文数".format(x))
