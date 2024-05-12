from django.contrib import admin
from .models import KariyerAçıklama,KariyerGörsel

    
class KariyerAçıklamaAdmin(admin.ModelAdmin):
    # verbose_name, verbose_name_plural ve verbose_name olarak kullanılabilir
    list_display=['tanim',]
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False
class KariyerGörselAdmin(admin.ModelAdmin):
    # verbose_name, verbose_name_plural ve verbose_name olarak kullanılabilir
    list_display=['tanim',]
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

admin.site.register(KariyerAçıklama, KariyerAçıklamaAdmin)
admin.site.register(KariyerGörsel, KariyerGörselAdmin)


KariyerAçıklama._meta.verbose_name_plural = "Açıklama"
KariyerGörsel._meta.verbose_name_plural = "Görsel"
