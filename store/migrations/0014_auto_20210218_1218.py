# Generated by Django 3.1.6 on 2021-02-18 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_auto_20210217_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile',
            name='color',
            field=models.CharField(choices=[('Grey', 'Grey'), ('Black', 'Black'), ('White', 'White'), ('Light Blue', 'Light Blue')], default='Black', max_length=25),
        ),
    ]
