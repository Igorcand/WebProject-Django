from django.shortcuts import render
from django.views import View
from django.db.models import Sum, F, FloatField, Max, Avg, Min, Count
from .models import Sale
from django.http import HttpResponseNotFound

class DashboardView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('vendas.ver_dashboard'):
            return HttpResponseNotFound('Acesso negado, sem permissão')
        return super(DashboardView, self).dispatch(request, *args, **kwargs)


    def get(self, request):
        media = Sale.objects.media()
        media_desc = Sale.objects.media_desc()
        min = Sale.objects.min_value()
        max = Sale.objects.max_value()
        qnt = Sale.objects.qnt_pedido()
        qnt_nfe = Sale.objects.qnt_pedido_nfe()

        return render(request, 'vendas/dashboard.html', {'media':media, 'media_desc':media_desc, 'min': min, 'max': max, 'qnt':qnt, 'qnt_nfe': qnt_nfe})
