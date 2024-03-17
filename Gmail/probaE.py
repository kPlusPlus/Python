import smtplib

sender_email = "tvrdiorah@gmail.com"
rec_email = "kresimir.ivkovic@gmail.com"
password = "dges xxsb xcet yadh"
message = "Hey,  Mikuli je puno Mali"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, password)
print("Login success")
server.sendmail(sender_email, rec_email, message)
print("Email has been sent")