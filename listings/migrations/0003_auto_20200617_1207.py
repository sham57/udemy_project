# Generated by Django 3.0.7 on 2020-06-17 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_listing_sqft'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='beedrooms',
            new_name='bedrooms',
        ),
    ]
