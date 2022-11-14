from django.http import HttpResponseNotFound

def nfe_emitida(modeladmin, request, queryset):
    if request.user.has_perm('vendas.setar_nfe'):
        queryset.update(nfe_emitida=True)
    else:
        return HttpResponseNotFound('<h1> Sem permissão </h1>')

def nfe_nao_emitida(modeladmin, request, queryset):
    queryset.update(nfe_emitida=False)


nfe_emitida.short_description = 'NFE Emitida'
nfe_nao_emitida.short_description = 'NFE não Emitida'
