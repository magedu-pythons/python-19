# a = "1,2,3".split(',')
# print(a)


from pathlib import Path
import shutil

dstdir = Path('C:\Python\magedu_class\ini-test')
srcfile = Path('C:\Python\magedu_class\learn argparse\pactice.text')
def copyfile_dir(srcfile, dstdir):
    index = srcfile.name.find('.')
    srcfilename = srcfile.name[:index]
    srcfileformat = srcfile.name[index+1:]
    copy_srcfilename = srcfilename+'2'+'.'+srcfileformat
    dstdir = dstdir.joinpath(copy_srcfilename)
    with open(str(dstdir), 'w') as f1:
        with open(str(srcfile)) as f2:
            a = f2.read()
            f1.write(a)

copyfile_dir(srcfile, dstdir)

li = [[]]*5
li[0].append(10)
print(li)
li[1].append(20)
print(li)
li.append(30)
print(li)
#[[10, 20], [10, 20], [10, 20], [10, 20], [10, 20], 30]
#因为[[]]*5,相当于里面的元素拷贝了5份,每个元素的id都是一样的,指向内存的同一个地址, li[0].append(10)当执行,里面每一个列表里都添加了10,同理li[1].append(20), 当li.append(30), li列表中添加了３０这个内存地址
a = []
a.sort()