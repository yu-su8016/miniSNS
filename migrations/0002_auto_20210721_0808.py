# Generated by Django 2.2.12 on 2021-07-21 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='good_content',
            new_name='good_count',
        ),
    ]
