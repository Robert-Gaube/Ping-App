# Generated by Django 3.2.17 on 2023-02-14 12:40

from django.db import migrations, models
import ping.models


class Migration(migrations.Migration):

    dependencies = [
        ('ping', '0002_setup_uefi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setup',
            name='name',
            field=models.CharField(max_length=50, validators=[ping.models.validate_name]),
        ),
    ]
