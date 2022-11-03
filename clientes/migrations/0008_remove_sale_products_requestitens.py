# Generated by Django 4.1.2 on 2022-11-03 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0007_sale_nfe_emitida'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='products',
        ),
        migrations.CreateModel(
            name='RequestItens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('discount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.product')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.sale')),
            ],
        ),
    ]
