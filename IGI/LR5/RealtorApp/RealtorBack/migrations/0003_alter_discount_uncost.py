# Generated by Django 5.0.6 on 2024-05-28 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RealtorBack', '0002_remove_immovables_responsuser_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='uncost',
            field=models.FloatField(default=1),
        ),
    ]