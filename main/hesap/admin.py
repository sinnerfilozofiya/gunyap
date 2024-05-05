from django.contrib import admin
from .models import Hesap
class HesapAdmin(admin.ModelAdmin):
    
    exclude=['ad']
    list_display=['ad','baglanti']
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False
admin.site.register(Hesap, HesapAdmin)
Hesap._meta.verbose_name_plural = "Hesaplar"