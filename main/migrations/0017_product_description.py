# Generated by Django 4.0.2 on 2022-04-13 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_store_address_application'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]