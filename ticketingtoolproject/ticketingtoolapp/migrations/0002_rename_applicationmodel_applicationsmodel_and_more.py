# Generated by Django 4.1.3 on 2022-11-30 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticketingtoolapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ApplicationModel',
            new_name='ApplicationsModel',
        ),
        migrations.RenameModel(
            old_name='BookingModel',
            new_name='BookingsModel',
        ),
        migrations.RenameModel(
            old_name='ProductModel',
            new_name='ProductsModel',
        ),
    ]