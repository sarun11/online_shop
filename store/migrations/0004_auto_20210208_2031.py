# Generated by Django 3.1.6 on 2021-02-08 14:46

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('store', '0003_auto_20210208_1955'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productpage',
            old_name='availabile',
            new_name='inStock',
        ),
        migrations.AddField(
            model_name='categorypage',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='categorypage',
            name='description',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Description of the Category', null=True),
        ),
        migrations.AddField(
            model_name='categorypage',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='categorypage',
            name='name',
            field=wagtail.core.fields.RichTextField(help_text='Enter page title here', null=True),
        ),
        migrations.AddField(
            model_name='productpage',
            name='mrp',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='productpage',
            name='name',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Name of the product', null=True),
        ),
        migrations.AddField(
            model_name='productpage',
            name='note',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Add notes (if any)', null=True),
        ),
        migrations.AddField(
            model_name='productpage',
            name='sku',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='productpage',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AlterField(
            model_name='productpage',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
