import smtplib
import os


def load_smtp_conf():
    s = smtplib.SMTP("smtp.gmail.com:587")
    s.starttls()
    username = os.environ['SITECHECKER_SMTP_USERNAME']
    password = os.environ['SITECHECKER_SMTP_PASSWORD']
    s.login(username, password)
    return s
