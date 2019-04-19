# Generated by Django 2.2 on 2019-04-15 18:08

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0005_problem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='location',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None, verbose_name='Location Of Climb'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Problem/Route Name'),
        ),
    ]