# Generated by Django 4.1.2 on 2022-11-09 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0009_remove_requestitens_product_remove_requestitens_sale_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'permissions': (('deletar_clientes', 'Pode deletar clientes'),)},
        ),
    ]
