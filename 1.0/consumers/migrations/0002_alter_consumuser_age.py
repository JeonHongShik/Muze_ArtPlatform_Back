# Generated by Django 4.2.3 on 2023-07-25 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumuser',
            name='Age',
            field=models.PositiveIntegerField(),
        ),
    ]