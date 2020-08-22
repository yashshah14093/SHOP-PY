from django.db import models

# Create your models here.
class Product(models.Model):
    image = models.FilePathField(path = "img/")
    description = models.TextField()


