# Generated by Django 2.2.10 on 2021-09-09 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riders', '0009_auto_20210908_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicetype',
            name='image',
            field=models.ImageField(blank=True, default='cars/1.jpg', null=True, upload_to='cars/'),
        ),
    ]
