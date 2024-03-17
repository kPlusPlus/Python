import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("tvrdiovan@gmail.com", "dges xxsb xcet yadh")
server.sendmail(
  "tvrdiovan@gmail.com", 
  "kresimir.ivkovic@gmail.com", 
  "this message is from python")
server.quit()