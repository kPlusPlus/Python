import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email content
sender_email = "tvrdiovan@gmail.com"
sender_password = "brodicmaleni500" #"dges xxsb xcet yadh"
recipient_email = "kresimir.ivkovicgmail.com"
subject = "Test email from Python"
body = "This is a test email sent from Python."

# Create the email message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = recipient_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

# Connect to Gmail's SMTP server
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, message.as_string())

print("Email sent successfully.")
