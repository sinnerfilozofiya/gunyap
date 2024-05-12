from django.contrib import admin
from .models import Mesaj

# Register your models here.
class MesajAdmin(admin.ModelAdmin):
    # verbose_name, verbose_name_plural ve verbose_name olarak kullanılabilir
    list_display=['gönderen','mail','tarih','konu','mesaj']
    verbose_name = "Özel Sayfa Adı"
    verbose_name_plural = "Özel Sayfa Adları"


admin.site.register(Mesaj,MesajAdmin)
Mesaj._meta.verbose_name_plural = "Mesajlar"

