# Generated by Django 4.1.3 on 2022-11-29 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticketingtoolapp', '0003_alter_user_role'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
