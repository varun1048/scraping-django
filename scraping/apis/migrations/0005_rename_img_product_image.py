# Generated by Django 4.0.4 on 2022-05-15 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0004_rename_ulr_product_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='img',
            new_name='image',
        ),
    ]
