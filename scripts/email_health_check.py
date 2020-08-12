import mimetypes
import smtplib
import ssl
import getpass
from email.message import EmailMessage


def generate_mail(Subject):
	
	message = EmailMessage()
	message['From'] = "yashshah2025@gmail.com"
	message['To'] = "yashshah2025@gmail.com"
	
	Body = "Please check your system and resolve the issue as soon as possible."
	message['Subject'] = Subject
	message.set_content(Body)
	return message

    # if(attachment_path != None):
    # 	attachment_filename = os.path.basename(attachment_path)
    #     mime_type, _ = mimetypes.guess_type(attachment_path)
    #     mime_type, mime_subtype = mime_type.split('/', 1)

    #     with open(attachment_path, 'rb') as ap:
    #         message.add_attachment(ap.read(),
    #             maintype=mime_type,
    #             subtype=mime_subtype,
    #             filename=os.path.basename(attachment_path))




def send_mail(Subject):
	sender = "yashshah2025@gmail.com"
	message = generate_mail(Subject)
	mail_server = smtplib.SMTP_SSL("smtp.gmail.com")
	password = getpass.getpass('Password? ')
	mail_server.login(sender, password)
	mail_server.send_message(message)
	mail_server.set_debuglevel(1)