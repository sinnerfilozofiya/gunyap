from django.contrib import admin
from .models import KariyerAçıklama

    
class KariyerAçıklamaAdmin(admin.ModelAdmin):
    # verbose_name, verbose_name_plural ve verbose_name olarak kullanılabilir
    list_display=['tanim',]
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False
    

admin.site.register(KariyerAçıklama, KariyerAçıklamaAdmin)
KariyerAçıklama._meta.verbose_name='Açıklama'
KariyerAçıklama._meta.verbose_name_plural = "Açıklama"

