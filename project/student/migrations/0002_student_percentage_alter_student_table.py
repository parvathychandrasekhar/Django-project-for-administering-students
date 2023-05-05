# Generated by Django 4.2 on 2023-04-27 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='percentage',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterModelTable(
            name='student',
            table='student',
        ),
    ]
