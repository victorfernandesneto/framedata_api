# Generated by Django 4.2.6 on 2023-10-06 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('framedata', '0002_character_delete_characters_alter_move_character'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
