# Generated by Django 3.1 on 2021-05-24 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_unread_userstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unread',
            name='receiver',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
