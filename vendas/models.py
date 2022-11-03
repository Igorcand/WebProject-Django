from django.db import models
from clientes.models import Person
from produtos.models import Product


class Sale(models.Model):
    num = models.CharField(max_length=7)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    tax = models.DecimalField(max_digits=5, decimal_places=2)
    #RELACIONAMENTO ONE TO MANY - FOREING KEY 
    # Uma pessoa pode ter várias vendas
    person = models.ForeignKey(Person, null=True, blank=True, on_delete=models.PROTECT)

    #RELACIONAMENTO MANY TO MANY
    #Várias vendas podem ter vários produtos, não importando com repetições
    #products = models.ManyToManyField(Product, blank=True)
    nfe_emitida = models.BooleanField(default=False)


    # def get_total(self):
    #     tot = 0
    #     for product in self.products.all():
    #         tot+= product.price 

    #     return (tot - self.discount) - self.tax 


    def __str__(self):
        return self.num


class RequestItens(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField()
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.sale.num + '-' + self.product.name

