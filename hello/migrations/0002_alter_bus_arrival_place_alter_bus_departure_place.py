# Generated by Django 4.0.4 on 2022-05-31 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='arrival_place',
            field=models.CharField(max_length=50, verbose_name='Место назначения'),
        ),
        migrations.AlterField(
            model_name='bus',
            name='departure_place',
            field=models.CharField(max_length=50, verbose_name='Точка сбора'),
        ),
    ]
