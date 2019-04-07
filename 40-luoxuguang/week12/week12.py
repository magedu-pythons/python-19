#1、使用python给自己qq邮箱发送一份邮件

# 参考网络上源码,学习发邮件的流程
# 发邮件需要借助符合POP3、SMTP和IMAP等协议的邮件服务器,通过python调用这些服务器实现发邮件
#
# import smtplib #smtplib用来配置邮件设置
# from email.mime.text import MIMEText #email构造邮件内容
#
# msg = MIMEText("this is a email from python") # 构造MIMEText对象
#
# s = smtplib.SMTP_SSL("smtp.qq.com",465) #设置邮件服务器，需要到qq邮箱开启SMTP服务
# s.login('1055728589@qq.com', "tnlnxztgjvszbdaa") #登录邮箱和授权码，不是密码
# s.sendmail('1055728589@qq.com', "373575483@qq.com", msg.as_string())
# s.quit()

#最终发送邮件成功，邮件格式还可以继续完善，但此次作业到这里就可以了


#2、实现一个函数获取一个目录下所有以.py结尾的文件（包含目录下的子目录中的.py文件）
from pathlib import Path

def searcher(pathname:str):
    path = Path(pathname)
    matcher = path.rglob("*.py")
    for file in matcher:
        yield file.name

for i in searcher("C:\python-code\practice"):
    print(i)




"""
(0 + 0)

    第二题尝试自行实现，不用模块
"""