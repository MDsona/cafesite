# Generated by Django 2.2.7 on 2020-06-14 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_auto_20200614_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapbox',
            name='mapURL',
            field=models.URLField(max_length=500),
        ),
    ]