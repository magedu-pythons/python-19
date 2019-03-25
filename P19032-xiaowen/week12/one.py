#!/usr/local/python3/bin/python3
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = "root@localhost.localdomain"
receivers = "815148805@qq.com"
message = MIMEText('python email text', 'plain', 'utf-8')
message['From'] = Header("localhost", 'utf-8')
message['TO'] = Header('text', 'utf-8')

subject = 'python smtp text'
message['subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print('successful')
except smtplib.SMTPException:
    print("Error: failed")

