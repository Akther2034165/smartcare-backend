# Generated by Django 5.0.4 on 2024-05-01 06:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_appointment_cancel'),
        ('doctor', '0004_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.availabletime'),
        ),
    ]
