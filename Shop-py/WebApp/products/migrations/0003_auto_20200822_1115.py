# Generated by Django 3.1 on 2020-08-22 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200822_0704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FilePathField(path='/mnt/c/Users/91894/Desktop/SHOP-PY/supplier-data/JPEG_images'),
        ),
    ]