# Generated by Django 3.1.4 on 2020-12-20 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20201220_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='about_image',
            field=models.ImageField(upload_to='media/about'),
        ),
    ]
