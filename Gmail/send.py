# https://mailtrap.io/blog/python-send-email-gmail/
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

subject = "Email Subject"
body = "This is the body of the text message"
sender = "tvrdiovan@gmail.com"
recipients = ["kresimir.ivkovic@gmail.com", "kresimir.ivkovic@gmail.com"]
password = "dges xxsb xcet yadh"


def send_email(sender_email, receiver_email, password, subject, message):
    # Create a secure SSL context
    context = ssl.create_default_context()

    # Set up the MIME
    email = MIMEMultipart()
    email['From'] = sender_email
    email['To'] = receiver_email
    email['Subject'] = subject

    # Attach the message to the email
    email.attach(MIMEText(message, 'plain'))

    # Log in to the SMTP server and send the email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, email.as_string())


#send_email(subject, body, sender, recipients, password)
#send_email(sender, recipients, password, subject, body)


# Connect to Gmail's SMTP server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

# Login to Gmail
server.login(sender, password)

# Send the email
server.sendmail(sender, recipients, message.as_string())

# Close the SMTP server connection
server.quit()

print("Email sent successfully.")