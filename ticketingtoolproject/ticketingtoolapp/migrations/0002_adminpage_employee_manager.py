# Generated by Django 4.1 on 2022-11-23 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketingtoolapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]