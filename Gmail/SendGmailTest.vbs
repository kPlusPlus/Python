'***********************
'Name:    Email Messages
'Author:  Jeremy England
'Company:    SimplyCoded
'Version:        rev.001
'Date: 	       1/02/2015
'***********************
Option Explicit
Dim objFSO : Set objFSO = CreateObject("Scripting.FileSystemObject")
Dim objSHL : Set objSHL = CreateObject("WScript.Shell")
Dim objMessage, Email, EPass, DroppedFile
Dim strSubject, strTxtBody, strToEmail, strAttach

On Error Resume Next

strSubject = "Pisem pisem pismo" 'InputBox("Subject...", "Subject")
CancelQuit strSubject
strTxtBody = "Malo test pismo. Moramo sve to proći" 'InputBox(strSubject&vbLf&string(80, "-")&vbLf&"Message...", "Message")
CancelQuit strTxtBody
strToEmail = "kresimir.ivkovic@gmail.com" 'InputBox(strSubject&vbLf&string(80, "-")&vbLf&strTxtBody&vbLf&vbLf&"Send to...","Send To","someone@somewhere.com")
CancelQuit strToEmail


Call Credentials()

If Not Err.Number = 0 Then 
Select Case MsgBox("Your email address or password is possibly wrong, or you tried to attach a vbs, bat, or exe file (others may apply as well). Do you want to try and enter your email and password again?",vbYesNo+vbExclamation, "Error")
Case vbYes
Call Credentials()
Case vbNo
MsgBox "Canceled",vbCritical
WScript.Quit
End Select
End If


'Cancel Function for InputBox strings
'-------------------------------------
Function CancelQuit(testVar)
	If IsEmpty(testVar) Then
	MsgBox "Canceled",vbCritical
	WScript.Quit
	End If
End Function


'Configuration information for the remote SMTP server.
'-----------------------------------------------------

Function Credentials()
 Email = "kresimir.ivkovic@gmail.com" 'InputBox(string(5, vbLf)& "Enter your Gmail address.","Emailing: "&strToEmail, "username@gmail.com")
 CancelQuit Email
 EPass = "brodicmaleni500" 'dges xxsb xcet yadh" 'InputBox(string(5, vbLf)& "Password for: "&Email,"Emailing: "&strToEmail)
 CancelQuit EPass
 SENDEmail()
End Function 


Function SENDEmail()
 Set objMessage = CreateObject("CDO.Message")
 objMessage.Subject = strSubject
 objMessage.From = Email
 objMessage.To = strToEmail
 objMessage.TextBody = strTxtBody
	If WScript.Arguments.Count > 0 Then
      For Each DroppedFile in Wscript.Arguments 
 	  objMessage.AddAttachment DroppedFile
 	  strAttach = strAttach & DroppedFile & vbLf
 	  Next 
	 Else
	  Select Case MsgBox("No files attached. To attach a file/files please drop it/them onto the vbscript icon. Send anyway?" ,vbYesNo+vbInformation)
	  Case vbNo
	  WScript.Quit
	  End Select	
	End If 
 objMessage.Configuration.Fields.Item _
 ("http://schemas.microsoft.com/cdo/configuration/sendusing") = 2
 
 'Name or IP of Remote SMTP Server
 objMessage.Configuration.Fields.Item _
 ("http://schemas.microsoft.com/cdo/configuration/smtpserver") = "smtp.gmail.com"

 objMessage.Configuration.Fields.Item _
 ("http://schemas.microsoft.com/cdo/configuration/smtpauthenticate") = 1

 'Your UserID on the SMTP server
 objMessage.Configuration.Fields.Item _
 ("http://schemas.microsoft.com/cdo/configuration/sendusername") = Email

 'Your password on the SMTP server
 objMessage.Configuration.Fields.Item _
 ("http://schemas.microsoft.com/cdo/configuration/sendpassword") = EPass

 'Server port (typically 25)
 objMessage.Configuration.Fields.Item _
 ("http://schemas.microsoft.com/cdo/configuration/smtpserverport") = "465"

 'Use SSL for the connection (False or True)
 objMessage.Configuration.Fields.Item _
 ("http://schemas.microsoft.com/cdo/configuration/smtpusessl") = True

 'Connection Timeout in seconds (the maximum time CDO will try to establish a connection to the SMTP server)
 objMessage.Configuration.Fields.Item _
 ("http://schemas.microsoft.com/cdo/configuration/smtpconnectiontimeout") = 60

 objMessage.Configuration.Fields.Update
 objMessage.Send

 If IsEmpty(strAttach) then
  MsgBox "Message Sent",vbInformation
 Else
  MsgBox "Message Sent" &vbLf&strAttach,vbInformation
 End If
End Function