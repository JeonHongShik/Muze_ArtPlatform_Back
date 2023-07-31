# Generated by Django 4.2.3 on 2023-07-31 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_usermodel'),
        ('post', '0002_performancepost_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performancepost',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Post_author', to='account.usermodel'),
        ),
    ]
