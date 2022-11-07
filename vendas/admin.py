from django.contrib import admin
from .models import Sale, RequestItens
from .actions import nfe_emitida, nfe_nao_emitida


class RequestItemInLine(admin.TabularInline):
    model = RequestItens
    extra = 1


class SaleAdmin(admin.ModelAdmin):
    readonly_fields = ('value', )
    #raw_id_fields = ('person', )
    autocomplete_fields = ('person', )

    list_filter = ('person__doc', 'discount')
    list_display = ('id', 'person',  'nfe_emitida')

    search_fields = ('id', 'person__first_name', 'person__doc__num_doc')
    actions = [nfe_emitida, nfe_nao_emitida]
    inlines = [RequestItemInLine]
    #filter_horizontal = ['products',]

admin.site.register(Sale, SaleAdmin)
admin.site.register(RequestItens)