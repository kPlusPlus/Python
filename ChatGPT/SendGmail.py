import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# set up email components
email_from = "kresimir.ivkovic@gmail.com"
email_to = "kresimir.ivkovic@gmail.com"
email_subject = "Test Email from Python"
email_body = "This is a test email sent from Python."

# create message object
msg = MIMEMultipart()
msg['From'] = email_from
msg['To'] = email_to
msg['Subject'] = email_subject

# attach body to message
msg.attach(MIMEText(email_body, 'plain'))

# attach image to message (optional)
with open('image.jpg', 'rb') as f:
    img_data = f.read()
    image = MIMEImage(img_data, name='image.jpg')
    msg.attach(image)

# establish connection with SMTP server
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "kresimir.ivkovic@gmail.com"
smtp_password = "@@<:kK11kK$$:>@@"

server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(smtp_username, smtp_password)

# send message and close server connection
server.sendmail(email_from, email_to, msg.as_string())
server.quit()
