from django.contrib import admin
from .models import Hesap,Telefon,Mail,Adres
class HesapAdmin(admin.ModelAdmin):
    
    exclude=['ad']
    list_display=['ad','baglanti']
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False
class TelefonAdmin(admin.ModelAdmin):
    
    list_display=['ad']
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

class MailAdmin(admin.ModelAdmin):
    
    list_display=['ad']
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

class AdresAdmin(admin.ModelAdmin):
    
    list_display=['ad']
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


admin.site.register(Adres, AdresAdmin)
admin.site.register(Telefon, TelefonAdmin)
admin.site.register(Mail, MailAdmin)
admin.site.register(Hesap, HesapAdmin)
Mail._meta.verbose_name_plural = "Mail"
Telefon._meta.verbose_name_plural = "İletişim Numarası"
Hesap._meta.verbose_name_plural = "Sosyal Medya "
Adres._meta.verbose_name_plural = "Adres "