# Generated by Django 5.0.6 on 2024-05-26 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='pasport',
            new_name='passport',
        ),
    ]
