# Generated by Django 4.2.3 on 2023-07-31 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile',
            field=models.ImageField(default='', upload_to='media/profile'),
        ),
    ]
