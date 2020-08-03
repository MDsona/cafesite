# Generated by Django 2.2.7 on 2020-08-03 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0013_auto_20200803_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='forreser',
            name='mobile_number',
            field=models.CharField(blank=True, help_text='مثال:0511111111', max_length=10, null=True, verbose_name='رقم الجوال'),
        ),
        migrations.AddField(
            model_name='forreser',
            name='session_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='التوقيت'),
        ),
        migrations.AddField(
            model_name='forreser',
            name='session_duration',
            field=models.IntegerField(blank=True, help_text='ساعة', null=True, verbose_name='مدة الجلسة'),
        ),
    ]