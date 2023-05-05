# Generated by Django 4.2 on 2023-04-27 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('physics_marks', models.PositiveIntegerField()),
                ('chemistry_marks', models.PositiveIntegerField()),
                ('maths_marks', models.PositiveIntegerField()),
                ('computer_science_marks', models.PositiveIntegerField()),
            ],
        ),
    ]