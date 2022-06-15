import smtplib, ssl

port = 465  # For SSL
#password = input("Type your password and press enter: ")
password =  "<:kK11kK$$:>"

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("kresimir.ivkovic@gmail.com", password)
    # TODO: Send email here

    sender_email = "kresimir.ivkovic@gmail.com"
    receiver_email = "kresimir.ivkovic@windowslive.com"
    message = """\
        Subject: Hi there

    This message is sent from Python."""

    server.sendmail(sender_email, receiver_email, message)


