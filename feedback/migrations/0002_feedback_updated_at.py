# Generated by Django 5.1.4 on 2024-12-13 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
