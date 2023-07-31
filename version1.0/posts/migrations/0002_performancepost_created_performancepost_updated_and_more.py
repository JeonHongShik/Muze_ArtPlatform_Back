# Generated by Django 4.2.3 on 2023-07-25 12:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='performancepost',
            name='Created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='performancepost',
            name='Updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='performancepost',
            name='post_image',
            field=models.ImageField(upload_to='about_Post/venue_images/'),
        ),
    ]