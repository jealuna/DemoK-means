# Generated by Django 2.1.3 on 2020-01-03 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_lugar_clusters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lugar',
            name='clusters',
            field=models.PositiveIntegerField(),
        ),
    ]
