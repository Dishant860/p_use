# Generated by Django 4.1.3 on 2022-12-24 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_remove_bill_qrimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='bphone',
            field=models.CharField(default='', max_length=10),
        ),
    ]
