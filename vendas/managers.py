from django.db import models 
from django.db.models import Sum, F, FloatField, Max, Avg, Min, Count

class SaleManager(models.Manager):
    def media(self):
        return self.all().aggregate(Avg('value'))['value__avg']

    def media_desc(self):
        return self.all().aggregate(Avg('discount'))['discount__avg']
    
    def min_value(self):
        return self.all().aggregate(Min('value'))['value__min']
    
    def max_value(self):
        return self.all().aggregate(Max('value'))['value__max']
    
    def qnt_pedido(self):
        return self.all().aggregate(Count('id'))['id__count']
    
    def qnt_pedido_nfe(self):
        return self.filter(nfe_emitida=True).aggregate(Count('id'))['id__count']