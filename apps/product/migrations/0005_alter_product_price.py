# Generated by Django 5.1.1 on 2024-09-27 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=4, max_length=100, verbose_name='Цена'),
        ),
    ]
