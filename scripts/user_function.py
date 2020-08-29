from  System_Setup import SystemSetup
SystemSetup()



from uploadImages import uploadImages
from  upload_products_WebApp import upload_products
from  report_mail import mail_report


d = uploadImages()

upload_products(d)

mail_report("shahysh1999@gmail.com")


