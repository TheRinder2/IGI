# Generated by Django 5.0.6 on 2024-09-20 15:53

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(null=True, validators=[django.core.validators.MaxValueValidator(limit_value=datetime.date(2006, 9, 20), message='You must be 18 y.o or older!'), django.core.validators.MinValueValidator(limit_value=datetime.date(1904, 10, 20), message='You must enter your real age!')]),
        ),
    ]