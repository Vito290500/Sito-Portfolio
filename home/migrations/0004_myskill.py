# Generated by Django 4.2.1 on 2023-07-01 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_slug_projectstorage_lenguage'),
    ]

    operations = [
        migrations.CreateModel(
            name='MySKill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lenguage', models.CharField(max_length=100)),
                ('conoscenza', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
