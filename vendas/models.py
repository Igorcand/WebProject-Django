from django.db import models
from clientes.models import Person
from produtos.models import Product

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.db.models import Sum, F, FloatField, Max
from .managers import SaleManager

class Sale(models.Model):
    num = models.CharField(max_length=7)
    value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    tax = models.DecimalField(max_digits=5, decimal_places=2)
    #RELACIONAMENTO ONE TO MANY - FOREING KEY 
    # Uma pessoa pode ter várias vendas
    person = models.ForeignKey(Person, null=True, blank=True, on_delete=models.PROTECT)

    #RELACIONAMENTO MANY TO MANY
    #Várias vendas podem ter vários produtos, não importando com repetições
    #products = models.ManyToManyField(Product, blank=True)
    nfe_emitida = models.BooleanField(default=False)

    objects = SaleManager()


    class Meta:
        permissions = (
            ('setar_nfe', 'Usuario pode alterar NFE'),
            ('ver_dashboard', 'Pode visualizar o dashboard'),
            ('permissao3', 'Permissão 3'),
        )


    def calc_total(self):
        total = self.requestitens_set.all().aggregate(
            tot_ped = Sum(
                (F('quantity') * F('product__price')) - F('discount'),
                output_field = FloatField()
                )
        )['tot_ped']
        try:
            t = float(self.tax)
        except:
            t = 0
        
        try:
            d = float(self.discount)
        except:
            d = 0

        total = total - t - d
        self.value = total
        Sale.objects.filter(id=self.id).update(value=total)


    def __str__(self):
        return self.num


class RequestItens(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField()
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.sale.num + '-' + self.product.name

@receiver(post_save,sender=RequestItens)
def update_vendas_total(sender, instance, **kwargs):
    instance.sale.calc_total()

@receiver(post_save,sender=Sale)
def update_vendas_total2(sender, instance, **kwargs):
    instance.calc_total()

