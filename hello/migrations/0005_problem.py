# Generated by Django 2.2 on 2019-04-11 16:08

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0004_auto_20190409_2106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mp_id', models.IntegerField()),
                ('boulder', models.BooleanField(default=True)),
                ('location', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
                ('lat', models.CharField(max_length=20)),
                ('lon', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=200)),
                ('area_id', models.IntegerField()),
            ],
        ),
    ]
