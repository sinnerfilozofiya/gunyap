from django.contrib import admin
from .models import Hizmet,HizmetAçıklama
from main.admin import admin_site
from django import forms


class AçıklamaAdmin(admin.ModelAdmin):
    # verbose_name, verbose_name_plural ve verbose_name olarak kullanılabilir
    list_display=['tanim',]
    
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False
 
class HizmetAdmin(admin.ModelAdmin):
    # verbose_name, verbose_name_plural ve verbose_name olarak kullanılabilir
    list_display=['ad','baslik',]
    exclude = ('baslik',)


admin.site.register(Hizmet,HizmetAdmin)
admin.site.register(HizmetAçıklama,AçıklamaAdmin)
Hizmet._meta.verbose_name_plural = "Hizmetler"
HizmetAçıklama._meta.verbose_name_plural = "Açıklama"

