# Generated by Django 3.1 on 2020-08-23 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200823_1451'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='Description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='Image',
        ),
        migrations.AddField(
            model_name='product',
            name='Name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='Quantity',
            field=models.IntegerField(null=True),
        ),
    ]