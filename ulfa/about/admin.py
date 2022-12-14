from django.contrib import admin

from . import models
class ulf(admin.ModelAdmin):
    list_display = ['NAMA','NPM']
    search_fields = ['NAMA','NPM']
    list_filter = ['NAMA','NPM']
    list_per_page = 2
    

admin.site.register(models.habib,ulf)
admin.site.register(models.tahu)
