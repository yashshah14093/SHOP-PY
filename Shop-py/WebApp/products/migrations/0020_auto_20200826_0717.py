# Generated by Django 3.1 on 2020-08-26 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20200826_0639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Image',
            field=models.ImageField(upload_to='img/'),
        ),
    ]