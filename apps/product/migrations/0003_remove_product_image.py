# Generated by Django 5.1.1 on 2024-09-27 04:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_rename_test_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
