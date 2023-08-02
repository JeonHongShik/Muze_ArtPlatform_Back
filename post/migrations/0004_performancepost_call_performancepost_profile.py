# Generated by Django 4.2.3 on 2023-08-01 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_alter_performancepost_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='performancepost',
            name='call',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='performancepost',
            name='profile',
            field=models.URLField(blank=True, null=True),
        ),
    ]
