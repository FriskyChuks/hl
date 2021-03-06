# Generated by Django 2.2.10 on 2021-09-10 09:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('riders', '0011_ride_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='ride_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ride',
            name='ride_time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
