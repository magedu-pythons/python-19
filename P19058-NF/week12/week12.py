# 使用python给自己qq邮箱发送一份邮件


import smtplib
from email.mime.text import MIMEText
import sys

sendusr = '634942686@qq.com'
password = 'xfrikzhpcgllbdfd'
reciveruer = '1003407840@qq.com'


subject = 'With Python'
content = 'use python send email'
msg = MIMEText(content)     #MIMEText实例
msg['Subject'] = subject
msg['From'] = sendusr
msg['To'] = reciveruer

try:
    s = smtplib.SMTP_SSL('stmp.qq.com', port=465)
    s.login(sendusr, password)
    s.sendmail(sendusr, reciveruer,msg.as_string())
    print('success')
except:
    print('fail', sys.exc_info())
finally:
    s.quit()



# 实现一个函数获取一个目录下所有以.py结尾的文件（包含目录下的子目录中的.py文件）
from pathlib import Path


def packageiter(p1):
    for file in p1.iterdir():
        if str(file).endswith('.py'):
            yield file
        elif file.is_dir():
            for file2 in file.iterdir():
                if str(file2).endswith('.py'):
                    yield file2
                else:
                    if file2.is_dir():
                        packageiter(file2)


p1 = Path('C:\Python\magedu_class\magedu')
packageiter(p1)
