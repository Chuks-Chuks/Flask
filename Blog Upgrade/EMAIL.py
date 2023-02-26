import smtplib
import os
import dotenv

project_folder = os.path.expanduser('../startbootstrap-clean-blog-gh-pages')
dotenv.load_dotenv(os.path.join(project_folder, '.env'))


class Email:
    def __init__(self, senders_mail, message):
        self.receiver_email = os.getenv('receiver_email')
        self.senders_mail = senders_mail
        self.smtp_address = os.getenv('smtp_address')
        self.message = message
        self.password = os.getenv('password')
        self.send_mail()

    def send_mail(self):
        with smtplib.SMTP(self.smtp_address) as connection:
            connection.starttls()
            connection.login(self.receiver_email, self.password)
            connection.sendmail(self.senders_mail,
                                self.receiver_email,
                                f"Subject: New Message\n\n{self.message}")
