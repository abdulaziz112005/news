from django.contrib import admin

from .models import *


class CatalogAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']

admin.site.register(Catalog, CatalogAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Contact, ContactAdmin)

