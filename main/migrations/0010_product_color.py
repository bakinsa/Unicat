# Generated by Django 4.0.2 on 2022-03-23 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_user_avatar_useravatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(default='#FFFFFF', max_length=10),
        ),
    ]
