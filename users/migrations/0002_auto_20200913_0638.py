# Generated by Django 3.1.1 on 2020-09-13 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdb',
            name='assigndb',
        ),
        migrations.AddField(
            model_name='userdb',
            name='assigndb',
            field=models.ManyToManyField(to='users.DatabaseList'),
        ),
    ]
