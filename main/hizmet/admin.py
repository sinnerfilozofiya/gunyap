from django.contrib import admin
from .models import Hizmet
from main.admin import admin_site
from django import forms



class HizmetAdmin(admin.ModelAdmin):
    # verbose_name, verbose_name_plural ve verbose_name olarak kullanılabilir
    list_display=['ad','baslik','tanim',]
    exclude = ('baslik',)

admin.site.site_header = "Melisa-Sina"
admin.site.register(Hizmet,HizmetAdmin)
Hizmet._meta.verbose_name_plural = "Hizmetler"
