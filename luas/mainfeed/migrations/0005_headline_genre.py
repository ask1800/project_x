# Generated by Django 2.0.9 on 2018-12-28 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainfeed', '0004_auto_20181228_0925'),
    ]

    operations = [
        migrations.AddField(
            model_name='headline',
            name='genre',
            field=models.CharField(blank=True, max_length=80),
        ),
    ]
