import reports
import emails
import os

path =  "/mnt/c/Users/91894/SHOP24/supplier-data/descriptions/"
path_to_report = reports.generate_report(path)

reciever = "shahysh1999@gmail.com"
message = emails.generate_mail(reciever,path_to_report)
emails.send_mail(message)
