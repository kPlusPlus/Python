Option Explicit

Const EMAIL_USERNAME = "tvrdiovan@gmail.com"
Const EMAIL_PASSWORD = "dges xxsb xcet yadh"
Const SMTP_SERVER = "smtp.gmail.com"
Const SMTP_PORT = 587

Dim objEmail
Set objEmail = CreateObject("CDO.Message")

objEmail.From = EMAIL_USERNAME
objEmail.To = "kresimir.ivkovic@example.com"
objEmail.Subject = "Test email from VBScript"
objEmail.TextBody = "This is a test email sent from VBScript."

' Configure SMTP server settings
objEmail.Configuration.Fields.Item("http://schemas.microsoft.com/cdo/configuration/sendusing") = 2 ' cdoSendUsingPort
objEmail.Configuration.Fields.Item("http://schemas.microsoft.com/cdo/configuration/smtpserver") = SMTP_SERVER
objEmail.Configuration.Fields.Item("http://schemas.microsoft.com/cdo/configuration/smtpserverport") = SMTP_PORT
objEmail.Configuration.Fields.Item("http://schemas.microsoft.com/cdo/configuration/smtpusessl") = True
objEmail.Configuration.Fields.Item("http://schemas.microsoft.com/cdo/configuration/smtpauthenticate") = 1 ' cdoBasic
objEmail.Configuration.Fields.Item("http://schemas.microsoft.com/cdo/configuration/sendusername") = EMAIL_USERNAME
objEmail.Configuration.Fields.Item("http://schemas.microsoft.com/cdo/configuration/sendpassword") = EMAIL_PASSWORD
objEmail.Configuration.Fields.Update

' Send the email
objEmail.Send

' Cleanup
Set objEmail = Nothing

WScript.Echo "Email sent successfully."
