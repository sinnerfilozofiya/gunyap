from django.contrib import admin
from .models import Slayt
from main.admin import admin_site

class SlaytAdmin(admin.ModelAdmin):
    
    # verbose_name, verbose_name_plural ve verbose_name olarak kullanılabilir
    list_display=['order']
    verbose_name = "Özel Sayfa Adı"
    verbose_name_plural = "Özel Sayfa Adları"

admin.site.site_header = "Melisa-Sina"
admin_site.register(Slayt,SlaytAdmin)

Slayt._meta.verbose_name_plural = "Slaytlar"
