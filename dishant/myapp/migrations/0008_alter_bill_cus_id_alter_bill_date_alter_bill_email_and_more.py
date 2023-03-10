# Generated by Django 4.1.3 on 2022-12-23 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_bill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='cus_id',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='bill',
            name='date',
            field=models.TextField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='bill',
            name='email',
            field=models.EmailField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='bill',
            name='name',
            field=models.TextField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='bill',
            name='phone',
            field=models.CharField(default='', max_length=50),
        ),
    ]
