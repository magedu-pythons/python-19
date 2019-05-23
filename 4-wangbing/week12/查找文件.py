'实现一个函数获取一个目录下所有以.py结尾的文件（包含目录下的子目录中的.py文件）  '

from pathlib import Path

def findfiles(p:str,type:str):
	p = Path(p)
	# return [p.name for file in p.rglob(type)]
	return (f.name for f in p.rglob('*.py'))


files = findfiles('','*.py')
print(list(files))
