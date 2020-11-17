import smtplib
from email.message import EmailMessage

user_mail = ''

class MailHelper:

    def __init__(self) -> None:
        self.server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        self.server.ehlo()
        self.server.login(user_mail, '')

    def send_mail(self, to: str, message: str, subject: str) -> None:
        mail = EmailMessage()
        mail.set_content(message)
        mail['Subject'] = subject
        mail['From'] = user_mail
        mail['To'] = to

        self.server.send_message(mail)

    def close_connection(self) -> None:
        self.server.close()
