import smtplib
print "import"
handle = smtplib.SMTP('smtp.xingcloud.com', 25)
print "start"
handle.ehlo()
#handle.starttls()
handle.ehlo()
print "login"
handle.login('zhangxiaoyang@xingcloud.com', 'Pass@w0rd')
print 1
msg = "Subject: pythoentestnotttl \r\n\r\n python send test mail\r\n"

print 2
handle.sendmail('zhangxiaoyang@xingcloud.com','tribieal@gmail.com', msg)
print 3
handle.close()


