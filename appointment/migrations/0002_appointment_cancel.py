# Generated by Django 5.0.4 on 2024-05-01 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='cancel',
            field=models.BooleanField(default=False),
        ),
    ]
