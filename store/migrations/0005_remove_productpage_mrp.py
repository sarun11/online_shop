# Generated by Django 3.1.6 on 2021-02-08 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20210208_2031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productpage',
            name='mrp',
        ),
    ]
