# Generated by Django 4.0.4 on 2022-05-11 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0003_rename_hamrobazaar_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='ulr',
            new_name='url',
        ),
    ]
