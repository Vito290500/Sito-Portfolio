# Generated by Django 4.2.1 on 2023-07-01 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_myupdatecontact_projectstorage_link_github'),
    ]

    operations = [
        migrations.AddField(
            model_name='myupdatecontact',
            name='stmplib_token',
            field=models.CharField(max_length=500, null=True),
        ),
    ]