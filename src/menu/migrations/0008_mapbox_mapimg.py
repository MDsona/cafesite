# Generated by Django 2.2.7 on 2020-06-15 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_auto_20200614_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='mapbox',
            name='mapIMG',
            field=models.ImageField(default='default.jpg', upload_to='map_imgs'),
        ),
    ]