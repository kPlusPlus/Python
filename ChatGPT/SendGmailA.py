import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# create message object
msg = MIMEMultipart()
msg['From'] = 'kresimir.ivkovic@gmail.com'
msg['To'] = 'kresimir.ivkovic@gmail.com'
msg['Subject'] = 'Test email from Python'

# add body to message
body = 'Hello, this is a test email from Python.'
msg.attach(MIMEText(body, 'plain'))

# establish connection with SMTP server
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'kresimir.ivkovic@gmail.com'
smtp_password = '@@<:kK11kK$$:>@@'

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    print('Email sent successfully!')
except Exception as e:
    print(f'Error: {e}')
finally:
    if server is not None:
        server.quit()
