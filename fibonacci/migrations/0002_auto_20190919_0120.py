# Generated by Django 2.2.5 on 2019-09-18 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fibonacci', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fibonacciseries',
            name='fibonacciNumber',
            field=models.CharField(max_length=200),
        ),
    ]
