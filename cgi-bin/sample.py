#!C:\Program Files (x86)\Python36-32\python.exe

print("Content-Type: text/html\r\n")
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import codecs
from genpdf import generate
import os
import cgi

f = cgi.FieldStorage()
designation = f.getvalue('designation')
dept = f.getvalue('dept')
msg1 = f.getvalue('msg')
		#print(name)
gmail_user = 'ahamedmusthafars@gmail.com'
gmail_pwd = '***********'	#Provide your required password
FROM = 'ahamedmusthafars@gmail.com'
TO = ['amrstech@gmail.com']
SUBJECT = 'GCT Website Grievances form mail - reg'
TEXT = 'For GCT website - Grievances, this mail is automated to notify the form submission by a user with the pdf attachment'
#message = "From: "+FROM+"\nTo: "+TO+"\nSubject: "+SUBJECT+"\n\n"+TEXT
try:
	generate(designation,dept,msg1)
	msg = MIMEMultipart()
	msg['Subject'] = SUBJECT 
	msg['From'] = FROM
	msg['To'] = ','.join(TO)
	msg.attach(MIMEText(TEXT))

	part = MIMEBase('application', "octet-stream")
	part.set_payload((codecs.open("C:\\xampp\\cgi-bin\\output.pdf", "rb")).read())
	encoders.encode_base64(part)

	part.add_header('Content-Disposition', 'attachment; filename="Attachment.pdf"')

	msg.attach(part)

	server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
	#server_ssl.ehlo()  optional, called by login()
	server_ssl.login(gmail_user, gmail_pwd)  
	# ssl server doesn't support or need tls, so don't call server_ssl.starttls() 
	server_ssl.sendmail(FROM, TO, msg.as_string())
	#server_ssl.quit()
	server_ssl.close()

	print('<!DOCTYPE html> <html> <head> <title>Sample Part of GCT Page</title> </head> <style type="text/css"> body{ background-color: rgb(0,32,96); } img{ padding: 10px 40px 20px 40px; } #navbar{ background-color: yellow; margin-top: 10px; margin-bottom: 0px; width: 100%; height: 50px; border-bottom: 1px solid black; border-radius:8px 8px 0 0; } div p{ padding-left: 48px; padding-top: 15px; font-size: 15px; font-weight: 600; font-family: sans-serif; } #whitetxt{ padding-top: 15px !important; padding-left: 48px !important; } div p a{ text-decoration: none; color: black; } #white{ background-color: white; height: 500px; /*border: solid 1px black;*/ } #formdiv{line-height:25px; height: 15px;margin: 10px 400px 100px 400px; padding-bottom: 20px; border: 1px solid black; border-radius: 8px; box-shadow: 5px 8px 25px; } textarea{ vertical-align: top; } </style> <body> <!-- <form action = "/cgi-bin/sample.py" method = "post"> <input type = "text" name = "Name"><br> <input type="submit" value="Submit"><br> </form> --> <a href="http://gct.ac.in"><img src="/gct/gct.png"></a> <div id="navbar"> <p><a href="/gct/">Grievances</a></p> </div> <div id="white"> <div id="whitetxt"> You can fill out this form to report your grievances. </div> <br> <div id="formdiv" align="center"> Your message is successfully submitted. </div> </div> </body> </html>')

except:
	print('<!DOCTYPE html> <html> <head> <title>Sample Part of GCT Page</title> </head> <style type="text/css"> body{ background-color: rgb(0,32,96); } img{ padding: 10px 40px 20px 40px; } #navbar{ background-color: yellow; margin-top: 10px; margin-bottom: 0px; width: 100%; height: 50px; border-bottom: 1px solid black; border-radius:8px 8px 0 0; } div p{ padding-left: 48px; padding-top: 15px; font-size: 15px; font-weight: 600; font-family: sans-serif; } #whitetxt{ padding-top: 15px !important; padding-left: 48px !important; } div p a{ text-decoration: none; color: black; } #white{ background-color: white; height: 500px; /*border: solid 1px black;*/ } #formdiv{line-height:25px; height: 15px;margin: 10px 400px 100px 400px; padding-bottom: 20px; border: 1px solid black; border-radius: 8px; box-shadow: 5px 8px 25px; } textarea{ vertical-align: top; } </style> <body> <!-- <form action = "/cgi-bin/sample.py" method = "post"> <input type = "text" name = "Name"><br> <input type="submit" value="Submit"><br> </form> --> <a href="http://gct.ac.in"><img src="/gct/gct.png"></a> <div id="navbar"> <p><a href="/gct/">Grievances</a></p> </div> <div id="white"> <div id="whitetxt"> You can fill out this form to report your grievances. </div> <br> <div id="formdiv" align="center"> Some Techincal issues. </div> </div> </body> </html>')
	
try:
	os.remove('C:\\xampp\\cgi-bin\\output.pdf')
except:
	print('')
