'请将 "1,2,3"，变成 ["1","2","3"]'

def convert(src:str) -> list:
	return  src.split(',')

print(convert('1,2,3'))