# Generated by Django 4.2.3 on 2023-07-25 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_updated_user_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='created',
            new_name='Created',
        ),
    ]
