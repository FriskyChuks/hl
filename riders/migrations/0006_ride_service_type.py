# Generated by Django 2.2.10 on 2021-09-07 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riders', '0005_delete_servicetype'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='service_type',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
