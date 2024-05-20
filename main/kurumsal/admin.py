from django.contrib import admin
from .models import BizKimiz,Misyonumuz,Vizyonumuz,Madde,Belge
from main.admin import admin_site

class BizKimizAdmin(admin.ModelAdmin):
    list_display=['tanim']
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False
 
class MisyonumuzAdmin(admin.ModelAdmin):
    list_display=['tanim']
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False
class VizyonumuzAdmin(admin.ModelAdmin):
    list_display=['tanim']
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


class MaddeAdmin(admin.ModelAdmin):
    pass

class BelgeAdmin(admin.ModelAdmin):
    list_display=['ad']
 

admin_site.register(BizKimiz,BizKimizAdmin)
admin_site.register(Misyonumuz,MisyonumuzAdmin)
admin_site.register(Vizyonumuz,VizyonumuzAdmin)
admin_site.register(Madde,MaddeAdmin)
admin_site.register(Belge,BelgeAdmin)

