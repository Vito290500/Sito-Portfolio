# Generated by Django 4.2.1 on 2023-06-29 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_projectstorage_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectstorage',
            old_name='slug',
            new_name='lenguage',
        ),
    ]
