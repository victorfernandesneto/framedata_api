# Generated by Django 4.2.6 on 2023-10-06 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('framedata', '0003_character_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='image',
        ),
    ]
