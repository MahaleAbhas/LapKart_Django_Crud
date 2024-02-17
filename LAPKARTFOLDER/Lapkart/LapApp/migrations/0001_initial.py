# Generated by Django 5.0.2 on 2024-02-13 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lap_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=35)),
                ('model', models.CharField(max_length=35)),
                ('ram', models.IntegerField()),
                ('rom', models.IntegerField()),
                ('prices', models.FloatField()),
            ],
        ),
    ]
