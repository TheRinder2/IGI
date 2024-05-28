# Generated by Django 5.0.6 on 2024-05-28 15:55

import datetime
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField(null=True, validators=[django.core.validators.MaxValueValidator(limit_value=datetime.date(2006, 5, 28), message='You must be 18 y.o or older!'), django.core.validators.MinValueValidator(limit_value=datetime.date(1904, 6, 27), message='You must enter your real age!')])),
                ('fullName', models.TextField(verbose_name='ФИО')),
                ('phone', models.TextField(verbose_name='Номер')),
                ('passport', models.TextField(verbose_name='Паспорт')),
                ('isworker', models.BooleanField(default=False, verbose_name='Работник')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
