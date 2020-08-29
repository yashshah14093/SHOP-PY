from products.models import Product

def upload_object(name,quantity,image,description):
    prod_obj = Product(Name = name, Quantity = quantity, Image = image, Description = description)
    prod_obj.save()

