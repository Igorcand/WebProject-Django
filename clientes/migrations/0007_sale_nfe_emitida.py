# Generated by Django 4.1.2 on 2022-11-03 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_product_sale_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='nfe_emitida',
            field=models.BooleanField(default=False),
        ),
    ]