from django.db import models

# Create your models here.
class Product(models.Model):
    Name = models.CharField(max_length=200,null = True)
    Quantity = models.IntegerField(null = True)
    Image = models.FilePathField(path = "/img")
    Description = models.TextField()


