# Generated by Django 2.2.5 on 2019-09-18 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FibonacciSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('fibonacciNumber', models.IntegerField()),
            ],
            options={
                'db_table': 'fibonacci_number',
            },
        ),
    ]
