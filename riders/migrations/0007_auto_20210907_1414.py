# Generated by Django 2.2.10 on 2021-09-07 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('riders', '0006_ride_service_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='ride',
            name='service_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='riders.ServiceType'),
            preserve_default=False,
        ),
    ]
