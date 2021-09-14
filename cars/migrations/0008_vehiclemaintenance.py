# Generated by Django 2.2.10 on 2021-09-14 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_auto_20210910_0844'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleMaintenance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('routine', 'Routine'), ('others', 'Others')], max_length=20)),
                ('date_maintained', models.DateField()),
                ('amount_spent', models.DecimalField(decimal_places=2, default=0.0, max_digits=65)),
                ('description', models.TextField(max_length=500)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.Car')),
            ],
        ),
    ]
