# Generated by Django 4.1.2 on 2022-11-09 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0004_alter_sale_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sale',
            options={'permissions': (('setar_nfe', 'Usuario pode alterar NFE'), ('permissao2', 'Permissão 2'), ('permissao3', 'Permissão 3'))},
        ),
    ]
