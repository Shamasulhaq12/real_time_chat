# Generated by Django 3.2.15 on 2023-11-09 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_alter_userprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_online',
            field=models.BooleanField(default=False),
        ),
    ]
