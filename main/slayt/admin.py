from django.contrib import admin
from .models import Slayt,Slogan,SlaytAçıklama
from main.admin import admin_site


class SloganAdmin(admin.ModelAdmin):
    # verbose_name, verbose_name_plural ve verbose_name olarak kullanılabilir
    list_display=['tanim',]
   
    
class SlaytAçıklamaAdmin(admin.ModelAdmin):
    # verbose_name, verbose_name_plural ve verbose_name olarak kullanılabilir
    list_display=['tanim',]
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

class SlaytAdmin(admin.ModelAdmin):
    # verbose_name, verbose_name_plural ve verbose_name olarak kullanılabilir
    list_display=['order']
    verbose_name = "Özel Sayfa Adı"
    verbose_name_plural = "Özel Sayfa Adları"

admin.site.site_header = "Melisa-Sina"
admin.site.register(Slayt,SlaytAdmin)
admin.site.register(Slogan,SloganAdmin)
admin.site.register(SlaytAçıklama,SlaytAçıklamaAdmin)
Slayt._meta.verbose_name_plural = "Slaytlar"
Slogan._meta.verbose_name_plural = "Slogan"
SlaytAçıklama._meta.verbose_name_plural = "Açıklama"
