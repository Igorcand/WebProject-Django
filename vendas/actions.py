

def nfe_emitida(modeladmin, request, queryset):
    queryset.update(nfe_emitida=True)

def nfe_nao_emitida(modeladmin, request, queryset):
    queryset.update(nfe_emitida=False)


nfe_emitida.short_description = 'NFE Emitida'
nfe_nao_emitida.short_description = 'NFE não Emitida'
