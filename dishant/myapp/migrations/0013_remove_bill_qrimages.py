# Generated by Django 4.1.3 on 2022-12-24 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_bill_qrimages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='qrimages',
        ),
    ]