# Generated by Django 3.1 on 2020-08-23 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20200823_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FilePathField(path='/mnt/c/Users/91894/desktop/SHOP-PY/Shop-py/WebApp/static/img/'),
        ),
    ]
