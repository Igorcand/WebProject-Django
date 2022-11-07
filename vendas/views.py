from django.shortcuts import render
from django.views import View
from django.db.models import Sum, F, FloatField, Max, Avg, Min, Count
from .models import Sale

class DashboardView(View):
    def get(self, request):
        media = Sale.objects.media()
        media_desc = Sale.objects.media_desc()
        min = Sale.objects.min_value()
        max = Sale.objects.max_value()
        qnt = Sale.objects.qnt_pedido()
        qnt_nfe = Sale.objects.qnt_pedido_nfe()

        return render(request, 'vendas/dashboard.html', {'media':media, 'media_desc':media_desc, 'min': min, 'max': max, 'qnt':qnt, 'qnt_nfe': qnt_nfe})
