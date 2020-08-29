import reports
import emails
import os

def mail_report(supplier):
    path =  "/mnt/c/Users/91894/Desktop/SHOP-PY/supplier-data/descriptions/"
    path_to_report = reports.generate_report(path)

    reciever = supplier
    message = emails.generate_mail(reciever,path_to_report)
    emails.send_mail(message)
