# Generated by Django 3.1.6 on 2021-02-08 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_remove_productpage_mrp'),
    ]

    operations = [
        migrations.AddField(
            model_name='productpage',
            name='brand',
            field=models.CharField(max_length=50, null=True),
        ),
    ]