from django.contrib import admin
from .models import Proje,ProjeImage,ProjeAçıklama
from main.admin import admin_site


class ImageInline(admin.TabularInline):
    model = ProjeImage
    extra = 0


class ProjeAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display=['ad','eklenme_tarihi']
    exclude = ('baslik',)
    
class ProjeAçıklamaAdmin(admin.ModelAdmin):
    # verbose_name, verbose_name_plural ve verbose_name olarak kullanılabilir
    list_display=['tanim',]
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False
    
    
admin.site.site_header = "Melisa-Sina"
admin.site.register(Proje, ProjeAdmin)
admin.site.register(ProjeAçıklama, ProjeAçıklamaAdmin)
ProjeAçıklama._meta.verbose_name='Açıklama'
ProjeAçıklama._meta.verbose_name_plural = "Açıklama"
Proje._meta.verbose_name_plural = "Projeler"
