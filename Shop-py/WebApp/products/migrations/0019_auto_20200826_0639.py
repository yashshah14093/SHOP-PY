# Generated by Django 3.1 on 2020-08-26 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_auto_20200825_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Image',
            field=models.FilePathField(path='img/'),
        ),
    ]
