#using starttls to secure the connection from a point onwards
import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 465 #587  # For starttls
sender_email = "tvrdiovan@gmail.com" # Enter your address
receiver_email = "kresimir.ivkovic@gmail.com" # Enter receiver address
password = "dges xxsb xcet yadh" #input("Input password and press enter: ")
message = """\
Subject: Hi there

Message body after 2 new lines."""

# Create a secure SSL context, loads system's default trusted CAs
context = ssl.create_default_context()

# Try block 

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted, called implicitly by the method if required
    server.starttls(context=context)
    server.ehlo()  # Can be omitted, called implicitly by the method if required
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    

server.quit() 