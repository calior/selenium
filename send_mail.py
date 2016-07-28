#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

smtpserver = 'smtp.163.com'
user = 'lijianhua1126@163.com'
password = 'Li13193812434@Li'
sender ='lijianhua1126@163.com'
receiver = 'lijianhua1126@163.com'
subject = 'python写的第一封邮件'
msg = MIMEText('<html><h1>你好!</html></h1>','html','utf-8')
msg['Subject'] = Header(subject,'utf-8')


smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user,password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()