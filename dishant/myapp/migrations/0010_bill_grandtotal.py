# Generated by Django 4.1.3 on 2022-12-24 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_rename_email_bill_bemail_rename_name_bill_bname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='grandtotal',
            field=models.CharField(default='', max_length=50),
        ),
    ]