#1����������һ���б�����ҳ�xԪ���Ƿ����б����棬������ڷ���1�������ڷ���0
#����1
lst=list(input(">>>"))
flag=True
while flag:
    x=input(">>>")
    if x=='out':
        flag=False
    print("1") if x in lst else print("0")

#����2
lst=list(input(">>>"))
while True:
    x=input(">>>")
    if x=='out':
        break
    print("1") if x in lst else print("0")
    
#��һ��Ӣ�ĵĴ��ı��ļ���ͳ�����еĵ��ʳ��ֵĸ�����
#����һ��
strings="""A graphical interface from the late 1980s, which features a TUI window for a man page. Another text window for a Unix shell is partially visible.
In computing, a shell is a user interface for access to an operating system's services. In general, operating system shells use either a command-line interface (CLI) or graphical user interface (GUI), depending on a computer's role and particular operation. It is named a shell because it is the outermost layer around the operating system kernel.[1][2]
CLI shells require the user to be familiar with commands and their calling syntax, and to understand concepts about the shell-specific scripting language (for example bash script). They are also more easily operated via refreshable braille display, and provide certain advantages to screen readers.Graphical shells place a low burden on beginning computer users, and are characterized as being easy to use. Since they also come with certain disadvantages, most GUI-enabled operating systems also provide CLI shells."""
lst1=list(strings.split())
print(lst1)
lst2=[]
for i in lst1:
    if i not in lst2:
        lst2.append(i)
        print("{} is appear {} times".format(i,lst1.count(i)))

#��������
strings="""A graphical interface from the late 1980s, which features a TUI window for a man page. Another text window for a Unix shell is partially visible.
In computing, a shell is a user interface for access to an operating system's services. In general, operating system shells use either a command-line interface (CLI) or graphical user interface (GUI), depending on a computer's role and particular operation. It is named a shell because it is the outermost layer around the operating system kernel.[1][2]
CLI shells require the user to be familiar with commands and their calling syntax, and to understand concepts about the shell-specific scripting language (for example bash script). They are also more easily operated via refreshable braille display, and provide certain advantages to screen readers.Graphical shells place a low burden on beginning computer users, and are characterized as being easy to use. Since they also come with certain disadvantages, most GUI-enabled operating systems also provide CLI shells."""
lst1=list(strings.split())
set1=set(lst1)
for i in set1:
    print("{} is appear {} times".format(i,lst1.count(i)))



"""
(0 + 0)

    第二题请参考答案实现
"""

