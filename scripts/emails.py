import mimetypes
import smtplib
import ssl
import getpass
from email.message import EmailMessage


def generate_mail(reciever,attachment-path = None,):
	
	message = EmailMessage()
	message['From'] = "automation@example.com"
	message['To'] = reciever
	
	Subject = "Upload Completed - Online Fruit Store"
	Body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
	message['Subject'] = Subject
	message.set_content(Body)
    
    if(attachment-path != None):
    	attachment_filename = os.path.basename(attachment_path)
        mime_type, _ = mimetypes.guess_type(attachment_path)
        mime_type, mime_subtype = mime_type.split('/', 1)

        with open(attachment_path, 'rb') as ap:
            message.add_attachment(ap.read(),
                maintype=mime_type,
                subtype=mime_subtype,
                filename=os.path.basename(attachment_path))

    return message



def send_mail(message):
	mail_server = smtplib.SMTP_SSL("smtp.example.com")
	password = getpass.getpass('Password? ')
	mail_server.login(sender, password)
	mail_server.send_message(message)
	mail_server.set_debuglevel(1)