# Generated by Django 3.2 on 2022-03-22 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0003_auto_20220320_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='invalid-slug', max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
