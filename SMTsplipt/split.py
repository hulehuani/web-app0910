# -*- coding: utf-8 -*-
# @Time: 2020/9/3 23:59
# @Author : huahua
# @Email : 523258779@qq.com
# @File :  split.py

import smtplib   #发送邮件模块
from email.mime.text import MIMEText    #邮件内容
from email.header import Header



def send_email(new_reportfile):
    """发送邮件"""
    f = open(new_reportfile,'rb')
    mail_content = f.read()

    # 发送邮箱服务器
    smtpserver = 'smtp.qq.com'

    # 用户名密码
    user = '523258779@qq.com'
    password = 'mxweymtlkptubggf'
    # 发送和接收邮箱用户
    sender = '523258779@qq.com'
    receiver = '577512689@qq.com'
    # 发送给多人
    # receiver = ['123@qq.com',  '23432@qq.com','719584032@qq.com']

    # 定义标题和内容
    biaoti = "my_fist自动化测试报告"

    # HTML邮件正文
    msg = MIMEText(mail_content, 'html', 'utf-8')
    msg['subject'] = Header(biaoti, 'utf-8')
    msg['from'] = sender
    msg['to'] = receiver
    # 发送给多人，已逗号为分隔符，针对receiver这个变量
    #   msg['to'] =','.join(receiver)

    # SSL协议端口号要使用465
    smtp = smtplib.SMTP_SSL(smtpserver, 465)

    # HELO 像服务器标识用户身份
    smtp.helo(smtpserver)
    # 服务器返回结果确认
    smtp.ehlo(smtpserver)
    # 登陆用户
    smtp.login(user, password)
    print("开始发送邮件.............")
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print("邮件发送完成.....................")
if __name__ == '__main__':
    path = 'D:/pycharm_worlkspace/untitled5/Testcase/report_0829.html'
    send_email(path)