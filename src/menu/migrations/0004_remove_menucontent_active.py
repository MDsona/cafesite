# Generated by Django 2.2.7 on 2020-03-14 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_menucontent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menucontent',
            name='active',
        ),
    ]