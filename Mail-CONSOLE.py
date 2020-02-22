#!/usr/bin/python
import smtplib,ssl
port=465
password='kULDEEP11@$@'
Context=ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",port,context=Context) as server :
    sender_email="mr.vikramkx@gmail.com"
    server.login(sender_email,password)
    reciver_email="vikashburdak04@gmail.com"
    msg='Subject : This is test email from python'
    server.sendmail(sender_email,reciver_email,msg)