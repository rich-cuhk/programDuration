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
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = email_address
    msg['To'] = user_email

    ## create email server
    import smtplib
    server = smtplib.SMTP_SSL(email_server, email_port)
    # server.starttls()
    server.login(email_address, email_password)
    server.sendmail(email_address, user_email, msg.as_string())
    server.quit()

    print(f'email sent to {user_email}')


if __name__ == '__main__':
    send_email('liujunbiao@163.com', 'test', 'test')
