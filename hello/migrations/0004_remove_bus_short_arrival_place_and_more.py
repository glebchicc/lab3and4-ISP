# Generated by Django 4.0.4 on 2022-05-31 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_bus_short_arrival_place_bus_short_departure_place'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bus',
            name='short_arrival_place',
        ),
        migrations.RemoveField(
            model_name='bus',
            name='short_departure_place',
        ),
    ]