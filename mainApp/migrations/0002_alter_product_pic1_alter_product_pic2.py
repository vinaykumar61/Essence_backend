# Generated by Django 5.1.2 on 2024-10-19 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pic1',
            field=models.ImageField(upload_to='product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pic2',
            field=models.ImageField(default=None, upload_to='product'),
            preserve_default=False,
        ),
    ]