# Generated by Django 4.2.3 on 2023-08-08 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_performancepost_pay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performancepost',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
