# Generated by Django 3.0.7 on 2020-06-20 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20200619_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]