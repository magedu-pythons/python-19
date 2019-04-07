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
#��Ϊ[[]]*5,�൱�������Ԫ�ؿ�����5��,ÿ��Ԫ�ص�id����һ����,ָ���ڴ��ͬһ����ַ, li[0].append(10)��ִ��,����ÿһ���б��ﶼ�����10,ͬ��li[1].append(20), ��li.append(30), li�б�������ˣ�������ڴ��ַ
a = []
a.sort()




"""
(0 + 0)

    还行
"""