# Generated by Django 2.1.3 on 2019-01-30 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lugar',
            name='clusters',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
