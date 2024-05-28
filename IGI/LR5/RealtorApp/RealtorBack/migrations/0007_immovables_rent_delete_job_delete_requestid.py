# Generated by Django 5.0.6 on 2024-05-27 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RealtorBack', '0006_rename_contacts_contact_rename_news_new_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Immovables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Описание')),
                ('tp', models.TextField(verbose_name='')),
                ('cost', models.IntegerField(verbose_name='Цена')),
            ],
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Услуга')),
                ('cost', models.IntegerField(verbose_name='Цена')),
                ('duration', models.DateTimeField(verbose_name='Длительность аренды')),
            ],
        ),
        migrations.DeleteModel(
            name='Job',
        ),
        migrations.DeleteModel(
            name='RequestId',
        ),
    ]
