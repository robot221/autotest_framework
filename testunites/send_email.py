# -*- coding:utf-8 -*-

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

msg = MIMEMultipart('mixed')
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.baidu.com"
text_plain = MIMEText(text, 'plain', 'utf-8')
msg.attach(text_plain)
sender = 'dxs86@163.com'
password = 'dxs8806'
receiver = ['daixs@hicando.com', '282497745@qq.com']
smtp_server = 'smtp.163.com'
msg['From'] = sender
msg['To'] = ",".join(receiver)
msg['Subject'] = 'python'
msg['Date'] = '2019-04-20'

server = smtplib.SMTP()
server.connect(smtp_server,25)
#server.starttls()
server.login(sender,password)
server.set_debuglevel(1)
server.sendmail(sender,receiver,msg.as_string())
server.quit()