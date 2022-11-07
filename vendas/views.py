from django.shortcuts import render
from django.views import View
from django.db.models import Sum, F, FloatField, Max, Avg, Min, Count
from .models import Sale

class DashboardView(View):
    def get(self, request):
        media = Sale.objects.all().aggregate(Avg('value'))['value__avg']
        media_desc = Sale.objects.all().aggregate(Avg('discount'))['discount__avg']
        min = Sale.objects.all().aggregate(Min('value'))['value__min']
        max = Sale.objects.all().aggregate(Max('value'))['value__max']
        qnt = Sale.objects.all().aggregate(Count('id'))['id__count']
        qnt_nfe = Sale.objects.filter(nfe_emitida=True).aggregate(Count('id'))['id__count']

        return render(request, 'vendas/dashboard.html', {'media':media, 'media_desc':media_desc, 'min': min, 'max': max, 'qnt':qnt, 'qnt_nfe': qnt_nfe})
