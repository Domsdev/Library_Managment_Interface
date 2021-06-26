import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import environ
import sys, traceback
import datetime

##############################################################################

def html_body_activation_code(name, code):

	subject = "Domsdev library - Activation code"

	# format message body using HTML + CSS

	email_body_header = f"""
	<html><head></head><body>
	<style type="text/css"></style>
	<br><p>	Hello {name},<br>
	<br>Welcome to Domsdev library !<br>"""

	email_body_content = f"""
	<H2>Here is your activation code: {code}</h2>"""

	email_body_footer = """
	<br>Thank you,<br>
	<br>Domsdev library Support Team.<br>"""

	email_body = email_body_header + email_body_content + email_body_footer

	return email_body, subject

##############################################################################

def html_body_new_activation_code(name, code):

	subject = "Domsdev library - New activation code"

	# format message body using HTML + CSS

	email_body_header = f"""
	<html><head></head><body>
	<style type="text/css"></style>
	<br><p>	Hello {name},<br>"""

	email_body_content = f"""
	<H2>Here is your new activation code: {code}</h2>"""

	email_body_footer = """
	<br>Thank you,<br>
	<br>Domsdev library Support Team.<br>"""

	email_body = email_body_header + email_body_content + email_body_footer

	return email_body, subject

##############################################################################

def Send_mail(receiver, html_body, subject):
	"send an HTML email"

	sender = environ.get('SENDER_MAIL')
	password = environ.get('PASSWORD_MAIL')

	message = MIMEMultipart('alternative')
	message["Subject"] = subject
	message["From"] = sender
	message["To"] = receiver

	# turn html_body in MIMEText object
	part = MIMEText(html_body, "html")

	# attach html to MIMEMultipart message
	message.attach(part)

	# convert message to string format
	message = message.as_string()

	# create secure connection with server and send email
	context = ssl.create_default_context()

	#server.set_debuglevel(True)

	try:
		server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context= context)
		server.login(sender, password)
		server.sendmail(sender, receiver, message)
		print('Info: sending mail to user')

	except:
		date_of_today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		
		traceback_lines = traceback.format_exc().splitlines()
		print(traceback_lines[-1])

		with open('error.txt', 'w') as f:
			f.write(f"\n\nError occured: {date_of_today}\n")
			for k in range(len(traceback_lines)):
				f.write(traceback_lines[k])
		return False

	else:
		server.quit()
		return True

	# with smtplib.SMTP_SSL("smtp.gmail.com", 465, context= context) as server:
	#    server.login(sender, password)
	#    server.sendmail(sender, receiver, message)

##############################################################################

def Send_mail_with_attachment(sender, password, receiver,
	                          subject, html_body, file):
	"create a message with attached file using the email Package"
	
	# Create a multipart message and set headers
	message = MIMEMultipart('alternative')
	message["Subject"] = subject
	message["From"] = sender
	# message["To"] = receiver

	message["Bcc"] = receiver
	# Bcc recommended for mass emails
	# as nobody can see email adresses of the receiver list

	# Add html_body to email
	message.attach(MIMEText(html_body, "html"))

	# Open file in binary mode
	with open(file, "rb") as f:
	    # Add file as application/octet-stream
	    # Email client can usually download this automatically as attachment
	    attached_file = MIMEBase("application", "octet-stream")
	    attached_file.set_payload(f.read())

	# Encode file in ASCII characters to send by email
	encoders.encode_base64(attached_file)

	# Add header as key/value pair to attachment part
	attached_file.add_header('Content-Disposition',
		                     'attachment',
		                     filename= file)
	# 'inline' file Content-disposition option exists

	# Add attachment to message
	message.attach(attached_file)

	# convert message to string format
	message = message.as_string()

	# Log in to server using secure context and send email
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
	    server.login(sender, password)
	    server.sendmail(sender, receiver.split(','), message)

##############################################################################

def plain_text_tls_mail(sender, receiver, password, message_body):

	port = 587  # For starttls
	smtp_server = "smtp.gmail.com"
	# sender = "sender@gmail.com"
	# receiver = "receiver@gmail.com"
	# password = input("Enter password:")

	message_exemple = """\
	Subject: How to send e-mail
	using SMTP and TLS (Transport Layer Security) protocol
	
	This message is sent from Python. \
	starttls start an unsecured SMTP connection \
	that can then be encrypted using .starttls()"""

	context = ssl.create_default_context()	
	with smtplib.SMTP(smtp_server, port) as server:

	    server.starttls(context=context)
	    server.login(sender, password)
	    server.sendmail(sender, receiver, message_body)

##############################################################################

if __name__ == '__main__':
	# Testing

	receiver = input("enter receiver mail adress")

	html_body, subject = html_body_activation_code('Huguette Pallant', 778265)

	Send_mail(receiver, html_body, subject)
