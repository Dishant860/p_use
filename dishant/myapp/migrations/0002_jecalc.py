# Generated by Django 4.1.3 on 2022-12-10 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JeCalc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(max_length=50)),
                ('weight', models.FloatField(max_length=50)),
                ('total', models.FloatField(max_length=50)),
            ],
        ),
    ]