# Generated by Django 4.2.3 on 2023-07-28 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_alter_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profile',
        ),
    ]
