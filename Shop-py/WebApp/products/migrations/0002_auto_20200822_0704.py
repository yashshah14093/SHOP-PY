# Generated by Django 3.1 on 2020-08-22 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FilePathField(path='C:\\Users\\91894\\Desktop\\SHOP-PY\\supplier-data\\JPEG_images\\'),
        ),
    ]