import smtplib

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login('@gmail.com', 'pass')
    server.sendmail('from', 'to', "msg")
    server.close()

    print("email sent")
except Exception as e:
    print(e)