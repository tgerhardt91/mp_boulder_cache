# Generated by Django 2.2 on 2019-04-09 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_auto_20190409_1642'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaCoordinates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.CharField(max_length=20)),
                ('lon', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
