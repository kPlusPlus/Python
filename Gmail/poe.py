# PoE
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl

sender_email = "tvrdiovan@gmail.com"
sender_password = "dges xxsb xcet yadh" # "brodicmaleni500" #"dges xxsb xcet yadh"
recipient_email = "kresimir.ivkovic@example.com"
subject = "Test Email"
body = "This is a test email sent through Gmail SMTP."

try:
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    # with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    #     smtp.starttls()
    #     smtp.login(sender_email, sender_password)
    #     smtp.send_message(message)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.user = sender_email 
        server.password = sender_password
        server.auth_login()
        server.sendmail(sender_email , recipient_email, message)
        server.close()


    print("Email sent successfully!")
except Exception as e:
    print("Failed to send email. Error:", str(e))