# Generated by Django 5.1.1 on 2024-10-05 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_farm_farmingmethods_farm_soiltype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='numberOfFarms',
        ),
        migrations.RemoveField(
            model_name='farm',
            name='company',
        ),
        migrations.AddField(
            model_name='company',
            name='primaryCommodity',
            field=models.CharField(default='Maize', max_length=255),
        ),
    ]
