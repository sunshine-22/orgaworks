# Generated by Django 3.0.14 on 2022-06-27 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orga', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='mail',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='contactus',
            old_name='desc',
            new_name='message',
        ),
    ]
