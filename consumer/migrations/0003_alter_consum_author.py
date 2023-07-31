# Generated by Django 4.2.3 on 2023-07-31 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_usermodel'),
        ('consumer', '0002_rename_consumuser_consum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consum',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consum_user', to='account.usermodel'),
        ),
    ]
