# create function to send an email using mail.163.com server to the user
from email.mime.text import MIMEText


def send_email(user_email, subject, body):

    ## import email credential from .env file
    from dotenv import load_dotenv
    import os
    load_dotenv()
    email_address = os.getenv('EMAIL_ADDRESS')
    email_password = os.getenv('EMAIL_PASSWORD')
    email_server = os.getenv('EMAIL_SERVER')
    email_port = os.getenv('EMAIL_PORT')


    ## create email message
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = email_address



