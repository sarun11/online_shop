# Generated by Django 3.1.6 on 2021-02-08 10:32

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='intro',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
    ]
