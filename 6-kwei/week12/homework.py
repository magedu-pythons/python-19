# 1、使用python给自己qq邮箱发送一份邮件
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = "senderQQnum@qq.com"
receiver = "receiverQQnum@qq.com"

subject = 'python test'
smtp_server = 'smtp.qq.com'

username = 'userQQnum@qq.com'
password = '授权码'

sendmsg = MIMEText('hellooooooooooooooooooooooooooo oooo!')
sendmsg["Subject"] = Header(subject)
sendmsg["From"] = 'Me'
sendmsg["to"] = 'Myself'

try:
    smtp = smtplib.SMTP()
    smtp.connect(smtp_server)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, sendmsg.as_string())
    smtp.quit()
    print('Success!')
except Exception:
    print('Error')

# 2、实现一个函数获取一个目录下所有以.py结尾的文件（包含目录下的子目录中的.py文件）
from pathlib import Path
import os

# 递归 , 将每个文件夹下的文件
# 文件夹 -> enter
# 不是文件夹 -> 以.py结尾就添加到list中

p = Path('/Users/wk/pythonwork')
print(p.absolute())


def find_py(path, res=[]):
    for item in os.listdir(path):
        filename = path / item
        if filename.is_dir():
            find_py(filename)
        else:
            if (filename).suffix == '.py':
                res.append(item)
    return res


# test
print(find_py(p))





"""
(0 + 0)

    函数参数不要用list
"""