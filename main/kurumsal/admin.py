from django.contrib import admin
from .models import BizKimiz,Misyonumuz,Vizyonumuz,Madde,Belge,BelgeOge
from main.admin import admin_site

class BizKimizAdmin(admin.ModelAdmin):
    
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False
 
class MisyonumuzAdmin(admin.ModelAdmin):
   
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False
class VizyonumuzAdmin(admin.ModelAdmin):
    
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


class MaddeAdmin(admin.ModelAdmin):
    pass


class BelgeInline(admin.TabularInline):
    model = BelgeOge
    fields = ['belge', 'dosya',]
    extra = 0

class BelgeAdmin(admin.ModelAdmin):
    inlines = [BelgeInline]
    list_display=['ad']
    
    def has_delete_permission(self, request, obj=None):
        return False  # Disable the delete functionality for all objects

BelgeOge._meta.verbose_name="Belge Ögesi"
BelgeOge._meta.verbose_name_plural="Belge Ögeleri"
admin_site.register(BizKimiz,BizKimizAdmin)
admin_site.register(Misyonumuz,MisyonumuzAdmin)
admin_site.register(Vizyonumuz,VizyonumuzAdmin)
admin_site.register(Madde,MaddeAdmin)
admin_site.register(Belge,BelgeAdmin)

