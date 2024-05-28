# Generated by Django 5.0.6 on 2024-05-26 15:36

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
                ('age', models.IntegerField()),
                ('fullName', models.TextField(verbose_name='ФИО')),
                ('phone', models.TextField(verbose_name='Номер')),
                ('pasport', models.TextField(verbose_name='Паспорт')),
                ('isworker', models.BooleanField(default=False, verbose_name='Работник')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]