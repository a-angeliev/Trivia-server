import smtplib

from decouple import config


class EmailSenderManager:
    @staticmethod
    def send_email(email, massage):
        # server = smtplib.SMTP(config("MAIL_SERVICE"), config("MAIL_PORT"))
        # server.starttls()
        # server.login(config("MAIL_USERNAME"), config("MAIL_PASSWORD"))
        # server.sendmail(config("MAIL_USERNAME"), f"{email}", massage)
        return "Send email"
