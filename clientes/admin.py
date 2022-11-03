from django.contrib import admin
from .models import Person, Document

class PersonAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dados Pessoais', {
            'fields': ('first_name', 'last_name', 'doc')
            }),
        ('Dados Complementares', {
            'classes': ('collapse',),
            'fields': ('age', 'salary', 'bio', 'photo')
            })
    )
    #fields = [('first_name', 'last_name'), 'age', 'salary', 'bio', 'photo']
    #exclude = ['bio']
    list_display = ['first_name', 'last_name', 'age', 'salary', 'bio', 'has_photo']
    list_filter = ('age', 'salary')
    search_fields = ('id', 'first_name')

    def has_photo(self, obj):
        if obj.photo:
            return True
        else:
            return False 
        
    has_photo.short_description = 'Has photo'



admin.site.register(Person, PersonAdmin)
admin.site.register(Document)
#admin.site.register(Product)


