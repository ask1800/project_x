# Generated by Django 2.0.9 on 2019-01-05 16:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainfeed', '0005_headline_genre'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='headline',
            options={},
        ),
        migrations.RemoveField(
            model_name='headline',
            name='read',
        ),
        migrations.AddField(
            model_name='headline',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
