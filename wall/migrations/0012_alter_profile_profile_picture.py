# Generated by Django 3.2 on 2022-04-10 20:30

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0011_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='profile_pic'),
        ),
    ]
